import os
import json
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import locale
from temperatura import get_weather
from screeninfo import get_monitors
import subprocess

# Função para executar o script SP_L01.py
def line4():
    try:
        subprocess.run(["python", "Mapa_dos_Trilhos\\Linhas\\SP_L04.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script: {e}")
        
# Define o local para o idioma português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

# Carrega os dados do arquivo JSON
with open('Mapa_dos_Trilhos/Linhas/trajeto.json', 'r', encoding='utf-8') as file:
    dados_linhas = json.load(file)

def get_destino_linha(script_name):
    dados = dados_linhas.get(script_name, {})
    destino = dados.get('DESTINO', 'DESTINO DESCONHECIDO')
    linha = dados.get('LINHA', '0000/00')
    trajeto = dados.get('TRAJETO', [])
    cor_linha = dados.get('COR_LINHA', '#000000')  # Obtém a cor da linha, com um padrão branco se não existir
    return destino, linha, trajeto, cor_linha

def mapa_linha():
    root = tk.Toplevel()
    # Obtém as dimensões da tela do monitor
    monitor = get_monitors()[0]
    screen_width = monitor.width
    screen_height = monitor.height
    root.geometry(f"{screen_width}x{screen_height}")  # Define as dimensões da janela
    root.attributes("-fullscreen", True)  # Deixa a janela em tela cheia
    root.overrideredirect(True)  # Remove os botões de fechar, maximizar, minimizar
    root.title("Linha 4 - Amarela") # Define o título da janela

    def sair(event=None):
        root.destroy()

    root.bind("<Escape>", sair)  # Associa a tecla Esc ao fechamento da janela

    canvas = tk.Canvas(root, width=1920, height=1080)  # Cria um canvas na janela
    canvas.pack()  # Empacota o canvas na janela

    # Cores de background
    preto = "#000000"
    azul = "#0455A1"
    cinza = "#D3D3D3"  

    # Adiciona um retângulo cinza que cobre toda a tela
    canvas.create_rectangle(0, 0, 1920, 1080, fill=cinza, outline=cinza)

    # Obtém os dados de DESTINO, LINHA e TRAJETO para o script atual
    script_name = os.path.basename(__file__)
    destino_text, linha_text, trajeto_list, cor_linha = get_destino_linha(script_name)

    # Adiciona faixas azuis atrás dos textos, ocupando toda a largura da tela
    canvas.create_rectangle(0, 0, 1920, 180, fill=cor_linha, outline=cor_linha)  

    # Função para obter a data em formato extenso
    def data_extenso():
        now = datetime.now()
        return now.strftime("%d de %B de %Y")

    # Inicializa as variáveis para temperatura e data/hora
    temperatura = get_weather()
    hora = datetime.now().strftime("%H:%M")
    dia_semana = datetime.now().strftime("%A")
    data_completa = data_extenso()

    linha1 = canvas.create_text(
        20, 20, text=f"{hora} | São Paulo | {temperatura}", font="Helvetica 24", anchor="nw", fill=preto)
    linha2 = canvas.create_text(
        20, 60, text=f"{dia_semana}, {data_completa}", font="Helvetica 24", anchor="nw", fill=preto)
    destino = canvas.create_text(
        20, 100, text=f"DESTINO: {destino_text}", font="Helvetica 24 bold", anchor="nw", fill=preto)
    linha = canvas.create_text(
        20, 140, text=f"LINHA: {linha_text}", font="Helvetica 24 bold", anchor="nw", fill=preto)

    # Exibir as informações do trajeto na horizontal, inclinadas em 60°
    canvas_center_x = 960
    total_items = len(trajeto_list)
    item_spacing = 50  # Espaçamento entre os itens do trajeto

    images = []  # Lista para manter referências das imagens

    for i, trajeto in enumerate(trajeto_list):
        x_position = canvas_center_x + (i - total_items // 2) * item_spacing
        y_position = 750

        if isinstance(trajeto, dict):
            text = trajeto.get("text", "")
            image_paths = [
                trajeto.get("image"),
                trajeto.get("image_1"),
                trajeto.get("image_2"),
                trajeto.get("image_3"),
                trajeto.get("image_4"),
            ]  # Lista de caminhos das imagens

            if text:
                canvas.create_text(x_position, y_position, text=text, font="Helvetica 24", angle=60, anchor="w")
                y_position += 30

            # Adicionar retângulo colorido abaixo das bolinhas
            rect = canvas.create_rectangle(x_position - 20, y_position + 15, x_position + 40, y_position + 50, fill=cor_linha, outline=cor_linha)

            # Exibir a bolinha branca acima do retângulo
            ball = canvas.create_oval(x_position - 10, y_position + 20, x_position + 10, y_position + 40, fill="#FFFFFF", outline="#FFFFFF")
            canvas.lift(ball)  # Levanta a bolinha branca acima de todos os outros objetos

            # Exibir as imagens abaixo da bolinha branca
            for image_path in image_paths:
                if image_path and os.path.exists(image_path):
                    img = Image.open(image_path)
                    img = img.resize((30, 30), Image.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    images.append(photo)  # Armazena a referência da imagem na lista
                    canvas.create_image(x_position, y_position + 70, image=photo, anchor="c")
                    y_position += 40  # Ajusta a posição `y` para a próxima imagem
                else:
                    print(f"Imagem não encontrada: {image_path}")
        else:
            canvas.create_text(x_position, y_position, text=trajeto, font="Helvetica 24", angle=60, anchor="w")
            y_position += 30
            # Adicionar retângulo colorido abaixo das bolinhas
            rect = canvas.create_rectangle(x_position - 20, y_position + 15, x_position + 40, y_position + 50, fill=cor_linha, outline=cor_linha)

            # Exibir a bolinha branca acima do retângulo
            ball = canvas.create_oval(x_position - 10, y_position + 20, x_position + 10, y_position + 40, fill="#FFFFFF", outline="#FFFFFF")
            canvas.lift(ball)  # Levanta a bolinha branca acima de todos os outros objetos


    def load_image(image_path, x, y, width, height):
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((width, height), Image.LANCZOS)  # Redimensiona a imagem
            photo = ImageTk.PhotoImage(img)
            images.append(photo)  # Armazena a referência da imagem na lista
            canvas.create_image(x, y, image=photo, anchor="center")  # Adiciona a imagem ao canvas
        else:
            print(f"Imagem não encontrada: {image_path}")

    # Função para atualizar a temperatura
    def atualizar_temperatura():
        global temperatura
        temperatura = get_weather()
        canvas.itemconfigure(linha1, text=f"{hora} | São Paulo | {temperatura}")
        root.after(1000, atualizar_temperatura)  # Atualiza a temperatura a cada 1 segundo

    # Função para atualizar a data e hora
    def atualizar_data_hora():
        global hora, dia_semana, data_completa
        hora = datetime.now().strftime("%H:%M")
        dia_semana = datetime.now().strftime("%A")
        data_completa = data_extenso()
        canvas.itemconfigure(linha1, text=f"{hora} | São Paulo | {temperatura}")
        canvas.itemconfigure(linha2, text=f"{dia_semana}, {data_completa}")
        root.after(1000, atualizar_data_hora)  # Atualiza a data e hora a cada 1 segundo

    # Função para alternar as imagens
    def alternar_imagens(index=1):
        if index > 6:
            index = 1
        image_path = f"Mapa_dos_Trilhos/Imgs/{index}.png"
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((960, 180), Image.LANCZOS)  # Redimensiona a imagem para cobrir a faixa azul
            photo = ImageTk.PhotoImage(img)
            images.append(photo)  # Armazena a referência da imagem na lista
            canvas.create_image(1440, 90, image=photo, anchor="center")  # Adiciona a imagem ao canvas
        else:
            print(f"Imagem não encontrada: {image_path}")
        root.after(60000, alternar_imagens, index + 1)  # Alterna a imagem a cada 1 minuto

    # Inicie os loops principais do Tkinter para temperatura, data/hora e alternar imagens
    def atualizar_temperatura_wrapper():
        atualizar_temperatura()

    def atualizar_data_hora_wrapper():
        atualizar_data_hora()

    root.after(0, atualizar_temperatura_wrapper)  # Inicia a atualização da temperatura
    root.after(0, atualizar_data_hora_wrapper)    # Inicia a atualização da data e hora
    root.after(0, alternar_imagens)               # Inicia a alternância de imagens

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    mapa_linha()