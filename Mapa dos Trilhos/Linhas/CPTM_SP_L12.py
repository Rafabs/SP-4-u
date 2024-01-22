import tkinter as tk  # Criação da Interface Gráfica
from tkinter import *
from PIL import Image, ImageTk  # Manipular imagens
from colorama import Fore, Back, Style, init
from datetime import datetime

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line12():
    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 12 - SAFIRA iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Criando a janela
    root = tk.Toplevel()
    root.title("Linha 12 - Safira")
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
    estacao_BAS = canvas.create_text(
        x1-5,  y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_TAT = canvas.create_text(
        x2-5,  y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_EGO = canvas.create_text(
        x3-5,  y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_USL = canvas.create_text(
        x4-5,  y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ERM = canvas.create_text(
        x5-5,  y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SMP = canvas.create_text(
        x6-5,  y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JHE = canvas.create_text(
        x7-5,  y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ITI = canvas.create_text(
        x8-5,  y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JRO = canvas.create_text(
        x9-5,  y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_EMF = canvas.create_text(
        x10-5, y10+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_IQC = canvas.create_text(
        x11-5, y11+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ARC = canvas.create_text(
        x12-5, y12+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CVN = canvas.create_text(
        x13-5, y13+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências
    # BRÁS
    linha3_vermelha_icon = canvas.create_text(
        x1-3, y1+40, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
    l3_icon = canvas.create_text(
        x1+6, y1+42, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha7_rubi_icon = canvas.create_text(
        x1-3, y1+60, text="●", font="Helvetica 32", anchor="w", fill=rubi)
    l7_icon = canvas.create_text(
        x1+6, y1+62, text="7", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha10_turquesa_icon = canvas.create_text(
        x1-3, y1+80, text="●", font="Helvetica 32", anchor="w", fill=turquesa)
    l10_icon = canvas.create_text(
        x1+3, y1+82, text="10", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha11_coral_icon = canvas.create_text(
        x1-3, y1+100, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x1+3, y1+102, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha13_jade_icon = canvas.create_text(
        x1-3, y1+120, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x1+3, y1+122, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # TATUAPÉ
    linha3_vermelha_icon = canvas.create_text(
        x2-3, y2+40, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
    l3_icon = canvas.create_text(
        x2+6, y2+42, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha11_coral_icon = canvas.create_text(
        x2-3, y2+60, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x2+3, y2+62, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)

    # ENGENHEIRO GOULART
    linha13_jade_icon = canvas.create_text(
        x3-3, y3+40, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x3+3, y3+42, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # CALMON VIANA
    linha11_coral_icon = canvas.create_text(
        x13-3, y13+40, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x13+3, y13+42, text="11", font="Helvetica 10 bold", anchor="w", fill=branco)

    # Desenha a linha conectando as estações
    linha = canvas.create_line(
        x1-10, y1+12, x13+25, y13+12, fill=safira, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_BAS)
    canvas.lift(estacao_TAT)
    canvas.lift(estacao_EGO)
    canvas.lift(estacao_USL)
    canvas.lift(estacao_ERM)
    canvas.lift(estacao_SMP)
    canvas.lift(estacao_JHE)
    canvas.lift(estacao_ITI)
    canvas.lift(estacao_JRO)
    canvas.lift(estacao_EMF)
    canvas.lift(estacao_IQC)
    canvas.lift(estacao_ARC)
    canvas.lift(estacao_CVN)
    canvas.lift(l3_icon)
    canvas.lift(l7_icon)
    canvas.lift(l10_icon)
    canvas.lift(l11_icon)
    canvas.lift(l13_icon)

    # Define as Estações
    nome_BAS = canvas.create_text(x1+8, y1-13, text="Brás",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_TAT = canvas.create_text(x2+8, y2-13, text="Tatuapé",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_EGO = canvas.create_text(x3+8, y3-13, text="Engenheiro Goulart",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_USL = canvas.create_text(x4+8, y4-13, text="USP Leste",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ERM = canvas.create_text(x5+8, y5-13, text="Ermelino Matarazzo",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SMP = canvas.create_text(x6+8, y6-13, text="São Miguel Paulista",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JHE = canvas.create_text(x7+8, y7-13, text="Jardim Helena - Vila Mara",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ITI = canvas.create_text(x8+8, y8-13, text="Itaim Paulista",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JRO = canvas.create_text(x9+8, y9-13, text="Jardim Romano",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_EMF = canvas.create_text(x10+8, y10-13, text="Engenheiro Manoel Feio",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_IQC = canvas.create_text(x11+8, y11-13, text="Itaquaquecetuba",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ARC = canvas.create_text(x12+8, y12-13, text="Aracaré",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CVN = canvas.create_text(x13+8, y13-13, text="Calmon Viana",
                                  font="Helvetica 12", anchor="w", angle=60)

    dev = canvas.create_text(
        960, 900, text="⚡Desenvolvido por RAFAEL BARBOSA - 10/03/2023 | Revisado em 02/09/2023", font="Helvetica 12", anchor="c")

    while True:
        root.update()
        try:
            root.update()
        except TclError:
            break