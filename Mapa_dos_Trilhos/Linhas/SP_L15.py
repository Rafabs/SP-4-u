import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import *  # Importa todas as classes e funções do módulo tkinter
from PIL import Image, ImageTk  # Importa classes para manipular imagens
from colorama import Fore, Back, Style, init  # Importa classes para cores de console
from datetime import datetime  # Importa a classe datetime para trabalhar com datas e horas

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def line15():
    # Imprime o texto formatado com informações sobre o início do mapa da Linha 15 - Prata
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA 15 - PRATA iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Criando a janela
    root = tk.Toplevel()
    root.title("Linha 15 - Prata") # Define o título da janela
    root.geometry("1920x1080")  # Define as dimensões da janela

    # Define o ícone da janela
    canvas = tk.Canvas(root, width=1920, height=1080)  # Cria um canvas na janela
    canvas.pack()  # Empacota o canvas na janela

    # Carrega uma imagem para o ícone da janela
    image = Image.open('Mapa dos Trilhos\\Favicon\\15_prata.ico')
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
    x1, y1 = 710, 750
    x2, y2 = 760, 750
    x3, y3 = 810, 750
    x4, y4 = 860, 750
    x5, y5 = 910, 750
    x6, y6 = 960, 750
    x7, y7 = 1010, 750
    x8, y8 = 1060, 750
    x9, y9 = 1110, 750
    x10, y10 = 1160, 750
    x11, y11 = 1210, 750

    # Desenha as estações no canvas
    estacao_VPM = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ORT = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SLU = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_CDD = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VTL = canvas.create_text(
        x5-5, y5+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_VUN = canvas.create_text(
        x6-5, y6+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_JPL = canvas.create_text(
        x7-5, y7+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SAP = canvas.create_text(
        x8-5, y8+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_FJT = canvas.create_text(
        x9-5, y9+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_MAT = canvas.create_text(
        x10-5, y10+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_IGT = canvas.create_text(
        x11-5, y11+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Inserindo as transferências

    # VILA PRUDENTE
    linha2_verde_icon = canvas.create_text(
        x1-3, y1+40, text="●", font="Helvetica 32", anchor="w", fill=verde)
    l2_icon = canvas.create_text(
        x1+6, y1+42, text="2", font="Helvetica 10 bold", anchor="w", fill=branco)

    # Desenha a linha que conecta as estações
    linha = canvas.create_line(
        x1-10, y1+12, x11+25, y11+12, fill=prata, width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_VPM)
    canvas.lift(estacao_ORT)
    canvas.lift(estacao_SLU)
    canvas.lift(estacao_CDD)
    canvas.lift(estacao_VTL)
    canvas.lift(estacao_VUN)
    canvas.lift(estacao_JPL)
    canvas.lift(estacao_SAP)
    canvas.lift(estacao_FJT)
    canvas.lift(estacao_MAT)
    canvas.lift(estacao_IGT)
    canvas.lift(l2_icon)

    # Define os nomes das estações
    nome_VPM = canvas.create_text(x1+8, y1-13, text="Vila Prudente",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_ORT = canvas.create_text(x2+8, y2-13, text="Oratório",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SLU = canvas.create_text(x3+8, y3-13, text="São Lucas",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_CDD = canvas.create_text(x4+8, y4-13, text="Camilo Haddad",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VTL = canvas.create_text(x5+8, y5-13, text="Vila Tolstói",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_VUN = canvas.create_text(x6+8, y6-13, text="Vila União",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_JPL = canvas.create_text(x7+8, y7-13, text="Jardim Planalto",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_SAP = canvas.create_text(x8+8, y8-13, text="Sapopemba",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_FJT = canvas.create_text(x9+8, y9-13, text="Fazenda da Juta",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_MAT = canvas.create_text(x10+8, y10-13, text="São Mateus",
                                  font="Helvetica 12", anchor="w", angle=60)
    nome_IGT = canvas.create_text(x11+8, y11-13, text="Jardim Colonial",
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