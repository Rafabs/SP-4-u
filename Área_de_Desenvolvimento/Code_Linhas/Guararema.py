import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import *  # Importa todas as classes e funções do módulo tkinter
from PIL import Image, ImageTk  # Importa classes para manipular imagens
from colorama import Fore, Back, Style, init  # Importa classes para cores de console
from datetime import datetime  # Importa a classe datetime para trabalhar com datas e horas

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def guararema():
    # Imprime o texto formatado com informações sobre o início do mapa da Linha GUARAREMA
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da LINHA GUARAREMA iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")     
    # Cria uma nova janela
    root = tk.Toplevel()
    root.title("Linha GUARAREMA")  # Define o título da janela
    root.geometry("1920x1080")  # Define as dimensões da janela

    # Define o ícone da janela
    canvas = tk.Canvas(root, width=1920, height=1080)  # Cria um canvas na janela
    canvas.pack()  # Empacota o canvas na janela

    # Carrega uma imagem para o ícone da janela
    image = Image.open('Mapa_dos_Trilhos\\Favicon\\ABPF_LOGO.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone da janela
    root.iconphoto(False, photo)

    # Carrega o logotipo da ABPF
    metro_logo = Image.open("Mapa_dos_Trilhos\\Imgs\\ABPF_LOGO.jpg")
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
    x1, y1 = 960, 750
    x2, y2 = 1010, 750

    # Desenha as estações no canvas
    estacao_GUARAREMA = canvas.create_text(
        x1-5, y1+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)
    estacao_LUIS_CARLOS = canvas.create_text(
        x2-5, y2+8, text="●", font="Helvetica 36 bold", anchor="w", fill=branco)

    # Desenha a linha que conecta as estações
    linha = canvas.create_line(
        x1-10, y1+12, x2+25, y2+12, fill='#f8e71c', width=30)

    # Sobrepõe as estações sobre a linha
    canvas.lift(estacao_GUARAREMA)
    canvas.lift(estacao_LUIS_CARLOS)

    # Define as Estações
    nome_GUARAREMA = canvas.create_text(x1+8, y1-13, text="Guararema",
                                        font="Helvetica 12", anchor="w", angle=60)
    nome_LUIS_CARLOS = canvas.create_text(x2+8, y2-13, text="Luis Carlos",
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