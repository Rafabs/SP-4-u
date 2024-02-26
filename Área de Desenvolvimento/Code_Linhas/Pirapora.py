import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import *  # Importa todas as classes e funções do módulo tkinter
from PIL import Image, ImageTk  # Importa classes para manipular imagens
from colorama import Fore, Back, Style, init  # Importa classes para cores de console
from datetime import datetime  # Importa a classe datetime para trabalhar com datas e horas

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def pirapora():
    # Imprime o texto formatado com informações sobre o início do mapa da Linha Pirapora
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA PIRAPORA iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Cria uma nova janela
    root = tk.Toplevel()
    root.title("Estrada de Ferro Perus-Pirapora (IFPPC)")  # Define o título da janela
    root.geometry("1920x1080")  # Define as dimensões da janela

    # Define o ícone da janela
    canvas = tk.Canvas(root, width=1920, height=1080)  # Cria um canvas na janela
    canvas.pack()  # Empacota o canvas na janela

    # Carrega uma imagem para o ícone da janela
    image = Image.open('Mapa dos Trilhos\\Favicon\\IFPPC_LOGO.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone da janela
    root.iconphoto(False, photo)

    # Carrega o logotipo da IFPPC
    metro_logo = Image.open("Mapa dos Trilhos\\Imgs\\IFPPC_LOGO.jpg")
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
    x1, y1 = 910, 750
    x2, y2 = 960, 750
    x3, y3 = 1010, 750
    x4, y4 = 1060, 750

    # Desenha as estações no canvas
    estacao_MINERAL = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_ECOLOGIA = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_SANTA_FE = canvas.create_text(
        x3-5, y3+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_NATURA = canvas.create_text(
        x4-5, y4+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Desenha a linha que conecta as estações
    linha = canvas.create_line(
        x1-10, y1+12, x4+25, y4+12, fill='#7ed321', width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_MINERAL)
    canvas.lift(estacao_ECOLOGIA)
    canvas.lift(estacao_SANTA_FE)
    canvas.lift(estacao_NATURA)

    # Define os nomes das estações
    nome_MINERAL = canvas.create_text(x1+8, y1-13, text="Mineral",
                                      font="Helvetica 12", anchor="w", angle=60)
    nome_ECOLOGIA = canvas.create_text(x2+8, y2-13, text="Ecologia",
                                       font="Helvetica 12", anchor="w", angle=60)
    nome_SANTA_FE = canvas.create_text(x3+8, y3-13, text="Santa Fé",
                                       font="Helvetica 12", anchor="w", angle=60)
    nome_NATURA = canvas.create_text(x4+8, y4-13, text="Natura",
                                     font="Helvetica 12", anchor="w", angle=60)

    # Cria um texto na parte inferior da tela indicando a autoria e data de desenvolvimento
    dev = canvas.create_text(
        960, 900, text="⚡Desenvolvido por RAFAEL BARBOSA - 15/09/2023 | Revisado em 15/09/2023", font="Helvetica 12", anchor="c")

    # Loop principal para atualizar a janela
    while True:
        root.update()
        try:
            root.update()
        except TclError:
            break # Sai do loop caso ocorra um erro