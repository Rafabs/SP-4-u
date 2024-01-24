import tkinter as tk  # Criação da Interface Gráfica
from tkinter import *
from PIL import Image, ImageTk  # Manipular imagens
from colorama import Fore, Back, Style, init
from datetime import datetime

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line8():
    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 8 - DIAMANTE iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Criando a janela
    root = tk.Toplevel()
    root.title("Linha 8 - Diamante")
    # Define uma largura e altura específicas para a janela
    root.geometry("1920x1080")

    canvas = tk.Canvas(root, width=1920, height=1080)
    canvas.pack()

    # Carrega a imagem usando o PIL
    image = Image.open('Mapa dos Trilhos\\Favicon\\8_diamante.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone
    root.iconphoto(False, photo)

    # Carrega o logotipo do Metrô
    metro_logo = Image.open("Mapa dos Trilhos\\Imgs\\VM_LOGO.jpg")
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
    x1, y1 = 410, 750
    x2, y2 = 460, 750
    x3, y3 = 510, 750
    x4, y4 = 560, 750
    x5, y5 = 610, 750
    x6, y6 = 660, 750
    x7, y7 = 710, 750
    x8, y8 = 760, 750
    x9, y9 = 810, 750
    x10, y10 = 860, 750
    x11, y11 = 910, 750
    x12, y12 = 960, 750
    x13, y13 = 1010, 750
    x14, y14 = 1060, 750
    x15, y15 = 1110, 750
    x16, y16 = 1160, 750
    x17, y17 = 1210, 750
    x18, y18 = 1260, 750
    x19, y19 = 1310, 750
    x20, y20 = 1360, 750
    x21, y21 = 1410, 750
    x22, y22 = 1460, 750
    x23, y23 = 1510, 750
    x24, y24 = 1560, 750

    # Desenha as estações
    estacao_JPR = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BFU = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_LAP = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_DMO = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ILE = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PAL = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_OSA = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CSA = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_QTU = canvas.create_text(
        x9-5, y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_GMC = canvas.create_text(
        x10-5, y10+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CPB = canvas.create_text(
        x11-5, y11+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_STE = canvas.create_text(
        x12-5, y12+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_AJO = canvas.create_text(
        x13-5, y13+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BRU = canvas.create_text(
        x14-5, y14+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JBE = canvas.create_text(
        x15-5, y15+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JSI = canvas.create_text(
        x16-5, y16+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JDI = canvas.create_text(
        x17-5, y17+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SCO = canvas.create_text(
        x18-5, y18+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ECD = canvas.create_text(
        x19-5, y19+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_IPV = canvas.create_text(
        x20-5, y20+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SRT = canvas.create_text(
        x21-5, y21+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CMR = canvas.create_text(
        x22-5, y22+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_AMB = canvas.create_text(
        x23-5, y23+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ABU = canvas.create_text(
        x24-5, y24+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências

    # BARRA FUNDA
    linha3_vermelha_icon = canvas.create_text(
        x2-3, y2+40, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
    l3_icon = canvas.create_text(
        x2+6, y2+42, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha7_rubi_icon = canvas.create_text(
        x2-3, y2+60, text="●", font="Helvetica 32", anchor="w", fill=rubi)
    l7_icon = canvas.create_text(
        x2+6, y2+62, text="7", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha11_coral_icon = canvas.create_text(
        x2-3, y2+80, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x2+3, y2+82, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha13_jade_icon = canvas.create_text(
        x2-3, y2+100, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x2+3, y2+102, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # PRESIDENTE ALTINO
    linha9_esmeralda_icon = canvas.create_text(
        x6-3, y6+40, text="●", font="Helvetica 32", anchor="w", fill=esmeralda)
    l9_icon = canvas.create_text(
        x6+6, y6+42, text="9", font="Helvetica 10 bold", anchor="w", fill=preto)

    # OSASCO
    linha9_esmeralda_icon = canvas.create_text(
        x7-3, y7+40, text="●", font="Helvetica 32", anchor="w", fill=esmeralda)
    l9_icon = canvas.create_text(
        x7+6, y7+42, text="9", font="Helvetica 10 bold", anchor="w", fill=preto)

    # Desenha a linha conectando as estações
    linha = canvas.create_line(
        x1-10, y1+12, x24+25, y24+12, fill=diamante, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_JPR)
    canvas.lift(estacao_BFU)
    canvas.lift(estacao_LAP)
    canvas.lift(estacao_DMO)
    canvas.lift(estacao_ILE)
    canvas.lift(estacao_PAL)
    canvas.lift(estacao_OSA)
    canvas.lift(estacao_CSA)
    canvas.lift(estacao_QTU)
    canvas.lift(estacao_GMC)
    canvas.lift(estacao_CPB)
    canvas.lift(estacao_STE)
    canvas.lift(estacao_AJO)
    canvas.lift(estacao_BRU)
    canvas.lift(estacao_JBE)
    canvas.lift(estacao_JSI)
    canvas.lift(estacao_JDI)
    canvas.lift(estacao_SCO)
    canvas.lift(estacao_ECD)
    canvas.lift(estacao_IPV)
    canvas.lift(estacao_SRT)
    canvas.lift(estacao_CMR)
    canvas.lift(estacao_AMB)
    canvas.lift(estacao_ABU)
    canvas.lift(l7_icon)
    canvas.lift(l9_icon)
    canvas.lift(l11_icon)
    canvas.lift(l13_icon)

    # Define as Estações
    nome_JPR = canvas.create_text(x1+8, y1-13, text="Júlio Prestes",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BFU = canvas.create_text(x2+8, y2-13, text="Palmeiras - Barra Funda",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_LAP = canvas.create_text(x3+8, y3-13, text="Lapa",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_DMO = canvas.create_text(x4+8, y4-13, text="Domingos de Moraes",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ILE = canvas.create_text(x5+8, y5-13, text="Imperatriz Leopoldina",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PAL = canvas.create_text(x6+8, y6-13, text="Presidente Altino",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_OSA = canvas.create_text(x7+8, y7-13, text="Osasco",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CSA = canvas.create_text(x8+8, y8-13, text="Comandante Sampaio",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_QTU = canvas.create_text(x9+8, y9-13, text="Quitaúna",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_GMC = canvas.create_text(x10+8, y10-13, text="General Miguel Costa",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CPB = canvas.create_text(x11+8, y11-13, text="Carapicuíba",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_STE = canvas.create_text(x12+8, y12-13, text="Santa Terezinha",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_AJO = canvas.create_text(x13+8, y13-13, text="Antônio João",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BRU = canvas.create_text(x14+8, y14-13, text="Barueri",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JBE = canvas.create_text(x15+8, y15-13, text="Jardim Belval",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JSI = canvas.create_text(x16+8, y16-13, text="Jardim Silveira",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JDI = canvas.create_text(x17+8, y17-13, text="Jandira",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SCO = canvas.create_text(x18+8, y18-13, text="Sagrado Coração",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ECD = canvas.create_text(x19+8, y19-13, text="Engenheiro Cardoso",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_IPV = canvas.create_text(x20+8, y20-13, text="Itapevi",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SRT = canvas.create_text(x21+8, y21-13, text="Santa Rita",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CMR = canvas.create_text(x22+8, y22-13, text="Cimenrita",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_AMB = canvas.create_text(x23+8, y23-13, text="Ambuitá",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ABU = canvas.create_text(x24+8, y24-13, text="Amador Bueno",
                                  font="Helvetica 12", anchor="w", angle=60)

    dev = canvas.create_text(
        960, 900, text="⚡Desenvolvido por RAFAEL BARBOSA - 10/03/2023 | Revisado em 02/09/2023", font="Helvetica 12", anchor="c")

    while True:
        root.update()
        try:
            root.update()
        except TclError:
            break