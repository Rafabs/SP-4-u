# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte pÃºblico Metropolitano do Estado de SÃ£o Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "28/06/2025 16:07"

DESCRITIVO:
    MÃ³dulo de funcionalidades especÃ­ficas

ARQUITETURA:
    Mapa_dos_Trilhos/Linhas/SP_L06.py
"""
import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import *  # Importa todas as classes e funções do módulo tkinter
from PIL import Image, ImageTk  # Importa classes para manipular imagens
from colorama import Fore, Back, Style, init  # Importa classes para cores de console
from datetime import datetime  # Importa a classe datetime para trabalhar com datas e horas

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line6():
    # Imprime o texto formatado com informações sobre o início do mapa da Linha 5 - Lilás
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 6 - LARANJA iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Criando a janela
    root = tk.Toplevel()
    root.title("Linha 6 - Laranja") # Define o título da janela
    root.geometry("1920x1080")  # Define as dimensões da janela

    # Define o ícone da janela
    canvas = tk.Canvas(root, width=1920, height=1080)  # Cria um canvas na janela
    canvas.pack()  # Empacota o canvas na janela

    # Carrega uma imagem para o ícone da janela
    image = Image.open('Mapa_dos_Trilhos\\Favicon\\6_laranja.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone da janela
    root.iconphoto(False, photo)

    # Carrega o logotipo do Metrô
    metro_logo = Image.open("Mapa_dos_Trilhos\\Imgs\\LINHA_UNI_LOGO.jpg")
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
    laranja = "#999999"    
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
    # Desenha as estações no canvas
    estacao_BRASILANDIA = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_MARISTELA = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ITB = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JPI = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_FRE = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_STM = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ABR = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_POMPEIA = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PERDIZES = canvas.create_text(
        x9-5, y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_PUC_CARDOSO_ALMEIDA = canvas.create_text(
        x10-5, y10+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_FAAP_PACAEMBU = canvas.create_text(
        x11-5, y11+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_HIG = canvas.create_text(
        x12-5, y12+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_14_BIS_SARACURA = canvas.create_text(
        x13-5, y13+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BELA_VISTA = canvas.create_text(
        x14-5, y14+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JQM = canvas.create_text(
        x15-5, y15+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências

    # ÁGUA BRANCA
    linha7_rubi_icon = canvas.create_text(
        x7-3, y7+40, text="●", font="Helvetica 32", anchor="w", fill=rubi)
    l7_icon = canvas.create_text(
        x7+6, y7+42, text="7", font="Helvetica 10 bold", anchor="w", fill=branco)
    linha8_diamante_icon = canvas.create_text(
        x7-3, y7+60, text="●", font="Helvetica 32", anchor="w", fill=diamante)
    l8_icon = canvas.create_text(
        x7+6, y7+62, text="8", font="Helvetica 10 bold", anchor="w", fill=preto)

    # HIGIENÓPOLIS - MACKENZIE
    linha4_amarela_icon = canvas.create_text(
        x12-3, y12+40, text="●", font="Helvetica 32", anchor="w", fill=amarela)
    l4_icon = canvas.create_text(
        x12+6, y12+42, text="4", font="Helvetica 10 bold", anchor="w", fill=preto)

    # SÃO JOAQUIM
    linha1_azul_icon = canvas.create_text(
        x15-3, y15+40, text="●", font="Helvetica 32", anchor="w", fill=azul)
    l1_icon = canvas.create_text(
        x15+6, y15+42, text="1", font="Helvetica 10 bold", anchor="w", fill=branco)

    # Desenha a linha que conecta as estações
    linha = canvas.create_line(
        x1-10, y1+12, x15+25, y15+12, fill=laranja, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_BRASILANDIA)
    canvas.lift(estacao_MARISTELA)
    canvas.lift(estacao_ITB)
    canvas.lift(estacao_JPI)
    canvas.lift(estacao_FRE)
    canvas.lift(estacao_STM)
    canvas.lift(estacao_ABR)
    canvas.lift(estacao_POMPEIA)
    canvas.lift(estacao_PERDIZES)
    canvas.lift(estacao_PUC_CARDOSO_ALMEIDA)
    canvas.lift(estacao_FAAP_PACAEMBU)
    canvas.lift(estacao_HIG)
    canvas.lift(estacao_14_BIS_SARACURA)
    canvas.lift(estacao_BELA_VISTA)
    canvas.lift(estacao_JQM)
    canvas.lift(l1_icon)
    canvas.lift(l4_icon)
    canvas.lift(l7_icon)
    canvas.lift(l8_icon)

    # Define os nomes das estações
    nome_BRASILANDIA = canvas.create_text(x1+8, y1-13, text="Brasilândia",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_MARISTELA = canvas.create_text(x2+8, y2-13, text="Maristela",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ITB = canvas.create_text(x3+8, y3-13, text="Itaberaba",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JPI = canvas.create_text(x4+8, y4-13, text="João Paulo I",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_FRE = canvas.create_text(x5+8, y5-13, text="Freguesia do Ó",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_STM = canvas.create_text(x6+8, y6-13, text="Santa Marina",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ABR = canvas.create_text(x7+8, y7-13, text="Água Branca",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_POMPEIA = canvas.create_text(x8+8, y8-13, text="Pompéia",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PERDIZES = canvas.create_text(x9+8, y9-13, text="Perdizes",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_PUC_CARDOSO_ALMEIDA = canvas.create_text(x10+8, y10-13, text="PUC - Cardoso de Almeida",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_FAAP_PACAEMBU = canvas.create_text(x11+8, y11-13, text="FAAP - Pacaembu",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_HIG = canvas.create_text(x12+8, y12-13, text="Higienópolis - Mackenzie",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_14_BIS_SARACURA = canvas.create_text(x13+8, y13-13, text="14 Bis - Saracura",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BELA_VISTA = canvas.create_text(x14+8, y14-13, text="Bela Vista",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JQM = canvas.create_text(x15+8, y15-13, text="São Joaquim",
                                  font="Helvetica 12", anchor="w", angle=60)

    informe = canvas.create_text(90, 90, text="LINHA EM CONSTRUÇÃO",
                                  font="Helvetica 42", anchor="w", angle=0, fill=vermelha)

    # Cria um texto na parte inferior da tela indicando a autoria e data de desenvolvimento
    dev = canvas.create_text(
        960, 900, text="⚡Desenvolvido por RAFAEL BARBOSA - 23/07/2024 | Revisado em 23/07/2024", font="Helvetica 12", anchor="c")

    # Loop principal para atualizar a janela
    while True:
        root.update()
        try:
            root.update()
        except TclError:
            break # Sai do loop caso ocorra um erro