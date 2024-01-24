import tkinter as tk  # Criação da Interface Gráfica
from tkinter import *
from PIL import Image, ImageTk  # Manipular imagens
from colorama import Fore, Back, Style, init
from datetime import datetime

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line10():
    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 10 - TURQUESA iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Criando a janela
    root = tk.Toplevel()
    root.title("Linha 10 - Turquesa")
    # Define uma largura e altura específicas para a janela
    root.geometry("1920x1080")

    canvas = tk.Canvas(root, width=1920, height=1080)
    canvas.pack()

    # Carrega a imagem usando o PIL
    image = Image.open('Mapa dos Trilhos\\Favicon\\cptm.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone
    root.iconphoto(False, photo)

    # Carrega o logotipo do Metrô
    metro_logo = Image.open("Mapa dos Trilhos\\Imgs\\CPTM_LOGO.jpg")
    # Redimensiona a imagem para ajustar ao tamanho do canvas
    metro_logo = metro_logo.resize((130, 50))
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
    x1, y1 = 660, 750
    x2, y2 = 710, 750
    x3, y3 = 760, 750
    x4, y4 = 810, 750
    x5, y5 = 860, 750
    x6, y6 = 910, 750
    x7, y7 = 960, 750
    x8, y8 = 1010, 750
    x9, y9 = 1060, 750
    x10, y10 = 1110, 750
    x11, y11 = 1160, 750
    x12, y12 = 1210, 750
    x13, y13 = 1260, 750

    # Desenha as estações
    estacao_RGS = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_RPI = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_GPT = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_MAU = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CPV = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SAN = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PSA = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_UTG = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SCS = canvas.create_text(
        x9-5, y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_TMD = canvas.create_text(
        x10-5, y10+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_IPG = canvas.create_text(
        x11-5, y11+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_MOC = canvas.create_text(
        x12-5, y12+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BAS = canvas.create_text(
        x13-5, y13+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências

    # BRÁS
    linha3_vermelha_icon = canvas.create_text(
        x13-3, y13+40, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
    l3_icon = canvas.create_text(
        x13+6, y13+42, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha11_coral_icon = canvas.create_text(
        x13-3, y13+60, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x13+3, y13+62, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha12_safira_icon = canvas.create_text(
        x13-3, y13+80, text="●", font="Helvetica 32", anchor="w", fill=safira)
    l12_icon = canvas.create_text(
        x13+3, y13+82, text="12", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha13_jade_icon = canvas.create_text(
        x13-3, y13+100, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x13+3, y13+102, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # TAMANDUATEÍ
    linha2_verde_icon = canvas.create_text(
        x10-3, y10+40, text="●", font="Helvetica 32", anchor="w", fill=verde)
    l2_icon = canvas.create_text(
        x10+6, y10+42, text="2", font="Helvetica 10 bold", anchor="w", fill=branco)

    # Desenha a linha conectando as estações
    linha = canvas.create_line(
        x1-10, y1+12, x13+25, y13+12, fill=turquesa, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_RGS)
    canvas.lift(estacao_RPI)
    canvas.lift(estacao_GPT)
    canvas.lift(estacao_MAU)
    canvas.lift(estacao_CPV)
    canvas.lift(estacao_SAN)
    canvas.lift(estacao_PSA)
    canvas.lift(estacao_UTG)
    canvas.lift(estacao_SCS)
    canvas.lift(estacao_TMD)
    canvas.lift(estacao_IPG)
    canvas.lift(estacao_MOC)
    canvas.lift(estacao_BAS)
    canvas.lift(l2_icon)
    canvas.lift(l3_icon)
    canvas.lift(l11_icon)
    canvas.lift(l12_icon)
    canvas.lift(l13_icon)

    # Define as Estações
    nome_RGS = canvas.create_text(x1+8, y1-13, text="Rio Grande da Serra",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_RPI = canvas.create_text(x2+8, y2-13, text="Ribeirão Pires",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_GPT = canvas.create_text(x3+8, y3-13, text="Guapituba",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_MAU = canvas.create_text(x4+8, y4-13, text="Mauá",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CPV = canvas.create_text(x5+8, y5-13, text="Capuava",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SAN = canvas.create_text(x6+8, y6-13, text="Prefeito Celso Daniel - Santo André",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PSA = canvas.create_text(x7+8, y7-13, text="Prefeito Saladino",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_UTG = canvas.create_text(x8+8, y8-13, text="Utinga",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SCS = canvas.create_text(x9+8, y9-13,  text="São Caetano do Sul - Prefeito Walter Braido",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_TMD = canvas.create_text(x10+8, y10-13, text="Tamanduateí",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_IPG = canvas.create_text(x11+8, y11-13, text="Ipiranga",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_MOC = canvas.create_text(x12+8, y12-13, text="Juventus - Mooca",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BAS = canvas.create_text(x13+8, y13-13, text="Brás",
                                  font="Helvetica 12", anchor="w", angle=60)

    dev = canvas.create_text(
        960, 900, text="⚡Desenvolvido por RAFAEL BARBOSA - 10/03/2023 | Revisado em 02/09/2023", font="Helvetica 12", anchor="c")

    while True:
        root.update()
        try:
            root.update()
        except TclError:
            break