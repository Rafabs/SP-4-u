import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import logging
from screeninfo import get_monitors
import calendar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mplcursors  # Para tooltips interativos

# Configuração do logger
logging.basicConfig(filename="Mapa_dos_Trilhos/log.txt", filemode="a", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Carregar CSV e JSON
csv_file = "Mapa_dos_Trilhos/Demanda_Passageiros/data_passenger.csv"
df = pd.read_csv(csv_file, sep=";", encoding="utf-8")

json_file = "Mapa_dos_Trilhos/Linhas/trajeto.json"
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Dicionários de mapeamento
estacoes_dict = {}
linhas_dict = {}

mapa_linhas = {
    "LINHA 1": "01 - AZUL",
    "LINHA 2": "02 - VERDE",
    "LINHA 3": "03 - VERMELHA",
    "LINHA 4": "04 - AMARELA",
    "LINHA 5": "05 - LILÁS",
    "LINHA 15": "15 - PRATA"
}

for nome_arquivo, linha in data.items():
    if "LINHA" in linha:
        linhas_dict[linha["LINHA"]] = linha["LINHA"]

    if "TRAJETO" in linha:
        for estacao in linha["TRAJETO"]:
            estacoes_dict[estacao["TAG"]] = estacao["primary"]

# Aplicar mapeamento
df["ESTACAO"] = df["ESTACAO"].map(estacoes_dict)
df.dropna(subset=["ESTACAO"], inplace=True)
df["LINHA"] = df["LINHA"].map(mapa_linhas)

def passageiro_estacao():
    """Janela para exibir o gráfico de demanda de passageiros com hover detalhado."""

    logging.info("Abrindo Demanda de Passageiros")

    # Criar janela Tkinter
    root = tk.Toplevel()
    monitor = get_monitors()[0]
    root.geometry(f"{monitor.width}x{monitor.height}")
    root.attributes("-fullscreen", True)
    root.overrideredirect(True)
    root.title("Demanda de Passageiros")

    def sair(event=None):
        root.destroy()
        logging.info("Fechando Demanda de Passageiros")

    root.bind("<Escape>", sair)

    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    tk.Label(frame, text="Selecione uma Linha:", font=("Arial", 14, "bold")).pack(pady=10)
    combobox_linha = ttk.Combobox(frame, values=sorted(linhas_dict.keys()), font=("Arial", 12))
    combobox_linha.pack()

    tk.Label(frame, text="Selecione uma Estação:", font=("Arial", 14, "bold")).pack(pady=10)
    combobox_estacao = ttk.Combobox(frame, font=("Arial", 12))
    combobox_estacao.pack()

    graph_frame = tk.Frame(frame)
    graph_frame.pack(expand=True, fill="both")

    def atualizar_estacoes(event=None):
        """Atualiza as estações ao escolher uma linha."""
        linha_selecionada = combobox_linha.get()
        estacoes_filtradas = [
            estacao["primary"] for linha in data.values() if linha["LINHA"] == linha_selecionada
            for estacao in linha.get("TRAJETO", [])
        ]
        combobox_estacao["values"] = sorted(estacoes_filtradas)
        if estacoes_filtradas:
            combobox_estacao.current(0)

    def exibir_grafico(event=None):
        """Gera um gráfico interativo exibindo todos os itens de uma estação."""
        linha_selecionada = combobox_linha.get()
        estacao_selecionada = combobox_estacao.get()

        if not linha_selecionada or not estacao_selecionada:
            return

        # Filtrar os dados da estação e da linha selecionadas
        df_filtrado = df[
            (df["ESTACAO"] == estacao_selecionada) &
            (df["LINHA"] == linha_selecionada)
        ].copy()

        if df_filtrado.empty:
            logging.warning(f"Sem dados para {estacao_selecionada}")
            return

        # Verificar colunas obrigatórias
        colunas_necessarias = {"ANO", "MES", "MEDIA", "DETALHE_1", "DETALHE_2"}
        if not colunas_necessarias.issubset(df_filtrado.columns):
            logging.error(f"Colunas ausentes: {colunas_necessarias - set(df_filtrado.columns)}")
            return

        meses_map = {
            "JANEIRO": 1, "FEVEREIRO": 2, "MARÇO": 3, "ABRIL": 4, "MAIO": 5, "JUNHO": 6,
            "JULHO": 7, "AGOSTO": 8, "SETEMBRO": 9, "OUTUBRO": 10, "NOVEMBRO": 11, "DEZEMBRO": 12
        }

        # Convertendo colunas
        df_filtrado["MES"] = df_filtrado["MES"].str.upper().map(meses_map)
        df_filtrado.dropna(subset=["MES", "ANO"], inplace=True)
        df_filtrado["MES"] = df_filtrado["MES"].astype(int)
        df_filtrado["ANO"] = df_filtrado["ANO"].astype(int)
        df_filtrado["MEDIA"] = pd.to_numeric(df_filtrado["MEDIA"], errors="coerce")

        logging.info("Linha selecionada:", linha_selecionada) 
        logging.info("Estação selecionada:", estacao_selecionada) 
        logging.info("DataFrame filtrado:", df[(df["LINHA"] == linha_selecionada) & (df["ESTACAO"] == estacao_selecionada)])

        # Criar coluna MES_ANO
        df_filtrado["MES_ANO"] = df_filtrado.apply(lambda x: f"{calendar.month_abbr[x['MES']]}-{x['ANO']}", axis=1)
        df_filtrado.sort_values(by=["ANO", "MES"], inplace=True)

        # Criar gráfico
        sns.set_style("whitegrid")
        fig, ax = plt.subplots(figsize=(12, 6))

        # Adicionar os pontos e a linha
        scatter = ax.scatter(
            df_filtrado["MES_ANO"], 
            df_filtrado["MEDIA"], 
            color="royalblue", 
            s=100, 
            edgecolor="black"
        )
        sns.lineplot(
            x=df_filtrado["MES_ANO"], 
            y=df_filtrado["MEDIA"], 
            marker="o", 
            color="royalblue", 
            linewidth=2, 
            ax=ax
        )

        # Personalizar eixos
        ax.set_xticks(range(len(df_filtrado["MES_ANO"].unique())))
        ax.set_xticklabels(
            df_filtrado["MES_ANO"].unique(), 
            rotation=45, 
            ha="right"
        )

        # Configurações visuais
        ax.set_title(
            f"Demanda de Passageiros - {estacao_selecionada} - LINHA ({linha_selecionada})", 
            fontsize=14, 
            fontweight="bold"
        )
        ax.set_xlabel("Período", fontsize=12)
        ax.set_ylabel("Média de Passageiros [em milhares]", fontsize=12)
        ax.grid(True, linestyle="--", alpha=0.6)

        # Adicionar interatividade com hover
        cursor = mplcursors.cursor(scatter, hover=True)
        cursor.connect(
            "add", 
            lambda sel: sel.annotation.set_text(
                f"Mês: {df_filtrado.iloc[sel.index]['MES_ANO']}\n"
                f"Passageiros: {df_filtrado.iloc[sel.index]['MEDIA']} mil\n"
                f"{df_filtrado.iloc[sel.index]['DETALHE_1']}\n"
                f"{df_filtrado.iloc[sel.index]['DETALHE_2']}"
            )
        )

        # Exibir no Tkinter
        for widget in graph_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")

    combobox_linha.bind("<<ComboboxSelected>>", atualizar_estacoes)
    combobox_estacao.bind("<<ComboboxSelected>>", exibir_grafico)

    root.mainloop()