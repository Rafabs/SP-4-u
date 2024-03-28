import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import *  # Importa todas as classes e funções do módulo tkinter
from PIL import Image, ImageTk  # Importa classes para manipular imagens
from colorama import Fore, Back, Style, init  # Importa classes para cores de console
from datetime import datetime  # Importa a classe datetime para trabalhar com datas e horas

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line2():
    # Imprime o texto formatado com informações sobre o início do mapa da Linha 2 - Verde
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 2 - VERDE iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Cria uma nova janela
    root = tk.Toplevel()
    root.title("Linha 2 - Verde") # Define o título da janela
    root.geometry("1920x1080")  # Define as dimensões da janela

    # Define o ícone da janela
    canvas = tk.Canvas(root, width=1920, height=1080)  # Cria um canvas na janela
    canvas.pack()  # Empacota o canvas na janela

    # Carrega uma imagem para o ícone da janela
    image = Image.open('Mapa_dos_Trilhos\\Favicon\\2_verde.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone da janela
    root.iconphoto(False, photo)

    # Carrega o logotipo do Metrô
    metro_logo = Image.open("Mapa_dos_Trilhos\\Imgs\\METRO_LOGO.jpg")
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
    x1, y1 = 690, 750
    x2, y2 = 740, 750
    x3, y3 = 790, 750
    x4, y4 = 840, 750
    x5, y5 = 890, 750
    x6, y6 = 940, 750
    x7, y7 = 990, 750
    x8, y8 = 1040, 750
    x9, y9 = 1090, 750
    x10, y10 = 1140, 750
    x11, y11 = 1190, 750
    x12, y12 = 1240, 750
    x13, y13 = 1290, 750
    x14, y14 = 1340, 750

    # Desenha as estações no canvas
    estacao_VMD = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SUM = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CLI = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CNS = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_TRI = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BGD = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PSO = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ANR = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CKB = canvas.create_text(
        x9-5, y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_IMG = canvas.create_text(
        x10-5, y10+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_AIP = canvas.create_text(
        x11-5, y11+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SAC = canvas.create_text(
        x12-5, y12+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_TTI = canvas.create_text(
        x13-5, y13+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VPT = canvas.create_text(
        x14-5, y14+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências
    # CONSOLAÇÃO
    linha4_amarela_icon = canvas.create_text(
        x4-3, y4+40, text="●", font="Helvetica 32", anchor="w", fill=amarela)
    l4_icon = canvas.create_text(
        x4+6, y4+42, text="4", font="Helvetica 10 bold", anchor="w", fill=preto)

    # PARAÍSO
    linha1_azul_icon = canvas.create_text(
        x7-3, y7+40, text="●", font="Helvetica 32", anchor="w", fill=azul)
    l1_icon = canvas.create_text(
        x7+6, y7+42, text="1", font="Helvetica 10 bold", anchor="w", fill=branco)

    # ANA ROSA
    linha1_azul_icon = canvas.create_text(
        x8-3, y8+40, text="●", font="Helvetica 32", anchor="w", fill=azul)
    l1_icon = canvas.create_text(
        x8+6, y8+42, text="1", font="Helvetica 10 bold", anchor="w", fill=branco)

    # CHÁCARA KLABIN
    linha5_lilas_icon = canvas.create_text(
        x9-3, y9+40, text="●", font="Helvetica 32", anchor="w", fill=lilás)
    l5_icon = canvas.create_text(
        x9+6, y9+42, text="5", font="Helvetica 10 bold", anchor="w", fill=branco)

    # TAMANDUATEÍ
    linha10_turquesa_icon = canvas.create_text(
        x13-3, y13+40, text="●", font="Helvetica 32", anchor="w", fill=turquesa)
    l10_icon = canvas.create_text(
        x13+3, y13+42, text="10", font="Helvetica 10 bold", anchor="w", fill=preto)

    # VILA PRUDENTE
    linha15_prata_icon = canvas.create_text(
        x14-3, y14+40, text="●", font="Helvetica 32", anchor="w", fill=prata)
    l15_icon = canvas.create_text(
        x14+3, y14+42, text="15", font="Helvetica 10 bold", anchor="w", fill=preto)

    # Desenha a linha que conecta as estações
    linha = canvas.create_line(
        x1-10, y1+12, x14+25, y14+12, fill=verde, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_VMD)
    canvas.lift(estacao_SUM)
    canvas.lift(estacao_CLI)
    canvas.lift(estacao_CNS)
    canvas.lift(estacao_TRI)
    canvas.lift(estacao_BGD)
    canvas.lift(estacao_PSO)
    canvas.lift(estacao_ANR)
    canvas.lift(estacao_CKB)
    canvas.lift(estacao_IMG)
    canvas.lift(estacao_AIP)
    canvas.lift(estacao_SAC)
    canvas.lift(estacao_TTI)
    canvas.lift(estacao_VPT)
    canvas.lift(l1_icon)
    canvas.lift(l4_icon)
    canvas.lift(l5_icon)
    canvas.lift(l15_icon)

    # Define os nomes das estações
    nome_VMD = canvas.create_text(x1+8, y1-13, text="Vila Madalena",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SUM = canvas.create_text(x2+8, y2-13, text="Sumaré",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CLI = canvas.create_text(x3+8, y3-13, text="Clinicas",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CNS = canvas.create_text(x4+8, y4-13, text="Consolação",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_TRI = canvas.create_text(x5+8, y5-13, text="Trianon-Masp",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BGD = canvas.create_text(x6+8, y6-13, text="Brigadeiro",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PSO = canvas.create_text(x7+8, y7-13, text="Paraíso",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ANR = canvas.create_text(x8+8, y8-13, text="Ana Rosa",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CKB = canvas.create_text(x9+8, y9-13, text="Chácara Klabin",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_IMG = canvas.create_text(x10+8, y10-13, text="Imigrantes",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_AIP = canvas.create_text(x11+8, y11-13, text="Alto do Ipiranga",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SAC = canvas.create_text(x12+8, y12-13, text="Sacomã",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_TTI = canvas.create_text(x13+8, y13-13, text="Tamanduateí",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VPT = canvas.create_text(x14+8, y14-13, text="Vila Prudente",
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