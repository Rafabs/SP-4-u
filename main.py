import requests  # Para baixar as imagens da internet
from io import BytesIO  # Para carregar as imagens diretamente da memória
import json
import sys  # Importa o módulo sys para acessar funcionalidades do sistema
sys.path.append(r'Mapa_dos_Trilhos') # Adiciona o diretório r'Mapa_dos_Trilhos' ao caminho de busca de módulos
sys.path.append(r'Mapa_dos_Trilhos\\Linhas') # Adiciona o diretório r'Mapa_dos_Trilhos\Linhas' ao caminho de busca de módulos
from colorama import Fore, Back, Style, init # Importa classes específicas do módulo colorama para colorir o terminal
import logging  # Importa o módulo logging para registrar mensagens de log
import tkinter as tk  # Importa o módulo tkinter para criar interfaces gráficas
from tkinter import ttk, Button, Frame, Tk # Importa classes específicas do módulo tkinter para criar interfaces gráficas
from datetime import datetime # Importa a classe datetime do módulo datetime para trabalhar com datas e horas
from PIL import Image, ImageTk # Importa classes específicas do módulo PIL para manipular imagens
import os  # Importa o módulo os para interagir com o sistema operacional
import platform  # Importa o módulo platform para obter informações sobre a plataforma
import tempfile  # Importa o módulo tempfile para trabalhar com arquivos temporários
import atexit  # Importa o módulo atexit para registrar funções a serem chamadas na saída do programa
import webbrowser  # Importa o módulo webbrowser para abrir URLs em um navegador
import re  # Importa o módulo re para realizar operações com expressões regulares
from Guararema import guararema  # Importa a função guararema do módulo Guararema
from Pirapora import pirapora  # Importa a função pirapora do módulo Pirapora
from SP_L17 import line17    # Importa a função line6 do módulo SP_L17
from SP_L15 import line15    # Importa a função line15 do módulo SP_L15
from SP_L13 import line13    # Importa a função line13 do módulo SP_L13
from SP_L12 import line12    # Importa a função line12 do módulo SP_L12
from SP_L11 import line11    # Importa a função line11 do módulo SP_L11
from SP_L10 import line10    # Importa a função line10 do módulo SP_L10
from SP_L09 import line9   # Importa a função line9 do módulo SP_L09
from SP_L08 import line8   # Importa a função line8 do módulo SP_L08
from SP_L07 import line7   # Importa a função line7 do módulo SP_L07
from SP_L06 import line6   # Importa a função line6 do módulo SP_L06
from SP_L05 import line5   # Importa a função line5 do módulo SP_L05
from SP_L04 import line4   # Importa a função line4 do módulo SP_L04
from SP_L03 import line3   # Importa a função line3 do módulo SP_L03
from SP_L02 import line2   # Importa a função line2 do módulo SP_L02
from SP_L01 import line1   # Importa a função line1 do módulo SP_L01
from noticia import notice_transp_sao_paulo # Importa a função notice_transp_sao_paulo do módulo noticia
from varredura import verificacao
from Pesquisa_pass.pesquisa_pass import passageiro_estacao
from Pesquisa_od.pesquisa_od import pesquisa_od_metro
from mapa import mapa_global  # Importa a função mapa_global do módulo mapa
from gtfs_emtu import emtu  # Importa a função emtu do módulo gtfs_emtu
from gtfs_sptrans import sptrans  # Importa a função sptrans do módulo gtfs_sptrans
from temperatura import get_weather # Importa a função get_weather do módulo temperatura
from Guias.guias import *  # Importa todas as funções do módulo guias
from pathlib import Path
import locale
import difflib
import csv
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

init() # Inicializa o colorama

def log_close_time():
    logging.info(f"{'=' * 30} PROGRAMA FECHADO {'=' * 30}")

# Registra a função para ser chamada na saída
atexit.register(log_close_time)

def dados_usuario():
    # Obtém a hora atual
    hora_atual = datetime.now().strftime("%d/%m/%Y | %H:%M:%S")

    print(f"=" * 30, "INFORMAÇÕES DO USUÁRIO", "=" * 30)
    print(hora_atual)

    # Obtém o nome do Sistema Operacional
    os_name = os.name
    print('<<<<<<Nome do Sistema Operacional>>>', os_name)

    # Informações sobre a Plataforma
    os_platform = platform.system()
    print('<<<Informações sobre a Plataforma>>>', os_platform)

    # Diretório Atual
    current_directory = os.getcwd()
    print('<<<Diretório Atual>>>', current_directory)

    # Usuário Atual
    current_user = os.getlogin()
    print('<<<Usuário Atual>>>', current_user)

    # Versão do Sistema Operacional (Não existe uma equivalência direta no Windows)
    os_version = platform.version()
    print('<<<Versão do Sistema Operacional>>>', os_version)

    # Informações sobre a Máquina
    machine_info = platform.machine()
    print('<<<Informações sobre a Máquina>>>', machine_info)

    # Arquitetura da Máquina (32 ou 64 bits)
    machine_architecture = platform.architecture()
    print('<<<Arquitetura da Máquina>>>', machine_architecture)

    # Versão do Python
    python_version = platform.python_version()
    print('<<<Versão do Python>>>', python_version)

    # Informações sobre a Distribuição do Python
    python_distribution = platform.version()
    print('<<<Distribuição do Python>>>', python_distribution)

    # Informações sobre o Processador
    processor_info = platform.processor()
    print('<<<Informações sobre o Processador>>>', processor_info)

    # Diretório Temporário
    temp_dir = tempfile.gettempdir()
    print('<<<Diretório Temporário>>>', temp_dir)

    # Diretórios Especiais (pasta do usuário, diretório inicial, etc.)
    user_home_directory = os.path.expanduser("~")
    print('<<<Diretório do Usuário>>>', user_home_directory)

    print("=" * 90)

# Configuração do logger
logging.basicConfig(filename=r'Mapa_dos_Trilhos\\log.txt', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

with open(r'Mapa_dos_Trilhos/Linhas/subtitle.json', 'r', encoding='utf-8') as file:
    lines_data = json.load(file)

# Redirecionamento de sys.stdout e sys.stderr para o logger
class StreamToLogger:
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            # Mapeia os níveis de log de saída do sys.stdout e sys.stderr para os níveis apropriados do logger
            if self.log_level == logging.WARNING:
                self.logger.warning(line.rstrip())
            elif self.log_level == logging.DEBUG:
                self.logger.debug(line.rstrip())
            elif self.log_level == logging.CRITICAL:
                self.logger.critical(line.rstrip())
            else:
                self.logger.info(line.rstrip())  # Por padrão, usa INFO

    def flush(self):
        pass

# Configuração de sys.stdout e sys.stderr
sys.stdout = StreamToLogger(logging.getLogger('STDOUT'), logging.INFO)
sys.stderr = StreamToLogger(logging.getLogger('STDERR'), logging.ERROR)

dados_usuario()

def abrir_link(url):
    # Remove qualquer fragmento indesejado da URL
    url = re.sub(r'/[^/]*$', '', url)

    # Abre o link em um navegador externo
    webbrowser.open_new(url)

def fazer_varredura():
    itens_arquivos = verificacao()

def exibir_noticias():
    noticias = notice_transp_sao_paulo()

    if noticias is not None:
        # Canvas específico para notícias
        canvas_noticias = tk.Canvas(
            root, bg="#333333", width=770, height=550, bd=0, highlightthickness=0)
        scroll = tk.Scrollbar(root, orient="vertical",
                              command=canvas_noticias.yview)
        frame_noticias = tk.Frame(canvas_noticias, bg="#333333")

        canvas_noticias.create_window(
            (0, 0), window=frame_noticias, anchor="nw")
        canvas_noticias.configure(yscrollcommand=scroll.set)

        canvas_noticias.place(x=10, y=150)
        scroll.place(x=780, y=150, height=550)

        frame_noticias.bind("<Configure>", lambda e: canvas_noticias.configure(
            scrollregion=canvas_noticias.bbox("all")))

        # Exibe as notícias no Frame
        for index, row in noticias.iterrows():
            title = row['title']
            link = row['link']
            image_url = row.get('image_url')  # Verifica se há URL da imagem

            # Baixa e redimensiona a imagem
            if image_url:
                try:
                    response = requests.get(image_url)
                    image_data = Image.open(BytesIO(response.content))
                    image_data = image_data.resize(
                        (100, 100), Image.ANTIALIAS)  # Redimensiona a imagem
                    img = ImageTk.PhotoImage(image_data)
                except Exception as e:
                    print(f"Erro ao carregar imagem: {e}")
                    img = None
            else:
                img = None

            # Cria um Frame para cada notícia
            noticia_frame = tk.Frame(
                frame_noticias, bg="#444444", padx=10, pady=5)
            noticia_frame.pack(fill="x", pady=5)

            # Adiciona a imagem, se disponível
            if img:
                label_image = tk.Label(noticia_frame, image=img, bg="#444444")
                # Referência para evitar que a imagem seja descartada pelo garbage collector
                label_image.image = img
                label_image.pack(side="left", padx=5)

            # Adiciona o título como um label clicável
            label_titulo = tk.Label(noticia_frame, text=title, fg="white", bg="#444444", font=(
                "Arial", 12), anchor="w", cursor="hand2", wraplength=750)
            label_titulo.pack(side="left", fill="x")
            label_titulo.bind("<Button-1>", lambda event,
                              url=link: abrir_link(url))

            # Linha de separação
            separator = tk.Frame(frame_noticias, height=1, bg="#555555")
            separator.pack(fill="x", pady=2)

    else:
        # Se não houver notícias, exibe uma mensagem indicando isso
        label_msg_noticias.config(text="Nenhuma notícia encontrada.",
                                  fg="red", bg="#333333", font=("Arial", 12), wraplength=900)

# Função para fechar a janela
def fechar_janela(event):
    root.destroy()

# Criando a janela
root = tk.Tk()
root.title("SAMPA 4U")
# Define uma largura e altura específicas para a janela
root.attributes("-fullscreen", True)

# Vincula a tecla ESC para fechar a janela
root.bind("<Escape>", fechar_janela)

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

# Imprime o texto formatado
print(f"{Style.BRIGHT}{Fore.WHITE}Programa Iniciado às {Fore.RED}{hora_atual}{Style.RESET_ALL}")

canvas = tk.Canvas(root, width=1920, height=1080)
canvas.pack()
canvas.configure(bg='#D3D3D3')

# Carrega a imagem usando o PIL
image = Image.open(r'Mapa_dos_Trilhos\\Favicon\\SP4U_LOGO.ico')
photo = ImageTk.PhotoImage(image)

# Define o ícone
root.iconphoto(False, photo)

# Carrega o logotipo do SP4U
logo = Image.open(r"Mapa_dos_Trilhos\\Imgs\\SP4U_LOGO.jpg")
# Redimensiona a imagem para ajustar ao tamanho do canvas
logo = logo.resize((70, 70))
logo_tk = ImageTk.PhotoImage(logo)
logo_label = ttk.Label(root, image=logo_tk)
logo_label.place(x=10, y=10)

# Código das cores de background
preto = "#000000"
branco = "#FFFFFF"
laranja = "#999999"
ouro = "#999999"

# Verifica se um caminho relativo existe a partir do diretório do script
def normalizar_nome(nome: str) -> str:
    return nome.lower().replace("_", "").replace(" ", "")

# Verifica se um caminho relativo existe a partir do diretório do script
def verificar_modulo(caminho_relativo: str) -> bool:
    base_dir = Path(__file__).resolve(
    ).parent if "__file__" in globals() else Path.cwd()
    raiz = base_dir / "Mapa_dos_Trilhos"

    if not raiz.exists():
        print(f"❌ Pasta 'Mapa_dos_Trilhos' não encontrada em {base_dir}")
        return False

    caminho_normalizado = normalizar_nome(caminho_relativo)
    extensoes_validas = {".zip", ".csv", ".json", ".xlsx",
                         ".xls", ".txt", ".png", ".jpg", ".pdf", ".parquet"}

    for item in raiz.rglob('*'):
        nome_item_normalizado = normalizar_nome(item.name)
        if caminho_normalizado in nome_item_normalizado and item.is_dir():
            arquivos = list(item.glob('*'))
            if arquivos:
                print(
                    f"✅ Diretório '{item}' existe e contém {len(arquivos)} arquivo(s).")
                return True
            else:
                print(f"⚠️ Diretório '{item}' encontrado, mas está vazio.")
                return False

    subdirs = [p for p in raiz.iterdir() if p.is_dir()]
    nomes_normalizados = {normalizar_nome(p.name): p for p in subdirs}

    # fuzzy match com tolerância
    correspondencias = difflib.get_close_matches(
        caminho_normalizado, nomes_normalizados.keys(), n=1, cutoff=0.6)

    if correspondencias:
        match = correspondencias[0]
        pasta = nomes_normalizados[match]

        arquivos_validos = [arq for arq in pasta.glob(
            "*") if arq.suffix.lower() in extensoes_validas]
        if arquivos_validos:
            print(
                f"✅ Diretório '{pasta}' contém arquivos válidos: {[a.name for a in arquivos_validos]}")
            return True
        else:
            print(
                f"⚠️ Diretório '{pasta}' encontrado, mas sem arquivos úteis.")
            return False

    print(
        f"❌ Erro: Nenhum caminho aproximado encontrado para '{caminho_relativo}'")
    return False

# Atualiza o status do indicador visualmente (verde/vermelho)
def atualizar_status(canva_modulo, modulo):
    try:
        cor = "green" if verificar_modulo(modulo) else "red"
    except Exception as e:
        cor = "red"
        print(f"Erro ao verificar o módulo '{modulo}': {e}")

    canva_modulo.delete("all")
    canva_modulo.create_oval(2, 2, 18, 18, fill=cor, outline=cor)
    canva_modulo.after(2000, atualizar_status, canva_modulo, modulo)

# Cria um botão com indicador de status opcional
def criar_botao(parent, text, command, bg, fg, hovercolor, width=None, modulo=None):
    container = tk.Frame(parent, bg=parent.cget(
        "bg") if "bg" in parent.keys() else "black")
    container.pack(side=tk.TOP, padx=5, pady=5, anchor="w", fill=tk.X)

    if modulo:
        print("🔍 DEBUG MODULO:", repr(modulo))
        canva_modulo = tk.Canvas(
            container, width=20, height=20, highlightthickness=0, bg=container["bg"])
        canva_modulo.pack(side=tk.LEFT, padx=5)
        atualizar_status(canva_modulo, modulo)

    button = Button(container, text=text, command=command,
                    bg=bg, fg=fg, width=width)
    button.pack(side=tk.LEFT, padx=5)

    button.bind("<Enter>", lambda e: button.config(bg=hovercolor))
    button.bind("<Leave>", lambda e: button.config(bg=bg))

# Frame Mapas
frame_mapas = ttk.LabelFrame(
    root, text="Mapas - Capital e RMSP", labelanchor='n', padding=2)
frame_mapas.place(relx=0.11, rely=0.01, anchor=tk.N)
criar_botao(frame_mapas, "Acessar Mapa", mapa_global, "black",
            "#C0C0C0", "#A9A9A9", width=20, modulo="mapa")

# Frame Sistemas
frame_sistemas = ttk.LabelFrame(
    root, text="Sistemas de Buscas de Linhas", labelanchor='n', padding=2)
frame_sistemas.place(relx=0.22, rely=0.01, anchor=tk.N)
criar_botao(frame_sistemas, "SPTRANS", sptrans, "black",
            "#FF2F2F", "#FF8080", width=20, modulo="gtfs_sptrans")
criar_botao(frame_sistemas, "EMTU", emtu, "black", "blue",
            "#5A79FF", width=20, modulo="gtfs_emtu")

# Frame Mapas da Rede
frame_mapa_guia = ttk.LabelFrame(
    root, text="Mapa da Rede - /Abr.25", labelanchor='n', padding=2)
frame_mapa_guia.place(relx=0.33, rely=0.01, anchor=tk.N)
criar_botao(frame_mapa_guia, "Mapa da Rede", mapa_rede, "black",
            "#00B352", "#5AFF7E", width=20, modulo="mapa")

# Frame Guia do Metrô
frame_guia_metro = ttk.LabelFrame(
    root, text="Guia de Usuário - METRÔ", labelanchor='n', padding=2)
frame_guia_metro.place(relx=0.44, rely=0.01, anchor=tk.N)
criar_botao(frame_guia_metro, "Guia do Usuário - PT/BR", guia_pt_metro,
            "black", "blue", "#0073E6", width=20, modulo="guias")
criar_botao(frame_guia_metro, "Guia do Usuário - EN/US", guia_en_metro,
            "black", "blue", "#0073E6", width=20, modulo="guias")

# Frame Guia CPTM
frame_guia_cptm = ttk.LabelFrame(
    root, text="Guia de Usuário - CPTM", labelanchor='n', padding=2)
frame_guia_cptm.place(relx=0.55, rely=0.01, anchor=tk.N)
criar_botao(frame_guia_cptm, "Guia do Usuário - CPTM", guia_cptm,
            "black", "#CA016B", "#E75480", width=20, modulo="guias")
criar_botao(frame_guia_cptm, "Guia do Expresso Turístico", guia_cptm_expresso_turistico,
            "black", "#CA016B", "#E75480", width=20, modulo="guias")

# Frame Pesquisas
frame_pesquisas_metro = ttk.LabelFrame(
    root, text="Pesquisas", labelanchor='n', padding=2)
frame_pesquisas_metro.place(relx=0.671, rely=0.01, anchor=tk.N)
criar_botao(frame_pesquisas_metro, "Pesquisa Origem e Destino", pesquisa_od_metro,
            "black", "#00c9c4", "#007875", width=26, modulo="pesquisa_od")
criar_botao(frame_pesquisas_metro, "Demanda por Estação", passageiro_estacao,
            "black", "#00c9c4", "#007875", width=26, modulo="pesquisa_pass")

# Notícias
noticia_ico = canvas.create_text(
    10, 140, text="Notícias:", font="Helvetica 10 bold", anchor="w", fill=preto)
label_msg_noticias = tk.Label(root, text="", anchor="se")
label_msg_noticias.place(x=10, y=500)

# Definindo os caminhos das imagens para cada linha
linha1_icon_path = r"Mapa_dos_Trilhos/Icons/1.png"
linha2_icon_path = r"Mapa_dos_Trilhos/Icons/2.png"
linha3_icon_path = r"Mapa_dos_Trilhos/Icons/3.png"
linha4_icon_path = r"Mapa_dos_Trilhos/Icons/4.png"
linha5_icon_path = r"Mapa_dos_Trilhos/Icons/5.png"
linha7_icon_path = r"Mapa_dos_Trilhos/Icons/7.png"
linha8_icon_path = r"Mapa_dos_Trilhos/Icons/8.png"
linha9_icon_path = r"Mapa_dos_Trilhos/Icons/9.png"
linha10_icon_path = r"Mapa_dos_Trilhos/Icons/10.png"
linha11_icon_path = r"Mapa_dos_Trilhos/Icons/11.png"
linha12_icon_path = r"Mapa_dos_Trilhos/Icons/12.png"
linha13_icon_path = r"Mapa_dos_Trilhos/Icons/13.png"
linha15_icon_path = r"Mapa_dos_Trilhos/Icons/15.png"

linha1_azul_icon_path = r"Mapa_dos_Trilhos/Icons/1_azul.png"
linha2_verde_icon_path = r"Mapa_dos_Trilhos/Icons/2_verde.png"
linha3_vermelha_icon_path = r"Mapa_dos_Trilhos/Icons/3_vermelha.png"
linha4_amarela_icon_path = r"Mapa_dos_Trilhos/Icons/4_amarela.png"
linha5_lilas_icon_path = r"Mapa_dos_Trilhos/Icons/5_lilas.png"
linha7_rubi_icon_path = r"Mapa_dos_Trilhos/Icons/cptm.png"
linha8_diamante_icon_path = r"Mapa_dos_Trilhos/Icons/8_diamante.png"
linha9_esmeralda_icon_path = r"Mapa_dos_Trilhos/Icons/9_esmeralda.png"
linha10_turquesa_icon_path = r"Mapa_dos_Trilhos/Icons/cptm.png"
linha11_coral_icon_path = r"Mapa_dos_Trilhos/Icons/cptm.png"
linha12_safira_icon_path = r"Mapa_dos_Trilhos/Icons/cptm.png"
linha13_jade_icon_path = r"Mapa_dos_Trilhos/Icons/cptm.png"
linha15_prata_icon_path = r"Mapa_dos_Trilhos/Icons/15_prata.png"

# Carregando as imagens apenas uma vez
linha1_icon = tk.PhotoImage(file=linha1_icon_path)
linha2_icon = tk.PhotoImage(file=linha2_icon_path)
linha3_icon = tk.PhotoImage(file=linha3_icon_path)
linha4_icon = tk.PhotoImage(file=linha4_icon_path)
linha5_icon = tk.PhotoImage(file=linha5_icon_path)
linha7_icon = tk.PhotoImage(file=linha7_icon_path)
linha8_icon = tk.PhotoImage(file=linha8_icon_path)
linha9_icon = tk.PhotoImage(file=linha9_icon_path)
linha10_icon = tk.PhotoImage(file=linha10_icon_path)
linha11_icon = tk.PhotoImage(file=linha11_icon_path)
linha12_icon = tk.PhotoImage(file=linha12_icon_path)
linha13_icon = tk.PhotoImage(file=linha13_icon_path)
linha15_icon = tk.PhotoImage(file=linha15_icon_path)

linha1_azul_icon = tk.PhotoImage(file=linha1_azul_icon_path)
linha2_verde_icon = tk.PhotoImage(file=linha2_verde_icon_path)
linha3_vermelha_icon = tk.PhotoImage(file=linha3_vermelha_icon_path)
linha4_amarela_icon = tk.PhotoImage(file=linha4_amarela_icon_path)
linha5_lilas_icon = tk.PhotoImage(file=linha5_lilas_icon_path)
linha7_rubi_icon = tk.PhotoImage(file=linha7_rubi_icon_path)
linha8_diamante_icon = tk.PhotoImage(file=linha8_diamante_icon_path)
linha9_esmeralda_icon = tk.PhotoImage(file=linha9_esmeralda_icon_path)
linha10_turquesa_icon = tk.PhotoImage(file=linha10_turquesa_icon_path)
linha11_coral_icon = tk.PhotoImage(file=linha11_coral_icon_path)
linha12_safira_icon = tk.PhotoImage(file=linha12_safira_icon_path)
linha13_jade_icon = tk.PhotoImage(file=linha13_jade_icon_path)
linha15_prata_icon = tk.PhotoImage(file=linha15_prata_icon_path)

def execute_line1_and_command():
    line1()  # Chama a função que executa o script SP_L01.py

def execute_line2_and_command():
    line2()  # Chama a função que executa o script SP_L02.py

def execute_line3_and_command():
    line3()  # Chama a função que executa o script SP_L03.py

def execute_line4_and_command():
    line4()  # Chama a função que executa o script SP_L04.py

def execute_line5_and_command():
    line5()  # Chama a função que executa o script SP_L05.py

def execute_line7_and_command():
    line7()  # Chama a função que executa o script SP_L07.py

def execute_line8_and_command():
    line8()  # Chama a função que executa o script SP_L08.py

def execute_line9_and_command():
    line9()  # Chama a função que executa o script SP_L09.py

def execute_line10_and_command():
    line10()  # Chama a função que executa o script SP_L10.py

def execute_line11_and_command():
    line11()  # Chama a função que executa o script SP_L11.py

def execute_line12_and_command():
    line12()  # Chama a função que executa o script SP_L12.py

def execute_line13_and_command():
    line13()  # Chama a função que executa o script SP_L13.py

def execute_line15_and_command():
    line15()  # Chama a função que executa o script SP_L15.py

def load_routes(filepath):
    routes = {}
    with open(filepath, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 4:
                continue
            line_name = row[0].replace('"', '').strip()
            station_str = row[3].replace('"', '').strip()

            # Divide todas as partes
            station_parts = [s.strip()
                             for s in station_str.split(' - ') if s.strip()]
            nparts = len(station_parts)

            # Balanceamento inteligente
            if nparts >= 2:
                mid = nparts // 2
                origin = " - ".join(station_parts[:mid])
                destination = " - ".join(station_parts[mid:])
            elif nparts == 1:
                origin = destination = station_parts[0]
            else:
                origin = destination = ""

            # Extrai chave (ex: L3 de METRÔ L3)
            if 'L' in line_name:
                key = 'L' + line_name.split('L')[-1]
            else:
                continue

            routes[key] = {
                "origin": origin,
                "destination": destination
            }

    return routes

# Substitua pelo caminho correto se estiver em outra pasta
routes = load_routes("Mapa_dos_Trilhos\\Gtfs_SPTRANS\\routes.txt")

# Carrega os dados do arquivo JSON
with open('Mapa_dos_Trilhos/Linhas/trajeto.json', 'r', encoding='utf-8') as file:
    trajetos = json.load(file)

# Variáveis para cor de fundo das linhas, código de linha extraído de trajeto.json e SP_LXX.py
cor_linha_01 = trajetos["SP_L01.py"]["COR_LINHA"]
cor_linha_02 = trajetos["SP_L02.py"]["COR_LINHA"]
cor_linha_03 = trajetos["SP_L03.py"]["COR_LINHA"]
cor_linha_04 = trajetos["SP_L04.py"]["COR_LINHA"]
cor_linha_05 = trajetos["SP_L05.py"]["COR_LINHA"]
cor_linha_07 = trajetos["SP_L07.py"]["COR_LINHA"]
cor_linha_08 = trajetos["SP_L08.py"]["COR_LINHA"]
cor_linha_09 = trajetos["SP_L09.py"]["COR_LINHA"]
cor_linha_10 = trajetos["SP_L10.py"]["COR_LINHA"]
cor_linha_11 = trajetos["SP_L11.py"]["COR_LINHA"]
cor_linha_12 = trajetos["SP_L12.py"]["COR_LINHA"]
cor_linha_13 = trajetos["SP_L13.py"]["COR_LINHA"]
cor_linha_15 = trajetos["SP_L15.py"]["COR_LINHA"]

# Botão para abrir o mapa da malha ferroviária e de corredores de ônibus
button_l1 = tk.Button(root, text="Azul", command=execute_line1_and_command,
                      fg="white", bg=cor_linha_01, width=15)
button_l1.place(x=1650, y=5)
canvas.create_image(1630, 18, image=linha1_icon)
canvas.create_image(1600, 18, image=linha1_azul_icon)
operadora_l1 = canvas.create_text(
    1580, 18, text="METRÔ", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L1", {})
tp_l1 = canvas.create_text(1910, 13, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l1 = canvas.create_text(1910, 23, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 30, 1920, 30, width=1)

button_l2 = tk.Button(root, text="Verde", command=execute_line2_and_command,
                      bg=cor_linha_02, fg="white", width=15)
button_l2.place(x=1650, y=32)
canvas.create_image(1630, 45, image=linha2_icon)
canvas.create_image(1600, 45, image=linha2_verde_icon)
operadora_l2 = canvas.create_text(
    1580, 45, text="METRÔ", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L2", {})
tp_l2 = canvas.create_text(1910, 40, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l2 = canvas.create_text(1910, 50, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 57, 1920, 57, width=1)

button_l3 = tk.Button(root, text="Vermelha", command=execute_line3_and_command,
                      bg=cor_linha_03, fg="black", width=15)
button_l3.place(x=1650, y=59)
canvas.create_image(1630, 72, image=linha3_icon)
canvas.create_image(1600, 72, image=linha3_vermelha_icon)
operadora_l3 = canvas.create_text(
    1580, 72, text="METRÔ", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L3", {})
tp_l3 = canvas.create_text(1910, 67, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l3 = canvas.create_text(1910, 77, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 84, 1920, 84, width=1)

button_l4 = tk.Button(root, text="Amarela", command=execute_line4_and_command,
                      bg=cor_linha_04, fg="black", width=15)
button_l4.place(x=1650, y=86)
canvas.create_image(1630, 99, image=linha4_icon)
canvas.create_image(1600, 99, image=linha4_amarela_icon)
operadora_l4 = canvas.create_text(
    1580, 99, text="VIAQUATRO", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L4", {})
tp_l4 = canvas.create_text(1910, 94, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l4 = canvas.create_text(1910, 104, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 111, 1920, 111, width=1)

button_l5 = tk.Button(root, text="Lilás", command=execute_line5_and_command,
                      bg=cor_linha_05, fg="white", width=15)
button_l5.place(x=1650, y=113)
canvas.create_image(1630, 126, image=linha5_icon)
canvas.create_image(1600, 126, image=linha5_lilas_icon)
operadora_l5 = canvas.create_text(
    1580, 126, text="VIAMOBILIDADE", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L5", {})
tp_l5 = canvas.create_text(1910, 121, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l5 = canvas.create_text(1910, 131, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 138, 1920, 138, width=1)

button_l6 = tk.Button(root, text="Laranja", command=line6,
                      bg=laranja, fg="white", width=15)
button_l6.place(x=1650, y=140)
route = routes.get("L6", {})
tp_l6 = canvas.create_text(1910, 148, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l6 = canvas.create_text(1910, 158, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 165, 1920, 165, width=1)

button_l7 = tk.Button(root, text="Rubi", command=execute_line7_and_command,
                      bg=cor_linha_07, fg="white", width=15)
button_l7.place(x=1650, y=167)
canvas.create_image(1630, 180, image=linha7_icon)
canvas.create_image(1600, 180, image=linha7_rubi_icon)
operadora_l7 = canvas.create_text(
    1580, 180, text="CPTM", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L07", {})
tp_l7 = canvas.create_text(1910, 175, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l7 = canvas.create_text(1910, 185, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 192, 1920, 192, width=1)

button_l8 = tk.Button(root, text="Diamante", command=execute_line8_and_command,
                      bg=cor_linha_08, fg="black", width=15)
button_l8.place(x=1650, y=194)
canvas.create_image(1630, 207, image=linha8_icon)
canvas.create_image(1600, 207, image=linha8_diamante_icon)
operadora_l8 = canvas.create_text(
    1580, 207, text="VIAMOBILIDADE", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L08", {})
tp_l8 = canvas.create_text(1910, 202, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l8 = canvas.create_text(1910, 212, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 219, 1920, 219, width=1)

button_l9 = tk.Button(root, text="Esmeralda",
                      command=execute_line9_and_command, bg=cor_linha_09, fg="black", width=15)
button_l9.place(x=1650, y=221)
canvas.create_image(1630, 234, image=linha9_icon)
canvas.create_image(1600, 234, image=linha9_esmeralda_icon)
operadora_l9 = canvas.create_text(
    1580, 234, text="VIAMOBILIDADE", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L09", {})
tp_l9 = canvas.create_text(1910, 229, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l9 = canvas.create_text(1910, 239, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 246, 1920, 246, width=1)

button_l10 = tk.Button(root, text="Turquesa",
                       command=execute_line10_and_command, bg=cor_linha_10, fg="black", width=15)
button_l10.place(x=1650, y=248)
canvas.create_image(1630, 261, image=linha10_icon)
canvas.create_image(1600, 261, image=linha10_turquesa_icon)
operadora_l10 = canvas.create_text(
    1580, 261, text="CPTM", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L10", {})
tp_l10 = canvas.create_text(1910, 256, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l10 = canvas.create_text(1910, 266, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 273, 1920, 273, width=1)

button_l11 = tk.Button(root, text="Coral", command=execute_line11_and_command,
                       bg=cor_linha_11, fg="black", width=15)
button_l11.place(x=1650, y=275)
canvas.create_image(1630, 288, image=linha11_icon)
canvas.create_image(1600, 288, image=linha11_coral_icon)
operadora_l11 = canvas.create_text(
    1580, 288, text="CPTM", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L11", {})
tp_l11 = canvas.create_text(1910, 283, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l11 = canvas.create_text(1910, 293, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 300, 1920, 300, width=1)

button_l12 = tk.Button(root, text="Safira",
                       command=execute_line12_and_command, bg=cor_linha_12, fg="white", width=15)
button_l12.place(x=1650, y=302)
canvas.create_image(1630, 315, image=linha12_icon)
canvas.create_image(1600, 315, image=linha12_safira_icon)
operadora_l12 = canvas.create_text(
    1580, 315, text="CPTM", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L12", {})
tp_l12 = canvas.create_text(1910, 310, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l12 = canvas.create_text(1910, 320, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 327, 1920, 327, width=1)

button_l13 = tk.Button(root, text="Jade", command=execute_line13_and_command,
                       bg=cor_linha_13, fg="black", width=15)
button_l13.place(x=1650, y=329)
canvas.create_image(1630, 342, image=linha13_icon)
canvas.create_image(1600, 342, image=linha13_jade_icon)
operadora_l13 = canvas.create_text(
    1580, 342, text="CPTM", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L13", {})
tp_l13 = canvas.create_text(1910, 337, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l13 = canvas.create_text(1910, 347, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 354, 1920, 354, width=1)

button_l15 = tk.Button(root, text="Prata", command=execute_line15_and_command,
                       bg=cor_linha_15, fg="black", width=15)
button_l15.place(x=1650, y=356)
canvas.create_image(1630, 369, image=linha15_icon)
canvas.create_image(1600, 369, image=linha15_prata_icon)
operadora_l15 = canvas.create_text(
    1580, 369, text="METRÔ", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L15", {})
tp_l15 = canvas.create_text(1910, 364, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l15 = canvas.create_text(1910, 374, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 381, 1920, 381, width=1)

button_l17 = tk.Button(root, text="Ouro", command=line17,
                       bg=ouro, fg="white", width=15)
button_l17.place(x=1650, y=383)
operadora_l8 = canvas.create_text(
    1580, 396, text="VIAMOBILIDADE", font="Helvetica 14", anchor="e", fill='#000000')
route = routes.get("L17", {})
tp_l17 = canvas.create_text(1910, 391, text=route.get(
    "origin", ""), font="Helvetica 8", anchor="e", fill='#000000')
ts_l17 = canvas.create_text(1910, 401, text=route.get(
    "destination", ""), font="Helvetica 8", anchor="e", fill='#000000')
canvas.create_line(1425, 408, 1920, 408, width=1)

button_guararema = tk.Button(
    root, text="Guararema", command=guararema, bg="#f8e71c", fg="black", width=15)
button_guararema.place(x=1650, y=410)

button_pirapora = tk.Button(
    root, text="Pirapora", command=pirapora, bg="#7ed321", fg="black", width=15)
button_pirapora.place(x=1650, y=437)

images = []  # Lista para armazenar as referências de imagem

# Função para carregar imagens
def load_image(image_path, x, y, width, height, canvas, images):
    if os.path.exists(image_path):
        img = Image.open(image_path)
        # Redimensiona a imagem
        img = img.resize((width, height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        images.append(photo)  # Armazena a referência da imagem na lista
        # Adiciona a imagem ao canvas
        canvas.create_image(x, y, image=photo, anchor="center")
    else:
        print(f"Imagem não encontrada: {image_path}")

for line in lines_data["lines"]:
    if isinstance(line, list):  # Verifica se o item é uma lista
        for sub_item in line:  # Percorre cada sub-item da lista
            if sub_item.get("type") == "oval":  # Verifica se o tipo é oval
                canvas.create_oval(
                    sub_item["position"]["x1"], sub_item["position"]["y1"],
                    sub_item["position"]["x2"], sub_item["position"]["y2"],
                    fill=sub_item["fill"], outline=sub_item["outline"]
                )
            elif sub_item.get("type") == "text":  # Verifica se o tipo é texto
                canvas.create_text(
                    sub_item["position"]["x"], sub_item["position"]["y"],
                    text=sub_item["text"], font=sub_item["font"],
                    anchor=sub_item["anchor"], fill=sub_item["color"]
                )
            else:
                print(f"Tipo inesperado: {sub_item}")

    elif "line" in line:
        # Processamento para linhas de separação
        canvas.create_line(
            line["line"]["x1"], line["line"]["y1"],
            line["line"]["x2"], line["line"]["y2"],
            fill=line["line"]["color"], width=line["line"]["width"]
        )

    elif "texts" in line:
        # Processamento de textos
        for text in line["texts"]:
            canvas.create_text(
                text["position"]["x"], text["position"]["y"],
                text=text["text"], font=text["font"],
                anchor=text["anchor"], fill=text["color"]
            )

    elif "icon" in line:
        # Processamento de imagens
        load_image(
            line["icon"], line["coordinates"]["x"], line["coordinates"]["y"],
            line["size"]["width"], line["size"]["height"], canvas, images
        )

    else:
        print(f"Item inesperado: {line}")

# Exibir as notícias automaticamente ao abrir a janela
exibir_noticias()

# Exibir os itens de arquivos disponíveis ao abrir a janela
fazer_varredura()

# Adiciona fundo estilizado para as informações
fundo_info = canvas.create_rectangle(
    1780, 685, 1920, 735, fill="#333333", outline="#222222", width=2)

# Guardar os IDs dos elementos criados para poder atualizá-los depois
id_hora_data = canvas.create_text(
    1910, 720, text=datetime.now().strftime("%d/%m/%Y %H:%M"),
    font="Helvetica 12 bold",
    anchor="e",
    fill='#ffffff'
)

id_temperatura = canvas.create_text(
    1910, 700, text=get_weather(),
    font="Helvetica 14 bold",
    anchor="e",
    fill='#00ff00'
)

def atualizar_temperatura():
    temperatura_atual = get_weather()
    canvas.itemconfigure(id_temperatura, text=temperatura_atual)
    root.after(60000, atualizar_temperatura)  # Atualiza a cada 1 minuto

def atualizar_data_hora():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    canvas.itemconfigure(id_hora_data, text=agora)
    root.after(1000, atualizar_data_hora)  # Atualiza a cada segundo

# Inicializa as atualizações periódicas
root.after(1000, atualizar_temperatura)
root.after(1000, atualizar_data_hora)

# Mantém o loop principal da interface
root.mainloop()