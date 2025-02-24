import pandas as pd
import tkinter as tk
from tkinter import ttk
import logging
from screeninfo import get_monitors
import os

# Configuração do logger
logging.basicConfig(filename='Mapa_dos_Trilhos\\log.txt', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Dicionário com os caminhos dos arquivos por ano
arquivos_od = {
    1997: "Mapa_dos_Trilhos\\Pesquisa_Origem_Destino\\OD1997\\Tabelas-OD1997\\Tab01_OD97.xls",
    2007: "Mapa_dos_Trilhos\\Pesquisa_Origem_Destino\\OD2007\\Tabelas-OD2007\\Tab01_OD2007.xlsx",
    2017: "Mapa_dos_Trilhos\\Pesquisa_Origem_Destino\\OD2017\\Tabelas-OD2017\\Tab01_OD2017.xlsx"
}

def carregar_dados(ano):
    """Carrega os dados do arquivo correspondente ao ano selecionado, tratando exceções."""
    if ano not in arquivos_od:
        logging.error(f"Erro: Ano {ano} não disponível.")
        return
    
    file_path = arquivos_od[ano]
    
    if not os.path.exists(file_path):
        logging.error(f"Erro: Arquivo não encontrado para {ano}: {file_path}")
        return
    
    try:
        if ano == 1977:
            # Tratamento especial para 1977: Pula 3 linhas e lê apenas colunas 0 e 1
            df = pd.read_excel(file_path, skiprows=3, usecols=[0, 1], names=["Município", "Nome do Município"])
        
        elif ano in [1997, 2007, 2017]:
            # Tratamento para os anos 1997, 2007 e 2017: Pula 6 linhas e lê todas as colunas
            df = pd.read_excel(file_path, skiprows=6)

        else:
            # Para outros anos (caso existam no futuro), lê normalmente
            df = pd.read_excel(file_path)

        logging.info(f"Dados do ano {ano} carregados com sucesso.")
        exibir_dados(df)

    except Exception as e:
        logging.error(f"Erro ao carregar os dados do ano {ano}: {str(e)}")

def exibir_dados(df):
    """ Exibe os dados da planilha no Treeview de forma formatada, sem sobreposição e com rolagem total """
    global tree, frame  

    # Criar o frame apenas na primeira vez
    if "frame" not in globals() or not frame.winfo_exists():
        frame = tk.Frame(tree.master)
        frame.pack(expand=True, fill="both")

        # Criar Treeview dentro do frame
        tree = ttk.Treeview(frame)
        
        # Criar barras de rolagem
        yscrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        xscrollbar = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)

        tree.configure(yscroll=yscrollbar.set, xscroll=xscrollbar.set)

        # Posicionar elementos
        yscrollbar.pack(side="right", fill="y")
        xscrollbar.pack(side="bottom", fill="x")
        tree.pack(expand=True, fill="both")

        # Adicionar suporte ao scroll do mouse
        def _on_mouse_wheel(event):
            tree.yview_scroll(-1 * (event.delta // 120), "units")

        tree.bind("<MouseWheel>", _on_mouse_wheel)

    # Limpar dados antigos antes de carregar os novos
    for i in tree.get_children():
        tree.delete(i)

    # Atualizar colunas da tabela
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    # Aplicar estilo
    style = ttk.Style()
    style.configure("Treeview", font=("Arial", 11), rowheight=25)
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=150)

    # Inserir dados, formatando números
    for _, row in df.iterrows():
        valores = [f"{valor:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".") if isinstance(valor, (int, float)) else valor for valor in row]
        tree.insert("", "end", values=valores)

def carregar_dados_selecionado():
    """ Obtém o ano selecionado pelo usuário e chama carregar_dados """
    ano = combobox_anos.get()
    if ano.isdigit():
        carregar_dados(int(ano))
    else:
        logging.error("Erro: Nenhum ano selecionado.")

def pesquisa_od_metro():
    """ Abre a janela principal para exibição dos dados da pesquisa OD. """
    logging.info("Abrindo Mapa da Pesquisa Origem e Destino")

    root = tk.Toplevel()
    monitor = get_monitors()[0]
    screen_width = monitor.width
    screen_height = monitor.height
    root.geometry(f"{screen_width}x{screen_height}")
    root.attributes("-fullscreen", True)
    root.overrideredirect(True)
    root.title("Pesquisa Origem e Destino - METRÔ-SP")

    # Criar e exibir tabela
    global tree, combobox_anos
    tree = ttk.Treeview(root)
    tree.pack(expand=True, fill="both")

    label = tk.Label(root, text="Selecione o ano dos dados:")
    label.pack(pady=10)

    # Combobox para selecionar o ano
    combobox_anos = ttk.Combobox(root, values=list(arquivos_od.keys()), state="readonly")
    combobox_anos.pack(pady=5)

    # Botão para carregar dados do ano selecionado
    btn_carregar = tk.Button(root, text="Carregar Dados", command=carregar_dados_selecionado, font=("Arial", 12))
    btn_carregar.pack(pady=10)

    root.bind("<Escape>", lambda e: root.destroy())

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    pesquisa_od_metro()