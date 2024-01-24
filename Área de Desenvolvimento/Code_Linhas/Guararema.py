import tkinter as tk  # Criação da Interface Gráfica
from tkinter import *
from PIL import Image, ImageTk  # Manipular imagens
from colorama import Fore, Back, Style, init
from datetime import datetime

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def guararema():
    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA GUARAREMA iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Criando a janela
    root = tk.Toplevel()
    root.title("Trem de Guararema (ABPF)")
    # Define uma largura e altura específicas para a janela
    root.geometry("1920x1080")

    canvas = tk.Canvas(root, width=1920, height=1080)
    canvas.pack()

    # Carrega a imagem usando o PIL
    image = Image.open('Mapa dos Trilhos\\Favicon\\ABPF_LOGO.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone
    root.iconphoto(False, photo)

    # Carrega o logotipo do Metrô
    metro_logo = Image.open("Mapa dos Trilhos\\Imgs\\ABPF_LOGO.jpg")
    # Redimensiona a imagem para ajustar ao tamanho do canvas
    metro_logo = metro_logo.resize((120, 50))
    metro_logo_tk = ImageTk.PhotoImage(metro_logo)

    # Insere a imagem do logotipo do Metrô no canvas na posiçao x,y
    canvas.create_image(0, 0, anchor="nw", image=metro_logo_tk)

    # Código das cores do mapa (em ordem numérica)
    azul = "#0455A1"
    verde = "#007E5E"
    vermelha = "#EE372F"
    amarela = "#FFF000"
    lilás = "#9B3894"
    rubi = "#CA016B"
    diamante = "#97A098"
    esmeralda = "#01A9A7"
    turquesa = "#049FC3"
    coral = "#F68368"
    safira = "#133C8D"
    jade = "#00B352"
    prata = "#C0C0C0"

    # Código das cores de background
    preto = "#000000"
    branco = "#FFFFFF"

    # Define as coordenadas para cada estação
    x1, y1 = 960, 750
    x2, y2 = 1010, 750

    # Desenha as estações
    estacao_GUARAREMA = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_LUIS_CARLOS = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Desenha a linha conectando as estações
    linha = canvas.create_line(
        x1-10, y1+12, x2+25, y2+12, fill='#f8e71c', width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_GUARAREMA)
    canvas.lift(estacao_LUIS_CARLOS)

    # Define as Estações
    nome_GUARAREMA = canvas.create_text(x1+8, y1-13, text="Guararema",
                                        font="Helvetica 12", anchor="w", angle=60)
    nome_LUIS_CARLOS = canvas.create_text(x2+8, y2-13, text="Luis Carlos",
                                          font="Helvetica 12", anchor="w", angle=60)

    dev = canvas.create_text(
        960, 900, text="⚡Desenvolvido por RAFAEL BARBOSA - 15/09/2023 | Revisado em 15/09/2023", font="Helvetica 12", anchor="c")

    while True:
        root.update()
        try:
            root.update()
        except TclError:
            break