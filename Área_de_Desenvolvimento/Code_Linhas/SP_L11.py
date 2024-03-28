import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import *  # Importa todas as classes e funções do módulo tkinter
from PIL import Image, ImageTk  # Importa classes para manipular imagens
from colorama import Fore, Back, Style, init  # Importa classes para cores de console
from datetime import datetime  # Importa a classe datetime para trabalhar com datas e horas

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line11():
    # Imprime o texto formatado com informações sobre o início do mapa da Linha 11 - Coral
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 11 - CORAL iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Cria uma nova janela
    root = tk.Toplevel()
    root.title("Linha 11 - Coral")  # Define o título da janela
    root.geometry("1920x1080")  # Define as dimensões da janela

    canvas = tk.Canvas(root, width=1920, height=1080)  # Cria um canvas na janela
    canvas.pack()  # Empacota o canvas na janela

    # Carrega uma imagem para o ícone da janela
    image = Image.open('Mapa_dos_Trilhos\\Favicon\\cptm.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone da janela
    root.iconphoto(False, photo)

    # Carrega o logotipo da CPTM
    metro_logo = Image.open("Mapa_dos_Trilhos\\Imgs\\CPTM_LOGO.jpg")
    # Redimensiona a imagem do logotipo para caber no canvas
    metro_logo = metro_logo.resize((130, 50))
    metro_logo_tk = ImageTk.PhotoImage(metro_logo)

    # Insere a imagem do logotipo no canvas
    canvas.create_image(0, 0, anchor="nw", image=metro_logo_tk)

    # Definição das cores usadas no mapa
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

    # Cores de background
    preto = "#000000"
    branco = "#FFFFFF"

    # Definição das coordenadas para cada estação no canvas
    # Aqui estão definidas as posições x e y de todas as estações no mapa
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

    # Desenha as estações no canvas
    estacao_BFU = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_LUZ = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BAS = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_TAT = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ITQ = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_DBO = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JBO = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_GUA = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_AGN = canvas.create_text(
        x9-5, y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_FVC = canvas.create_text(
        x10-5, y10+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_POA = canvas.create_text(
        x11-5, y11+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CVN = canvas.create_text(
        x12-5, y12+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SUZ = canvas.create_text(
        x13-5, y13+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JPB = canvas.create_text(
        x14-5, y14+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BCB = canvas.create_text(
        x15-5, y15+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_MDC = canvas.create_text(
        x16-5, y16+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_EST = canvas.create_text(
        x17-5, y17+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências
    # PALMEIRAS - BARRA FUNDA
    linha3_vermelha_icon = canvas.create_text(
        x1-3, y1+40, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
    l3_icon = canvas.create_text(
        x1+6, y1+42, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha7_rubi_icon = canvas.create_text(
        x1-3, y1+60, text="●", font="Helvetica 32", anchor="w", fill=rubi)
    l7_icon = canvas.create_text(
        x1+6, y1+62, text="7", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha8_diamante_icon = canvas.create_text(
        x1-3, y1+80, text="●", font="Helvetica 32", anchor="w", fill=diamante)
    l8_icon = canvas.create_text(
        x1+6, y1+82, text="8", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha13_jade_icon = canvas.create_text(
        x1-3, y1+100, text="●",  font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x1+3, y1+102, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # LUZ
    linha1_azul_icon = canvas.create_text(
        x2-3, y2+40, text="●", font="Helvetica 32", anchor="w", fill=azul)
    l1_icon = canvas.create_text(
        x2+6, y2+42, text="1", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha4_amarela_icon = canvas.create_text(
        x2-3, y2+60, text="●", font="Helvetica 32", anchor="w", fill=amarela)
    l4_icon = canvas.create_text(
        x2+6, y2+62, text="4", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha7_rubi_icon = canvas.create_text(
        x2-3, y2+80,  text="●", font="Helvetica 32", anchor="w", fill=rubi)
    l7_icon = canvas.create_text(
        x2+6, y2+82, text="7", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha13_jade_icon = canvas.create_text(
        x2-3, y2+100, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x2+3, y2+102, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # BRÁS
    linha3_vermelha_icon = canvas.create_text(
        x3-3, y3+40, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
    l3_icon = canvas.create_text(
        x3+6, y3+42, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha7_rubi_icon = canvas.create_text(
        x3-3, y3+60, text="●", font="Helvetica 32", anchor="w", fill=rubi)
    l7_icon = canvas.create_text(
        x3+6, y3+62, text="7", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha10_turquesa_icon = canvas.create_text(
        x3-3, y3+80, text="●", font="Helvetica 32", anchor="w", fill=turquesa)
    l10_icon = canvas.create_text(
        x3+3, y3+82, text="10", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha12_safira_icon = canvas.create_text(
        x3-3, y3+100, text="●", font="Helvetica 32", anchor="w", fill=safira)
    l12_icon = canvas.create_text(
        x3+3, y3+102, text="12", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha13_jade_icon = canvas.create_text(
        x3-3, y3+120, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x3+3, y3+122, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # TATUAPÉ
    linha3_vermelha_icon = canvas.create_text(
        x4-3, y4+40, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
    l3_icon = canvas.create_text(
        x4+6, y4+42, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha12_safira_icon = canvas.create_text(
        x4-3, y4+60, text="●", font="Helvetica 32", anchor="w", fill=safira)
    l12_icon = canvas.create_text(
        x4+3, y4+62, text="12", font="Helvetica 10 bold", anchor="w", fill=branco)

    # CORINTHIANS - ITAQUERA
    linha3_vermelha_icon = canvas.create_text(
        x5-3, y5+40, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
    l3_icon = canvas.create_text(
        x5+6, y4+42, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)

    # CALMON VIANA
    line_12 = canvas.create_text(
        x12-3, y12+40, text="●", font="Helvetica 32", anchor="w", fill=safira)
    l12_icon = canvas.create_text(
        x12+3, y12+42, text="12", font="Helvetica 10 bold", anchor="w", fill=branco)

    # Desenha a linha que conecta as estações
    linha = canvas.create_line(
        x1-10, y1+12, x17+25, y17+12, fill=coral, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_BFU)
    canvas.lift(estacao_LUZ)
    canvas.lift(estacao_BAS)
    canvas.lift(estacao_TAT)
    canvas.lift(estacao_ITQ)
    canvas.lift(estacao_DBO)
    canvas.lift(estacao_JBO)
    canvas.lift(estacao_GUA)
    canvas.lift(estacao_AGN)
    canvas.lift(estacao_FVC)
    canvas.lift(estacao_POA)
    canvas.lift(estacao_CVN)
    canvas.lift(estacao_SUZ)
    canvas.lift(estacao_JPB)
    canvas.lift(estacao_BCB)
    canvas.lift(estacao_MDC)
    canvas.lift(estacao_EST)
    canvas.lift(l1_icon)
    canvas.lift(l3_icon)
    canvas.lift(l4_icon)
    canvas.lift(l7_icon)
    canvas.lift(l8_icon)
    canvas.lift(l10_icon)
    canvas.lift(l12_icon)
    canvas.lift(l13_icon)

    # Define os nomes das estações
    nome_BFU = canvas.create_text(x1+8, y1-13, text="Palmeiras - Barra Funda",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_LUZ = canvas.create_text(x2+8, y2-13, text="Luz",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BAS = canvas.create_text(x3+8, y3-13, text="Brás",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_TAT = canvas.create_text(x4+8, y4-13, text="Tatuapé",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ITQ = canvas.create_text(x5+8, y5-13, text="Corinthians - Itaquera",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_DBO = canvas.create_text(x6+8, y6-13, text="Dom Bosco",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JBO = canvas.create_text(x7+8, y7-13, text="José Bonifácio",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_GUA = canvas.create_text(x8+8, y8-13, text="Guaianazes",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_AGN = canvas.create_text(x9+8, y9-13, text="Antônio Gianetti Neto",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_FVC = canvas.create_text(x10+8, y10-13, text="Ferraz de Vasconcelos",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_POA = canvas.create_text(x11+8, y11-13, text="Poá",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CVN = canvas.create_text(x12+8, y12-13, text="Calmon Viana",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SUZ = canvas.create_text(x13+8, y13-13, text="Suzano",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JPB = canvas.create_text(x14+8, y14-13, text="Jundiapeba",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BCB = canvas.create_text(x15+8, y15-13, text="Braz Cubas",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_MDC = canvas.create_text(x16+8, y16-13, text="Mogi das Cruzes",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_EST = canvas.create_text(x17+8, y17-13, text="Estudantes",
                                  font="Helvetica 12", anchor="w", angle=60)

    # Cria um texto na parte inferior da tela indicando a autoria e data de desenvolvimento
    dev = canvas.create_text(
        960, 900, text="⚡Desenvolvido por RAFAEL BARBOSA - 10/03/2023 | Revisado em 02/09/2023", font="Helvetica 12", anchor="c")

    # Loop principal para atualizar a janela
    while True:
        root.update()
        try:
            root.update()
        except TclError:
            break # Sai do loop caso ocorra um erro