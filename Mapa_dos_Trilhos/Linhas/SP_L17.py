# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte pÃºblico Metropolitano do Estado de SÃ£o Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "30/06/2025 00:42"

DESCRITIVO:
MÃ³dulo de funcionalidades especÃ­ficas
ARQUITETURA:
    Mapa_dos_Trilhos/Linhas/SP_L17.py
"""
import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import *  # Importa todas as classes e funções do módulo tkinter
from PIL import Image, ImageTk  # Importa classes para manipular imagens
from colorama import Fore, Back, Style, init  # Importa classes para cores de console
from datetime import datetime  # Importa a classe datetime para trabalhar com datas e horas

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line17():
    # Imprime o texto formatado com informações sobre o início do mapa da Linha 5 - Lilás
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 17 - OURO iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Criando a janela
    root = tk.Toplevel()
    root.title("Linha 17 - Ouro") # Define o título da janela
    root.geometry("1920x1080")  # Define as dimensões da janela

    # Define o ícone da janela
    canvas = tk.Canvas(root, width=1920, height=1080)  # Cria um canvas na janela
    canvas.pack()  # Empacota o canvas na janela

    # Carrega uma imagem para o ícone da janela
    image = Image.open('Mapa_dos_Trilhos\\Favicon\\17_ouro.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone da janela
    root.iconphoto(False, photo)

    # Carrega o logotipo do Metrô
    metro_logo = Image.open("Mapa_dos_Trilhos\\Imgs\\VM_LOGO.jpg")
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
    ouro = "#999999"    

    # Cores de background
    preto = "#000000"
    branco = "#FFFFFF"

    # Definição das coordenadas para cada estação no canvas
    # Aqui estão definidas as posições x e y de todas as estações no mapa
    x1, y1 = 810, 750
    x2, y2 = 860, 750
    x3, y3 = 910, 750
    x4, y4 = 960, 750
    x5, y5 = 1010, 750
    x6, y6 = 1060, 750
    x7, y7 = 1110, 750
    x8, y8 = 1160, 750

    # Desenha as estações no canvas
    estacao_JAP = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CGN = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_BPA = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VJD = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CMB = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VCD = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CZD = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_MOB = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências

    # CAMPO BELO
    linha5_lilas_icon = canvas.create_text(
        x5-3, y5+40, text="●", font="Helvetica 32", anchor="w", fill=lilás)
    l5_icon = canvas.create_text(
        x5+6, y5+42, text="5", font="Helvetica 10 bold", anchor="w", fill=branco)

    # MORUMBI
    linha9_esmeralda_icon = canvas.create_text(
        x8-3, y8+40, text="●", font="Helvetica 32", anchor="w", fill=esmeralda)
    l9_icon = canvas.create_text(
        x8+6, y8+42, text="9", font="Helvetica 10 bold", anchor="w", fill=branco)

    # Desenha a linha que conecta as estações
    linha = canvas.create_line(
        x1-10, y1+12, x8+25, y8+12, fill=ouro, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_JAP)
    canvas.lift(estacao_CGN)
    canvas.lift(estacao_BPA)
    canvas.lift(estacao_VJD)
    canvas.lift(estacao_CMB)
    canvas.lift(estacao_VCD)
    canvas.lift(estacao_CZD)
    canvas.lift(estacao_MOB)
    canvas.lift(l5_icon)
    canvas.lift(l9_icon)

    # Define os nomes das estações
    nome_JAP = canvas.create_text(x1+8, y1-13, text="Washington Luís",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CGN = canvas.create_text(x2+8, y2-13, text="Aeroporto de Congonhas",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_BPA = canvas.create_text(x3+8, y3-13, text="Brooklin Paulista",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VJD = canvas.create_text(x4+8, y4-13, text="Vereador José Diniz",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CBM = canvas.create_text(x5+8, y5-13, text="Campo Belo",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VCD = canvas.create_text(x6+8, y6-13, text="Vila Cordeiro",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CZD = canvas.create_text(x7+8, y7-13, text="Chucri Zaidan",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_MOB = canvas.create_text(x8+8, y8-13, text="Morumbi",
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