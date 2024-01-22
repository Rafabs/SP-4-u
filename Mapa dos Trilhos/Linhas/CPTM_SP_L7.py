import tkinter as tk  # Criação da Interface Gráfica
from tkinter import *
from PIL import Image, ImageTk  # Manipular imagens
from colorama import Fore, Back, Style, init
from datetime import datetime

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line7():
    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 7 - RUBI iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")    
    # Criando a janela
    root = tk.Toplevel()
    root.title("Linha 7 - Rubi")
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
    x1, y1 = 560, 750
    x2, y2 = 610, 750
    x3, y3 = 660, 750
    x4, y4 = 710, 750
    x5, y5 = 760, 750
    x6, y6 = 810, 750
    x7, y7 = 860, 750
    x8, y8 = 910, 750
    x9, y9 = 960, 750
    x10, y10 = 1010, 750
    x11, y11 = 1060, 750
    x12, y12 = 1110, 750
    x13, y13 = 1160, 750
    x14, y14 = 1210, 750
    x15, y15 = 1260, 750
    x16, y16 = 1310, 750
    x17, y17 = 1360, 750
    x18, y18 = 1410, 750
    x19, y19 = 1460, 750

    # Desenha as estações
    estacao_BAS = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_LUZ = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BFU = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ABR = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_LPA = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PQR = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PRT = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VCL = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JRG = canvas.create_text(
        x9-5, y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VAU = canvas.create_text(
        x10-5, y10+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PRU = canvas.create_text(
        x11-5, y11+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CAI = canvas.create_text(
        x12-5, y12+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_FDR = canvas.create_text(
        x13-5, y13+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BFI = canvas.create_text(
        x14-5, y14+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_FMO = canvas.create_text(
        x15-5, y15+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BTJ = canvas.create_text(
        x16-5, y16+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CLP = canvas.create_text(
        x17-5, y17+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VPL = canvas.create_text(
        x18-5, y18+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JUN = canvas.create_text(
        x19-5, y19+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências

    # BRÁS
    linha3_vermelha_icon = canvas.create_text(
        x1-3, y1+40, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
    l3_icon = canvas.create_text(
        x1+6, y1+42, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha11_coral_icon = canvas.create_text(
        x1-3, y1+60, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x1+3, y1+62, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha12_safira_icon = canvas.create_text(
        x1-3, y1+80, text="●", font="Helvetica 32", anchor="w", fill=safira)
    l12_icon = canvas.create_text(
        x1+3, y1+82, text="12", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha13_jade_icon = canvas.create_text(
        x1-3, y1+100, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x1+3, y1+102, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # LUZ
    line_1 = canvas.create_text(
        x2-3, y2+40, text="●", font="Helvetica 32", anchor="w", fill=azul)
    l1_icon = canvas.create_text(
        x2+6, y2+42, text="1", font="Helvetica 10 bold", anchor="w", fill=branco)
    line_4 = canvas.create_text(
        x2-3, y2+60, text="●", font="Helvetica 32", anchor="w", fill=amarela)
    l4_icon = canvas.create_text(
        x2+6, y2+62, text="4", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha11_coral_icon = canvas.create_text(
        x2-3, y2+80, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x2+3, y2+82, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha13_jade_icon = canvas.create_text(
        x2-3, y2+100, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x2+3, y2+102, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # PALMEIRAS - BARRA FUNDA
    linha3_vermelha_icon = canvas.create_text(
        x3-3, y3+40, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
    l3_icon = canvas.create_text(
        x3+6, y3+42, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha8_diamante_icon = canvas.create_text(
        x3-3, y3+60, text="●", font="Helvetica 32", anchor="w", fill=diamante)
    l8_icon = canvas.create_text(
        x3+6, y3+62, text="8", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha13_jade_icon = canvas.create_text(
        x3-3, y3+80, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x3+3, y3+82, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # Desenha a linha conectando as estações
    linha = canvas.create_line(
        x1-10, y1+12, x19+25, y19+12, fill=rubi, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_BAS)
    canvas.lift(estacao_LUZ)
    canvas.lift(estacao_BFU)
    canvas.lift(estacao_ABR)
    canvas.lift(estacao_LPA)
    canvas.lift(estacao_PQR)
    canvas.lift(estacao_PRT)
    canvas.lift(estacao_VCL)
    canvas.lift(estacao_JRG)
    canvas.lift(estacao_VAU)
    canvas.lift(estacao_PRU)
    canvas.lift(estacao_CAI)
    canvas.lift(estacao_FDR)
    canvas.lift(estacao_BFI)
    canvas.lift(estacao_FMO)
    canvas.lift(estacao_BTJ)
    canvas.lift(estacao_CLP)
    canvas.lift(estacao_VPL)
    canvas.lift(estacao_JUN)
    canvas.lift(l1_icon)
    canvas.lift(l4_icon)
    canvas.lift(l3_icon)
    canvas.lift(l8_icon)
    canvas.lift(l11_icon)
    canvas.lift(l12_icon)
    canvas.lift(l13_icon)

    # Define as Estações
    nome_BAS = canvas.create_text(x1+8, y1-13, text="Brás",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_LUZ = canvas.create_text(x2+8, y2-13, text="Luz",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BFU = canvas.create_text(x3+8, y3-13, text="Palmeiras - Barra Fundas",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ABR = canvas.create_text(x4+8, y4-13, text="Água Branca",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_LPA = canvas.create_text(x5+8, y5-13, text="Lapa",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PQR = canvas.create_text(x6+8, y6-13, text="Piqueri",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PRT = canvas.create_text(x7+8, y7-13, text="Pirituba",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VCL = canvas.create_text(x8+8, y8-13, text="Vila Clarice",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JRG = canvas.create_text(x9+8, y9-13, text="Jaraguá",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VAU = canvas.create_text(x10+8, y10-13, text="Vila Aurora",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PRU = canvas.create_text(x11+8, y11-13, text="Perus",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CAI = canvas.create_text(x12+8, y12-13, text="Caieiras",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_FDR = canvas.create_text(x13+8, y13-13, text="Franco da Rocha",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BFI = canvas.create_text(x14+8, y14-13, text="Baltazar Fidélis",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_FMO = canvas.create_text(x15+8, y15-13, text="Francisco Morato",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BTJ = canvas.create_text(x16+8, y16-13, text="Botujuru",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CLP = canvas.create_text(x17+8, y17-13, text="Campo Limpo Paulista",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VPL = canvas.create_text(x18+8, y18-13, text="Várzea Paulista",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JUN = canvas.create_text(x19+8, y19-13, text="Jundiaí",
                                  font="Helvetica 12", anchor="w", angle=60)

    dev = canvas.create_text(
        960, 900, text="⚡Desenvolvido por RAFAEL BARBOSA - 10/03/2023 | Revisado em 02/09/2023", font="Helvetica 12", anchor="c")

    while True:
        root.update()
        try:
            root.update()
        except TclError:
            break