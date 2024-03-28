import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import *  # Importa todas as classes e funções do módulo tkinter
from PIL import Image, ImageTk  # Importa classes para manipular imagens
from colorama import Fore, Back, Style, init  # Importa classes para cores de console
from datetime import datetime  # Importa a classe datetime para trabalhar com datas e horas

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line9():
    # Imprime o texto formatado com informações sobre o início do mapa da Linha 9 - Esmeralda
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 9 - ESMERALDA iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Cria uma nova janela
    root = tk.Toplevel()
    root.title("Linha 9 - Esmeralda")  # Define o título da janela
    root.geometry("1920x1080")  # Define as dimensões da janela

    canvas = tk.Canvas(root, width=1920, height=1080)  # Cria um canvas na janela
    canvas.pack()  # Empacota o canvas na janela

    # Carrega uma imagem para o ícone da janela
    image = Image.open('Mapa dos Trilhos\\Favicon\\9_esmeralda.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone da janela
    root.iconphoto(False, photo)

    # Carrega o logotipo da ViaMobilidade
    metro_logo = Image.open("Mapa dos Trilhos\\Imgs\\VM_LOGO.jpg")
    # Redimensiona a imagem do logotipo para caber no canvas
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
    x1, y1 = 510, 750
    x2, y2 = 560, 750
    x3, y3 = 610, 750
    x4, y4 = 660, 750
    x5, y5 = 710, 750
    x6, y6 = 760, 750
    x7, y7 = 810, 750
    x8, y8 = 860, 750
    x9, y9 = 910, 750
    x10, y10 = 960, 750
    x11, y11 = 1010, 750
    x12, y12 = 1060, 750
    x13, y13 = 1110, 750
    x14, y14 = 1160, 750
    x15, y15 = 1210, 750
    x16, y16 = 1260, 750
    x17, y17 = 1310, 750
    x18, y18 = 1360, 750
    x19, y19 = 1410, 750
    x20, y20 = 1460, 750
    x21, y21 = 1510, 750

    # Desenha as estações no canvas
    estacao_OSA = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PAL = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CEA = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JAG = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_USP = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PIN = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_HBR = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CJD = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VOL = canvas.create_text(
        x9-5, y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BRR = canvas.create_text(
        x10-5, y10+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_MRB = canvas.create_text(
        x11-5, y11+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_GJT = canvas.create_text(
        x12-5, y12+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JOD = canvas.create_text(
        x13-5, y13+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SAM = canvas.create_text(
        x14-5, y14+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SOC = canvas.create_text(
        x15-5, y15+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JUR = canvas.create_text(
        x16-5, y16+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_AUT = canvas.create_text(
        x17-5, y17+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_INT = canvas.create_text(
        x18-5, y18+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_GRA = canvas.create_text(
        x19-5, y19+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_MVN = canvas.create_text(
        x20-5, y20+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VAR = canvas.create_text(
        x21-5, y21+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências

    # PRESIDENTE ALTINO
    linha8_diamante_icon = canvas.create_text(
        x1-3, y1+40, text="●", font="Helvetica 32", anchor="w", fill=diamante)
    l8_icon = canvas.create_text(
        x1+6, y1+42, text="8", font="Helvetica 10 bold", anchor="w", fill=preto)

    # OSASCO
    linha8_diamante_icon = canvas.create_text(
        x2-3, y2+40, text="●", font="Helvetica 32", anchor="w", fill=diamante)
    l8_icon = canvas.create_text(
        x2+6, y2+42, text="8", font="Helvetica 10 bold", anchor="w", fill=preto)

    # PINHEIROS
    linha4_amarela_icon = canvas.create_text(
        x6-3, y6+40, text="●", font="Helvetica 32", anchor="w", fill=amarela)
    l4_icon = canvas.create_text(
        x6+6, y6+42, text="4", font="Helvetica 10 bold", anchor="w", fill=preto)

    # SANTO AMARO
    linha5_lilas_icon = canvas.create_text(
        x14-3, y14+40, text="●", font="Helvetica 32", anchor="w", fill=lilás)
    l5_icon = canvas.create_text(
        x14+6, y14+42, text="5", font="Helvetica 10 bold", anchor="w", fill=branco)

    # Desenha a linha que conecta as estações
    linha = canvas.create_line(
        x1-10, y1+12, x21+25, y21+12, fill=esmeralda, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_OSA)
    canvas.lift(estacao_PAL)
    canvas.lift(estacao_CEA)
    canvas.lift(estacao_JAG)
    canvas.lift(estacao_USP)
    canvas.lift(estacao_PIN)
    canvas.lift(estacao_HBR)
    canvas.lift(estacao_CJD)
    canvas.lift(estacao_VOL)
    canvas.lift(estacao_BRR)
    canvas.lift(estacao_MRB)
    canvas.lift(estacao_GJT)
    canvas.lift(estacao_JOD)
    canvas.lift(estacao_SAM)
    canvas.lift(estacao_SOC)
    canvas.lift(estacao_JUR)
    canvas.lift(estacao_AUT)
    canvas.lift(estacao_INT)
    canvas.lift(estacao_GRA)
    canvas.lift(estacao_MVN)
    canvas.lift(estacao_VAR)
    canvas.lift(l4_icon)
    canvas.lift(l5_icon)
    canvas.lift(l8_icon)

    # Define os nomes das estações
    nome_OSA = canvas.create_text(x1+8, y1-13, text="Osasco",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PAL = canvas.create_text(x2+8, y2-13, text="Presidente Altino",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CEA = canvas.create_text(x3+8, y3-13, text="Ceasa",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JAG = canvas.create_text(x4+8, y4-13, text="Vila Lobos - Jaguaré",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_USP = canvas.create_text(x5+8, y5-13, text="Cidade Universitária",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PIN = canvas.create_text(x6+8, y6-13, text="Pinheiros",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_HBR = canvas.create_text(x7+8, y7-13, text="Hebraica - Rebouças",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CJD = canvas.create_text(x8+8, y8-13, text="Cidade Jardim",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VOL = canvas.create_text(x9+8, y9-13, text="Vila Olímpia",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BRR = canvas.create_text(x10+8, y10-13, text="Berrini",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_MRB = canvas.create_text(x11+8, y11-13, text="Morumbi",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_GJT = canvas.create_text(x12+8, y12-13, text="Granja Julieta",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JOD = canvas.create_text(x13+8, y13-13, text="João Dias",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SAM = canvas.create_text(x14+8, y14-13, text="Santo Amaro",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SOC = canvas.create_text(x15+8, y15-13, text="Socorro",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JUR = canvas.create_text(x16+8, y16-13, text="Jurubatuba",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_AUT = canvas.create_text(x17+8, y17-13, text="Autódromo",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_INT = canvas.create_text(x18+8, y18-13, text="Primavera - Interlagos",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_GRA = canvas.create_text(x19+8, y19-13, text="Grajaú",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_MVN = canvas.create_text(x20+8, y20-13, text="Bruno Covas / Mendes - Vila Natal",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VAR = canvas.create_text(x21+8, y21-13, text="Varginha",
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