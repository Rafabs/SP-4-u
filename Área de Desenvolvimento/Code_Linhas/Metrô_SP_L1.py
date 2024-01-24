import tkinter as tk  # Criação da Interface Gráfica
from tkinter import *
from PIL import Image, ImageTk  # Manipular imagens
from colorama import Fore, Back, Style, init
from datetime import datetime

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line1():
    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 1 - AZUL iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Criando a janela
    root = tk.Toplevel()
    root.title("Linha 1 - Azul")
    # Define uma largura e altura específicas para a janela
    root.geometry("1920x1080")

    canvas = tk.Canvas(root, width=1920, height=1080)
    canvas.pack()

    # Carrega a imagem usando o PIL
    image = Image.open('Mapa dos Trilhos\\Favicon\\1_azul.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone
    root.iconphoto(False, photo)

    # Carrega o logotipo do Metrô
    metro_logo = Image.open("Mapa dos Trilhos\\Imgs\\METRO_LOGO.jpg")
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
    x1, y1 = 460, 750
    x2, y2 = 510, 750
    x3, y3 = 560, 750
    x4, y4 = 610, 750
    x5, y5 = 660, 750
    x6, y6 = 710, 750
    x7, y7 = 760, 750
    x8, y8 = 810, 750
    x9, y9 = 860, 750
    x10, y10 = 910, 750
    x11, y11 = 960, 750
    x12, y12 = 1010, 750
    x13, y13 = 1060, 750
    x14, y14 = 1110, 750
    x15, y15 = 1160, 750
    x16, y16 = 1210, 750
    x17, y17 = 1260, 750
    x18, y18 = 1310, 750
    x19, y19 = 1360, 750
    x20, y20 = 1410, 750
    x21, y21 = 1460, 750
    x22, y22 = 1510, 750
    x23, y23 = 1560, 750

    # Desenha as estações
    estacao_TUC = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PIG = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JPA = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SAN = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CDU = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_TTE = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PPQ = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_TRD = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_LUZ = canvas.create_text(
        x9-5, y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BTO = canvas.create_text(
        x10-5, y10+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PSE = canvas.create_text(
        x11-5, y11+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_LIB = canvas.create_text(
        x12-5, y12+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JQM = canvas.create_text(
        x13-5, y13+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VGO = canvas.create_text(
        x14-5, y14+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PSO = canvas.create_text(
        x15-5, y15+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ANR = canvas.create_text(
        x16-5, y16+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VMN = canvas.create_text(
        x17-5, y17+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SCZ = canvas.create_text(
        x18-5, y18+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ARV = canvas.create_text(
        x19-5, y19+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SAU = canvas.create_text(
        x20-5, y20+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JUD = canvas.create_text(
        x21-5, y21+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CON = canvas.create_text(
        x22-5, y22+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JAB = canvas.create_text(
        x23-5, y23+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências
    # LUZ
    linha4_amarela_icon = canvas.create_text(
        x9-3, y9+40, text="●", font="Helvetica 32", anchor="w", fill=amarela)
    l4_icon = canvas.create_text(
        x9+6, y9+42, text="4", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha7_rubi_icon = canvas.create_text(
        x9-3, y9+60, text="●", font="Helvetica 32", anchor="w", fill=rubi)
    l7_icon = canvas.create_text(
        x9+6, y9+62, text="7", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha10_turquesa_icon = canvas.create_text(
        x9-3, y9+80, text="●", font="Helvetica 32", anchor="w", fill=turquesa)
    l10_icon = canvas.create_text(
        x9+3, y9+82, text="10", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha11_coral_icon = canvas.create_text(
        x9-3, y9+100, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x9+3, y9+102, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha13_jade_icon = canvas.create_text(
        x9-3, y9+120, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x9+3, y9+122, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # SÉ
    linha3_vermelha_icon = canvas.create_text(
        x11-3, y11+40, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
    l3_icon = canvas.create_text(
        x11+6, y11+42, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)

    # PARAÍSO
    linha2_verde_icon = canvas.create_text(
        x15-3, y15+40, text="●", font="Helvetica 32", anchor="w", fill=verde)
    l2_icon = canvas.create_text(
        x15+6, y15+42, text="2", font="Helvetica 10 bold", anchor="w", fill=branco)

    # ANA ROSA
    linha2_verde_icon = canvas.create_text(
        x16-3, y16+40, text="●", font="Helvetica 32", anchor="w", fill=verde)
    l2_icon = canvas.create_text(
        x16+6, y16+42, text="2", font="Helvetica 10 bold", anchor="w", fill=branco)

    # SANTA CRUZ
    linha5_lilas_icon = canvas.create_text(
        x18-3, y18+40, text="●", font="Helvetica 32", anchor="w", fill=lilás)
    l5_icon = canvas.create_text(
        x18+6, y18+42, text="5", font="Helvetica 10 bold", anchor="w", fill=branco)

    # Desenha a linha conectando as estações
    linha = canvas.create_line(
        x1-10, y1+12, x23+25, y23+12, fill=azul, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_TUC)
    canvas.lift(estacao_PIG)
    canvas.lift(estacao_JPA)
    canvas.lift(estacao_SAN)
    canvas.lift(estacao_CDU)
    canvas.lift(estacao_TTE)
    canvas.lift(estacao_PPQ)
    canvas.lift(estacao_TRD)
    canvas.lift(estacao_LUZ)
    canvas.lift(estacao_BTO)
    canvas.lift(estacao_PSE)
    canvas.lift(estacao_LIB)
    canvas.lift(estacao_JQM)
    canvas.lift(estacao_VGO)
    canvas.lift(estacao_PSO)
    canvas.lift(estacao_ANR)
    canvas.lift(estacao_VMN)
    canvas.lift(estacao_SCZ)
    canvas.lift(estacao_ARV)
    canvas.lift(estacao_SAU)
    canvas.lift(estacao_JUD)
    canvas.lift(estacao_CON)
    canvas.lift(estacao_JAB)
    canvas.lift(l2_icon)
    canvas.lift(l3_icon)
    canvas.lift(l4_icon)
    canvas.lift(l5_icon)
    canvas.lift(l7_icon)
    canvas.lift(l10_icon)
    canvas.lift(l11_icon)
    canvas.lift(l13_icon)

    # Define as Estações
    nome_TUC = canvas.create_text(x1+8, y1-13, text="Tucuruvi",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PIG = canvas.create_text(x2+8, y2-13, text="Parada Inglesa",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JPA = canvas.create_text(x3+8, y3-13, text="Jardim São Paulo - Ayrton Senna",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SAN = canvas.create_text(x4+8, y4-13, text="Santana",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CDU = canvas.create_text(x5+8, y5-13, text="Carandiru",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_TTE = canvas.create_text(x6+8, y6-13, text="Portuguesa Tietê",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PPQ = canvas.create_text(x7+8, y7-13, text="Armênia",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_TRD = canvas.create_text(x8+8, y8-13, text="Tiradentes",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_LUZ = canvas.create_text(x9+8, y9-13, text="Luz",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BTO = canvas.create_text(x10+8, y10-13, text="São Bento",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PSE = canvas.create_text(x11+8, y11-13, text="Sé",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_LIB = canvas.create_text(x12+8, y12-13, text="Japão - Liberdade",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JQM = canvas.create_text(x13+8, y13-13, text="São Joaquim",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VGO = canvas.create_text(x14+8, y14-13, text="Vergueiro",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PSO = canvas.create_text(x15+8, y15-13, text="Paraíso",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ANR = canvas.create_text(x16+8, y16-13, text="Ana Rosa",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VMN = canvas.create_text(x17+8, y17-13, text="Vila Mariana",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SCZ = canvas.create_text(x18+8, y18-13, text="Santa Cruz",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ARV = canvas.create_text(x19+8, y19-13, text="Praça da Árvore",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SAU = canvas.create_text(x20+8, y20-13, text="Saúde - Ultra farma",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JUD = canvas.create_text(x21+8, y21-13, text="São Judas",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CON = canvas.create_text(x22+8, y22-13, text="Conceição",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JAB = canvas.create_text(x23+8, y23-13, text="Jabaquara",
                                  font="Helvetica 12", anchor="w", angle=60)

    dev = canvas.create_text(
        960, 900, text="⚡Desenvolvido por RAFAEL BARBOSA - 10/03/2023 | Revisado em 02/09/2023", font="Helvetica 12", anchor="c")

    while True:
        root.update()
        try:
            root.update()
        except TclError:
            break