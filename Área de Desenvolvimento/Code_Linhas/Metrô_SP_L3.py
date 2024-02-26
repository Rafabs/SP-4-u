import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import *  # Importa todas as classes e funções do módulo tkinter
from PIL import Image, ImageTk  # Importa classes para manipular imagens
from colorama import Fore, Back, Style, init  # Importa classes para cores de console
from datetime import datetime  # Importa a classe datetime para trabalhar com datas e horas

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line3():
    # Imprime o texto formatado com informações sobre o início do mapa da Linha 3 - Vermelha
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 3 - VERMELHA iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Criando a janela
    root = tk.Toplevel()
    root.title("Linha 3 - Vermelha") # Define o título da janela
    root.geometry("1920x1080")  # Define as dimensões da janela

    # Define o ícone da janela
    canvas = tk.Canvas(root, width=1920, height=1080)  # Cria um canvas na janela
    canvas.pack()  # Empacota o canvas na janela

    # Carrega uma imagem para o ícone da janela
    image = Image.open('Mapa dos Trilhos\\Favicon\\3_vermelha.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone da janela
    root.iconphoto(False, photo)

    # Carrega o logotipo do Metrô
    metro_logo = Image.open("Mapa dos Trilhos\\Imgs\\METRO_LOGO.jpg")
    # Redimensiona a imagem para ajustar ao tamanho do canvas
    metro_logo = metro_logo.resize((120, 50))
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
    x1, y1 = 540, 750
    x2, y2 = 590, 750
    x3, y3 = 640, 750
    x4, y4 = 690, 750
    x5, y5 = 740, 750
    x6, y6 = 790, 750
    x7, y7 = 840, 750
    x8, y8 = 890, 750
    x9, y9 = 940, 750
    x10, y10 = 990, 750
    x11, y11 = 1040, 750
    x12, y12 = 1090, 750
    x13, y13 = 1140, 750
    x14, y14 = 1190, 750
    x15, y15 = 1240, 750
    x16, y16 = 1290, 750
    x17, y17 = 1340, 750
    x18, y18 = 1390, 750

    # Desenha as estações no canvas
    estacao_BFU = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_DEO = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CEC = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_REP = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_GBU = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PSE = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PDS = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BAS = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BRE = canvas.create_text(
        x9-5, y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BEL = canvas.create_text(
        x10-5, y10+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_TAT = canvas.create_text(
        x11-5, y11+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CAR = canvas.create_text(
        x12-5, y12+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PEN = canvas.create_text(
        x13-5, y13+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VTD = canvas.create_text(
        x14-5, y14+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VPA = canvas.create_text(
        x15-5, y15+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PCA = canvas.create_text(
        x16-5, y16+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ART = canvas.create_text(
        x17-5, y17+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ITQ = canvas.create_text(
        x18-5, y18+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências
    # PALMEIRAS - BARRA FUNDA
    linha7_rubi_icon = canvas.create_text(
        x1-3, y1+40, text="●", font="Helvetica 32", anchor="w", fill=rubi)
    l7_icon = canvas.create_text(
        x1+6, y1+42, text="7", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha8_diamante_icon = canvas.create_text(
        x1-3, y1+60, text="●", font="Helvetica 32", anchor="w", fill=diamante)
    l8_icon = canvas.create_text(
        x1+6, y1+62, text="8", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha11_coral_icon = canvas.create_text(
        x1-3, y1+80, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x1+3, y1+82, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha13_jade_icon = canvas.create_text(
        x1-3, y1+100, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x1+3, y1+102, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # REPÚBLICA
    linha4_amarela_icon = canvas.create_text(
        x4-3, y4+40, text="●", font="Helvetica 32", anchor="w", fill=amarela)
    l4_icon = canvas.create_text(
        x4+6, y4+42, text="4", font="Helvetica 10 bold", anchor="w", fill=preto)

    # SÉ
    linha1_azul_icon = canvas.create_text(
        x6-3, y6+40, text="●", font="Helvetica 32", anchor="w", fill=azul)
    l1_icon = canvas.create_text(
        x6+6, y6+42, text="1", font="Helvetica 10 bold", anchor="w", fill=branco)

    # BRÁS
    linha7_rubi_icon = canvas.create_text(
        x8-3, y8+40, text="●", font="Helvetica 32", anchor="w", fill=rubi)
    l7_icon = canvas.create_text(
        x8+6, y8+42, text="7", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha10_turquesa_icon = canvas.create_text(
        x8-3, y8+60, text="●", font="Helvetica 32", anchor="w", fill=turquesa)
    l10_icon = canvas.create_text(
        x8+3, y8+62, text="10", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha11_coral_icon = canvas.create_text(
        x8-3, y8+80, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x8+3, y8+82, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha12_safira_icon = canvas.create_text(
        x8-3, y8+100, text="●", font="Helvetica 32", anchor="w", fill=safira)
    l12_icon = canvas.create_text(
        x8+3, y8+102, text="12", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha13_jade_icon = canvas.create_text(
        x8-3, y8+120, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x8+3, y8+122, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # TATUAPÉ
    linha11_coral_icon = canvas.create_text(
        x11-3, y11+40, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x11+3, y11+42, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha12_safira_icon = canvas.create_text(
        x11-3, y11+60,  text="●", font="Helvetica 32", anchor="w", fill=safira)
    l12_icon = canvas.create_text(
        x11+3, y11+62, text="12", font="Helvetica 10 bold", anchor="w", fill=branco)

    # PENHA
    linha2_verde_icon = canvas.create_text(
        x13-3, y13+40, text="●", font="Helvetica 32", anchor="w", fill=verde)
    l2_icon = canvas.create_text(
        x13+6, y13+42, text="2", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha11_coral_icon = canvas.create_text(
        x13-3, y13+60, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x13+3, y13+62, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)

    # CORINTHIANS - ITAQUERA
    linha11_coral_icon = canvas.create_text(
        x18-3, y18+40, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x18+3, y18+42, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)

    # Desenha a linha que conecta as estações
    linha = canvas.create_line(
        x1-10, y1+12, x18+25, y18+12, fill=vermelha, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_BFU)
    canvas.lift(estacao_DEO)
    canvas.lift(estacao_CEC)
    canvas.lift(estacao_REP)
    canvas.lift(estacao_GBU)
    canvas.lift(estacao_PSE)
    canvas.lift(estacao_PDS)
    canvas.lift(estacao_BAS)
    canvas.lift(estacao_BRE)
    canvas.lift(estacao_BEL)
    canvas.lift(estacao_TAT)
    canvas.lift(estacao_CAR)
    canvas.lift(estacao_PEN)
    canvas.lift(estacao_VTD)
    canvas.lift(estacao_VPA)
    canvas.lift(estacao_PCA)
    canvas.lift(estacao_ART)
    canvas.lift(estacao_ITQ)
    canvas.lift(l1_icon)
    canvas.lift(l2_icon)
    canvas.lift(l4_icon)
    canvas.lift(l7_icon)
    canvas.lift(l8_icon)
    canvas.lift(l10_icon)
    canvas.lift(l11_icon)
    canvas.lift(l12_icon)
    canvas.lift(l13_icon)

    # Define os nomes das estações
    nome_BFU = canvas.create_text(x1+8, y1-13, text="Palmeiras - Barra Funda",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_DEO = canvas.create_text(x2+8, y2-13, text="Marechal Deodoro",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CEC = canvas.create_text(x3+8, y3-13, text="Santa Cecília",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_REP = canvas.create_text(x4+8, y4-13, text="República",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_GBU = canvas.create_text(x5+8, y5-13, text="Anhangabaú",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PSE = canvas.create_text(x6+8, y6-13, text="Sé",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PDS = canvas.create_text(x7+8, y7-13, text="Pedro ll",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BAS = canvas.create_text(x8+8, y8-13, text="Brás",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BRE = canvas.create_text(x9+8, y9-13, text="Bresser - Mooca",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BEL = canvas.create_text(x10+8, y10-13, text="Belém",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_TAT = canvas.create_text(x11+8, y11-13, text="Tatuapé",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CAR = canvas.create_text(x12+8, y12-13, text="Carrão - Assaí Atacadista",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PEN = canvas.create_text(x13+8, y13-13, text="Penha - Lojas Besni",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VTD = canvas.create_text(x14+8, y14-13, text="Vila Matilde",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VPA = canvas.create_text(x15+8, y11-13, text="Guilhermina - Esperança",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PCA = canvas.create_text(x16+8, y12-13, text="Patriarca - Vila Ré",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ART = canvas.create_text(x17+8, y13-13, text="Artur Alvim",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ITQ = canvas.create_text(x18+8, y14-13, text="Corinthians - Itaquera",
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