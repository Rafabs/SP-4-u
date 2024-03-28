import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import *  # Importa todas as classes e funções do módulo tkinter
from PIL import Image, ImageTk  # Importa classes para manipular imagens
from colorama import Fore, Back, Style, init  # Importa classes para cores de console
from datetime import datetime  # Importa a classe datetime para trabalhar com datas e horas

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line4():
    # Imprime o texto formatado com informações sobre o início do mapa da Linha 4 - Amarela
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 4 - AMARELA iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Criando a janela
    root = tk.Toplevel()
    root.title("Linha 4 - Amarela") # Define o título da janela
    root.geometry("1920x1080")  # Define as dimensões da janela

    # Define o ícone da janela
    canvas = tk.Canvas(root, width=1920, height=1080)  # Cria um canvas na janela
    canvas.pack()  # Empacota o canvas na janela

    # Carrega uma imagem para o ícone da janela
    image = Image.open('Mapa dos Trilhos\\Favicon\\4_amarela.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone da janela
    root.iconphoto(False, photo)

    # Carrega o logotipo do Metrô
    viaquatro_logo = Image.open("Mapa dos Trilhos\\Imgs\\VIAQUATRO_LOGO.jpg")
    # Redimensiona a imagem para ajustar ao tamanho do canvas
    viaquatro_logo = viaquatro_logo.resize((150, 40))
    viaquatro_logo_tk = ImageTk.PhotoImage(viaquatro_logo)

     # Insere a imagem do logotipo no canvas
    canvas.create_image(0, 0, anchor="nw", image=viaquatro_logo)

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
    x1, y1 = 760, 750
    x2, y2 = 810, 750
    x3, y3 = 860, 750
    x4, y4 = 910, 750
    x5, y5 = 960, 750
    x6, y6 = 1010, 750
    x7, y7 = 1060, 750
    x8, y8 = 1110, 750
    x9, y9 = 1160, 750
    x10, y10 = 1210, 750
    x11, y11 = 1260, 750

    # Desenha as estações no canvas
    estacao_LUZ = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_REP = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_HIG = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PTA = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_FRE = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_FRA = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_FAL = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PIN = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BUT = canvas.create_text(
        x9-5, y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_MBI = canvas.create_text(
        x10-5, y10+8,  text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VSO = canvas.create_text(
        x11-5, y11+8,  text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências
    # LUZ
    linha1_azul_icon = canvas.create_text(
        x1-3, y1+40, text="●", font="Helvetica 32", anchor="w", fill=azul)
    l1_icon = canvas.create_text(
        x1+6, y1+42, text="1", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha7_rubi_icon = canvas.create_text(
        x1-3, y1+60, text="●", font="Helvetica 32", anchor="w", fill=rubi)
    l7_icon = canvas.create_text(
        x1+6, y1+62, text="7", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha10_turquesa_icon = canvas.create_text(
        x1-3, y1+80, text="●", font="Helvetica 32", anchor="w", fill=turquesa)
    l10_icon = canvas.create_text(
        x1+3, y1+82, text="10", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha11_coral_icon = canvas.create_text(
        x1-3, y1+100, text="●", font="Helvetica 32", anchor="w", fill=coral)
    l11_icon = canvas.create_text(
        x1+3, y1+102, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)
    linha13_jade_icon = canvas.create_text(
        x1-3, y1+120, text="●", font="Helvetica 32", anchor="w", fill=jade)
    l13_icon = canvas.create_text(
        x1+3, y1+122, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

    # REPÚBLICA
    linha3_vermelha_icon = canvas.create_text(
        x2-3, y2+40, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
    l3_icon = canvas.create_text(
        x2+6, y2+42, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)

    # PAULISTA
    linha2_verde_icon = canvas.create_text(
        x4-3, y4+40, text="●", font="Helvetica 32", anchor="w", fill=verde)
    l2_icon = canvas.create_text(
        x4+6, y4+42, text="2", font="Helvetica 10 bold", anchor="w", fill=branco)

    # PINHEIROS
    linha9_esmeralda_icon = canvas.create_text(
        x8-3, y8+40, text="●", font="Helvetica 32", anchor="w", fill=esmeralda)
    l9_icon = canvas.create_text(
        x8+6, y8+42, text="9", font="Helvetica 10 bold", anchor="w", fill=preto)

    # Desenha a linha que conecta as estações
    linha = canvas.create_line(
        x1-10, y1+12, x11+25, y11+12, fill=amarela, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_LUZ)
    canvas.lift(estacao_REP)
    canvas.lift(estacao_HIG)
    canvas.lift(estacao_PTA)
    canvas.lift(estacao_FRE)
    canvas.lift(estacao_FRA)
    canvas.lift(estacao_FAL)
    canvas.lift(estacao_PIN)
    canvas.lift(estacao_BUT)
    canvas.lift(estacao_MBI)
    canvas.lift(estacao_VSO)
    canvas.lift(l1_icon)
    canvas.lift(l2_icon)
    canvas.lift(l3_icon)
    canvas.lift(l7_icon)
    canvas.lift(l9_icon)
    canvas.lift(l10_icon)
    canvas.lift(l11_icon)
    canvas.lift(l13_icon)

    # Define os nomes das estações
    LUZ = canvas.create_text(x1+8, y1-13, text="Luz",
                             font="Helvetica 12", anchor="w", angle=60)
    REP = canvas.create_text(x2+8, y2-13, text="República",
                             font="Helvetica 12", anchor="w", angle=60)
    MCK = canvas.create_text(x3+8, y3-13, text="Higienópolis - Mackenzie",
                             font="Helvetica 12", anchor="w", angle=60)
    PLT = canvas.create_text(x4+8, y4-13, text="Paulista - Pernambucanas",
                             font="Helvetica 12", anchor="w", angle=60)
    OFR = canvas.create_text(x5+8, y5-13, text="Oscar Freire",
                             font="Helvetica 12", anchor="w", angle=60)
    FRC = canvas.create_text(x6+8, y6-13, text="Fradique Coutinho",
                             font="Helvetica 12", anchor="w", angle=60)
    FLM = canvas.create_text(x7+8, y7-13, text="Faria Lima",
                             font="Helvetica 12", anchor="w", angle=60)
    PIN = canvas.create_text(x8+8, y8-13, text="Pinheiros",
                             font="Helvetica 12", anchor="w", angle=60)
    BUT = canvas.create_text(x9+8, y9-13, text="Butantã",
                             font="Helvetica 12", anchor="w", angle=60)
    MOR = canvas.create_text(x10+8, y10-13, text="São Paulo - Morumbi",
                             font="Helvetica 12", anchor="w", angle=60)
    VSN = canvas.create_text(x11+8, y11-13, text="Vila Sônia - Profª Elisabeth Terneiro",
                             font="Helvetica 12", anchor="w", angle=60)

    # Cria um texto na parte inferior da tela indicando a autoria e data de desenvolvimento
    dev = canvas.create_text(
        960, 900, text="⚡Desenvolvido por RAFAEL BARBOSA - 10/03/2023 | Revisado em 24/01/2024", font="Helvetica 12", anchor="c")
    
    # Loop principal para atualizar a janela
    while True:
        root.update()
        try:
            root.update()
        except TclError:
            break # Sai do loop caso ocorra um erro