import tkinter as tk  # Criação da Interface Gráfica
from tkinter import *
from PIL import Image, ImageTk  # Manipular imagens
from colorama import Fore, Back, Style, init
from datetime import datetime

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line5():
    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 5 - LILÁS iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Criando a janela
    root = tk.Toplevel()
    root.title("Linha 5 - Lilás")
    # Define uma largura e altura específicas para a janela
    root.geometry("1920x1080")

    canvas = tk.Canvas(root, width=1920, height=1080)
    canvas.pack()

    # Carrega a imagem usando o PIL
    image = Image.open('Mapa dos Trilhos\\Favicon\\5_lilas.ico')
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
    x1, y1 = 610, 750
    x2, y2 = 660, 750
    x3, y3 = 710, 750
    x4, y4 = 760, 750
    x5, y5 = 810, 750
    x6, y6 = 860, 750
    x7, y7 = 910, 750
    x8, y8 = 960, 750
    x9, y9 = 1010, 750
    x10, y10 = 1060, 750
    x11, y11 = 1110, 750
    x12, y12 = 1160, 750
    x13, y13 = 1210, 750
    x14, y14 = 1260, 750
    x15, y15 = 1310, 750
    x16, y16 = 1360, 750
    x17, y17 = 1410, 750

    # Desenha as estações
    estacao_CKB = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SCZ = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_HSP = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SER = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_MOE = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ECT = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CPB = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BRK = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BGA = canvas.create_text(
        x9-5, y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ABV = canvas.create_text(
        x10-5, y10+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_APN = canvas.create_text(
        x11-5, y11+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_LTR = canvas.create_text(
        x12-5, y12+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_STA = canvas.create_text(
        x13-5, y13+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_GGR = canvas.create_text(
        x14-5, y14+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VBE = canvas.create_text(
        x15-5, y15+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CPL = canvas.create_text(
        x16-5, y16+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CPR = canvas.create_text(
        x17-5, y17+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências

    # CHÁCARA KLABIN
    linha2_verde_icon = canvas.create_text(
        x1-3, y1+40, text="●", font="Helvetica 32", anchor="w", fill=verde)
    l2_icon = canvas.create_text(
        x1+6, y1+42, text="2", font="Helvetica 10 bold", anchor="w", fill=branco)

    # SANTA CRUZ
    linha1_azul_icon = canvas.create_text(
        x2-3, y2+40, text="●", font="Helvetica 32", anchor="w", fill=azul)
    l1_icon = canvas.create_text(
        x2+6, y2+42, text="1", font="Helvetica 10 bold", anchor="w", fill=branco)

    # SANTO AMARO
    linha9_esmeralda_icon = canvas.create_text(
        x13-3, y13+40, text="●", font="Helvetica 32", anchor="w", fill=esmeralda)
    l9_icon = canvas.create_text(
        x13+6, y13+42, text="9", font="Helvetica 10 bold", anchor="w", fill=preto)

    # Desenha a linha conectando as estações
    linha = canvas.create_line(
        x1-10, y1+12, x17+25, y17+12, fill=lilás, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_CKB)
    canvas.lift(estacao_SCZ)
    canvas.lift(estacao_HSP)
    canvas.lift(estacao_SER)
    canvas.lift(estacao_MOE)
    canvas.lift(estacao_ECT)
    canvas.lift(estacao_CPB)
    canvas.lift(estacao_BRK)
    canvas.lift(estacao_BGA)
    canvas.lift(estacao_ABV)
    canvas.lift(estacao_APN)
    canvas.lift(estacao_LTR)
    canvas.lift(estacao_STA)
    canvas.lift(estacao_GGR)
    canvas.lift(estacao_VBE)
    canvas.lift(estacao_CPL)
    canvas.lift(estacao_CPR)
    canvas.lift(l1_icon)
    canvas.lift(l2_icon)
    canvas.lift(l9_icon)

    # Define as Estações
    nome_CKB = canvas.create_text(x1+8, y1-13, text="Chácara Klabin",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SCZ = canvas.create_text(x2+8, y2-13, text="Santa Cruz",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_HSP = canvas.create_text(x3+8, y3-13, text="Hospital São Paulo",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SER = canvas.create_text(x4+8, y4-13, text="AACD - Servidor",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_MOE = canvas.create_text(x5+8, y5-13, text="Moema",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ECT = canvas.create_text(x6+8, y6-13, text="Eucaliptos",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CPB = canvas.create_text(x7+8, y7-13, text="Campo Belo",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BRK = canvas.create_text(x8+8, y8-13, text="Brooklin",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BGA = canvas.create_text(x9+8, y9-13, text="Borba Gato",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ABV = canvas.create_text(x10+8, y10-13, text="Alto da Boa Vista",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_APN = canvas.create_text(x11+8, y11-13, text="Adolfo Pinheiro",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_LTR = canvas.create_text(x12+8, y12-13, text="Largo Treze",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_STA = canvas.create_text(x13+8, y13-13, text="Santo Amaro",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_GGR = canvas.create_text(x14+8, y14-13, text="Giovanni Gronchi",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VBE = canvas.create_text(x15+8, y15-13, text="Vila das Belezas",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CPL = canvas.create_text(x16+8, y16-13, text="Campo Limpo",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CPR = canvas.create_text(x17+8, y17-13, text="Capão Redondo",
                                  font="Helvetica 12", anchor="w", angle=60)

    dev = canvas.create_text(
        960, 900, text="⚡Desenvolvido por RAFAEL BARBOSA - 10/03/2023 | Revisado em 02/09/2023", font="Helvetica 12", anchor="c")

    while True:
        root.update()
        try:
            root.update()
        except TclError:
            break