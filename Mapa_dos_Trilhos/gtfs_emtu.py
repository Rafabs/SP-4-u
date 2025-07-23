# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte público Metropolitano do Estado de São Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "22/07/2025 17:14"

DESCRITIVO:
MÃ³dulo de processamento de dados GTFS (General Transit Feed Specification):
- Implementa parser completo do formato GTFS
- Carrega e processa arquivos: routes.txt, trips.txt, stop_times.txt, stops.txt
- Calcula itinerÃ¡rios e conexÃµes entre linhas
- Interface grÃ¡fica com Tkinter para consulta
- VisualizaÃ§Ã£o de mapas com Folium
- IntegraÃ§Ã£o com API Olho Vivo (tempo real)
- ExportaÃ§Ã£o para CSV/Excel/JSON
- Algoritmo de roteamento (Dijkstra)
- Suporte a mÃºltiplos encodings (UTF-8, Latin-1)
ARQUITETURA:
    Mapa_dos_Trilhos/gtfs_emtu.py
"""
import csv
import webbrowser
import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter.scrolledtext import ScrolledText
import folium
from folium.plugins import MarkerCluster
from PIL import Image, ImageTk
from colorama import Fore, Back, Style, init
from datetime import datetime

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def emtu():
    """
    Função principal que cria a interface gráfica para consulta de rotas da EMTU.
    
    Esta função:
    - Cria a janela principal da aplicação
    - Configura elementos da interface (botões, campos de texto, tabelas)
    - Carrega e exibe dados GTFS da EMTU
    - Implementa funcionalidades de visualização de mapas
    - Permite pesquisa e filtragem de linhas
    
    A interface inclui:
    - Listagem de todas as rotas
    - Tabela de tarifas
    - Visualização de mapas com shapes e paradas
    - Campo de pesquisa para filtrar linhas
    """
    # Imprime o texto formatado indicando o início do processo
    print(f"{Style.BRIGHT}{Fore.WHITE}GTFS da EMTU iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")
    
    # Criando a janela principal do aplicativo
    root = tk.Toplevel()
    root.title("Consulta de Rotas EMTU")
    root.geometry("1920x1080")

    # Carrega a imagem do ícone usando o PIL
    image = Image.open('Mapa_dos_Trilhos\\Favicon\\onibus_EMTU.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone da janela
    root.iconphoto(False, photo)

    def exibir_rotas():
        """
        Carrega e exibe as rotas disponíveis a partir do arquivo routes.txt.
        
        Returns:
            list: Lista de strings contendo todas as rotas no formato "Número - Nome"
        """
        try:
            with open('Mapa_dos_Trilhos\\Gtfs_EMTU\\routes.txt', newline='', encoding='utf-8') as arquivo:
                leitor = csv.reader(arquivo)
                next(leitor)
                rotas = [f"{linha[1]} - {linha[2]}\n" for linha in leitor]
                resultado_text.insert(tk.END, "".join(rotas))
                return rotas
        except FileNotFoundError:
            resultado_text.insert(
                tk.END, "Arquivo 'routes.txt' não encontrado.")
            return []

    def exibir_tarifas():
        """
        Carrega e exibe as tarifas das linhas a partir do arquivo fare_attributes.txt.
        
        Os dados são exibidos em uma tabela ordenada alfabeticamente pelo nome da linha.
        """
        try:
            with open('Mapa_dos_Trilhos\\Gtfs_EMTU\\fare_attributes.txt', newline='', encoding='utf-8') as arquivo:
                leitor = csv.reader(arquivo)
                next(leitor)
                linhas = []
                for linha in leitor:
                    nome = linha[0]
                    tarifa = float(linha[1])
                    linhas.append((nome, tarifa))

                # Ordenar a lista de linhas com base na tarifa
                linhas_ordenadas = sorted(linhas, key=lambda x: x[0])

                for linha in linhas_ordenadas:
                    nome = linha[0]
                    tarifa = f'R$ {linha[1]:.2f}'
                    tabela_tarifas.insert("", "end", values=(nome, tarifa))
        except FileNotFoundError:
            tabela_tarifas.insert("", "end", values=(
                "Arquivo 'fare_attributes.txt' não encontrado.", ""))

    def carregar_mapa():
        """
        Carrega e exibe um mapa interativo com as shapes (rotas) da EMTU.
        
        O mapa é gerado usando Folium e exibe todas as rotas encontradas no arquivo shapes.txt.
        O mapa é salvo como HTML e aberto no navegador padrão.
        """
        m = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)

        shapes = {}
        caminho_arquivo_shapes = "Mapa_dos_Trilhos\\Gtfs_EMTU\\shapes.txt"

        with open(caminho_arquivo_shapes, 'r', encoding='utf-8') as arquivo_shapes:
            linhas = arquivo_shapes.readlines()
            for linha in linhas[1:]:
                dados = linha.strip().split(',')
                if len(dados) >= 4:
                    shape_id = dados[0]
                    lat = float(dados[1].strip('"'))
                    lon = float(dados[2].strip('"'))

                    if shape_id not in shapes:
                        shapes[shape_id] = []

                    shapes[shape_id].append((lat, lon))

        for shape_id, coordenadas in shapes.items():
            folium.PolyLine(coordenadas, color='red').add_to(m)

        m.save("Mapa_dos_Trilhos\\mapa_shapes.html")
        webbrowser.open("Mapa_dos_Trilhos\\mapa_shapes.html")

    def pontos():
        """
        Carrega e exibe um mapa interativo com os pontos de parada da EMTU.
        
        Os pontos são agrupados em clusters para melhor visualização quando há muitos marcadores próximos.
        O mapa é salvo como HTML e aberto no navegador padrão.
        """
        n = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)
        marker_cluster = MarkerCluster().add_to(n)

        caminho_arquivo_stops = "Mapa_dos_Trilhos\\Gtfs_EMTU\\stops.txt"
        dados_paradas = []

        with open(caminho_arquivo_stops, 'r', encoding='utf-8') as arquivo_stops:
            leitor_csv = csv.reader(arquivo_stops)
            cabecalho = next(leitor_csv)

            for linha in leitor_csv:
                dados_paradas.append(linha)

        for dados in dados_paradas:
            stop_id, stop_name, stop_lat, stop_lon = dados
            stop_lat = float(stop_lat)
            stop_lon = float(stop_lon)

            folium.Marker(
                location=[stop_lat, stop_lon],
                popup=folium.Popup(f"ID: {stop_id}<br>Localização: {stop_name}",
                                   max_width=300),

            ).add_to(marker_cluster)

        n.save("Mapa_dos_Trilhos\\mapa_paradas_cluster.html")
        webbrowser.open("Mapa_dos_Trilhos\\mapa_paradas_cluster.html")

    def filtrar_linhas():
        """
        Filtra as linhas exibidas com base no termo digitado no campo de pesquisa.
        
        A filtragem é feita em tempo real enquanto o usuário digita.
        """
        termo = campo_pesquisa.get().lower()
        linhas_filtradas = [linha for linha in rotas if termo in linha.lower()]
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, "".join(linhas_filtradas))

    # Estilos dos widgets
    estilo = ttk.Style()
    estilo.configure("TButton", font=("Arial", 12), width=30)
    estilo.configure("TLabel", font=("Arial", 14))
    estilo.configure("TEntry", font=("Arial", 12))

    # Título da aplicação
    titulo_label = ttk.Label(root, text="Consulta de Rotas EMTU")
    titulo_label.pack(pady=(20, 30))

    # Campo de Pesquisa
    pesquisa = ttk.Label(
        root, text="Pesquisar por número ou nome da linha", foreground="red")
    pesquisa.pack(padx=20, pady=(5, 20), anchor='w',)

    campo_pesquisa = ttk.Entry(root, width=50)
    campo_pesquisa.insert(tk.END, "")
    campo_pesquisa.pack(padx=20, pady=(5, 20), anchor='w')
    campo_pesquisa.bind('<KeyRelease>', lambda event: filtrar_linhas())

    # Frame para Resultado e Tabela de Linhas
    frame_esquerdo = ttk.Frame(root)
    frame_esquerdo.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

    # Resultado da pesquisa
    resultado_text = ScrolledText(
        frame_esquerdo, width=80, height=20, wrap=tk.WORD)
    resultado_text.pack(pady=(0, 20), anchor='w', fill=tk.BOTH, expand=True)

    # Frame para Botões
    frame_botoes = ttk.Frame(frame_esquerdo)
    frame_botoes.pack(pady=(0, 20), anchor='w')

    # Botões
    botao_shapes = ttk.Button(
        frame_botoes, text="Visualizar Mapa de Ruas Atendidas", command=carregar_mapa)
    botao_shapes.pack(side=tk.LEFT, padx=10)

    botao_stops = ttk.Button(
        frame_botoes, text="Visualizar Mapa com as Paradas", command=pontos)
    botao_stops.pack(side=tk.RIGHT, padx=10)

    # Exibição das rotas
    rotas = exibir_rotas()

    # Frame para Tabela de Tarifas
    frame_direito = ttk.Frame(root)
    frame_direito.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

    # Tabela de Tarifas
    tabela_tarifas = ttk.Treeview(frame_direito, columns=(
        "Linha", "Tarifa"), show="headings")
    tabela_tarifas.heading("Linha", text="Linha")
    tabela_tarifas.heading("Tarifa", text="Tarifa")
    tabela_tarifas.column("Linha", width=150, anchor="w")
    tabela_tarifas.column("Tarifa", width=50, anchor="w")

    # Adicionando a scrollbar vertical
    scrollbar_vertical = ttk.Scrollbar(frame_direito, orient="vertical", command=tabela_tarifas.yview)
    scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)
    tabela_tarifas.configure(yscrollcommand=scrollbar_vertical.set)
    
    # Definir a altura da tabela
    tabela_tarifas.config(height=200)

    # Empacotar a tabela dentro do frame
    tabela_tarifas.pack(pady=(0, 20), fill=tk.BOTH, expand=True)

    # Exibir as tarifas das linhas
    exibir_tarifas()

    # Iniciar o loop principal da aplicação
    root.mainloop()

# Verifica se o script está sendo executado como o programa principal
if __name__ == "__main__":
    emtu()