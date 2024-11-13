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
def line8():
    try:
        subprocess.run(["python", "Mapa_dos_Trilhos\\Linhas\\SP_L08.py"], check=True)
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

# Função para carregar imagens
def load_image(image_path, x, y, width, height, canvas, images):
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((width, height), Image.LANCZOS)  # Redimensiona a imagem
        photo = ImageTk.PhotoImage(img)
        images.append(photo)  # Armazena a referência da imagem na lista
        canvas.create_image(x, y, image=photo, anchor="center")  # Adiciona a imagem ao canvas
    else:
        print(f"Imagem não encontrada: {image_path}")

def mapa_linha():
    root = tk.Toplevel()
    monitor = get_monitors()[0]
    screen_width = monitor.width
    screen_height = monitor.height
    root.geometry(f"{screen_width}x{screen_height}")
    root.attributes("-fullscreen", True)
    root.overrideredirect(True)
    root.title("Linha 8 - Diamante")

    def sair(event=None):
        root.destroy()

    root.bind("<Escape>", sair)

    canvas = tk.Canvas(root, width=1920, height=1080)
    canvas.pack()

    cinza = "#D3D3D3"
    canvas.create_rectangle(0, 0, 1920, 1080, fill=cinza, outline=cinza)

    script_name = os.path.basename(__file__)
    destino_text, linha_text, trajeto_list, cor_linha = get_destino_linha(script_name)

    canvas.create_rectangle(0, 0, 1920, 60, fill="#000000", outline="#000000")
    canvas.create_rectangle(0, 60, 1920, 180, fill=cor_linha, outline=cor_linha)
    
    def data_extenso():
        now = datetime.now()
        return now.strftime("%d de %B de %Y")

    # Inicializa as variáveis para temperatura e data/hora
    temperatura = get_weather()
    hora = datetime.now().strftime("%H:%M")
    dia_semana = datetime.now().strftime("%A")
    data_completa = data_extenso()

    linha1 = canvas.create_text(
        50, 20, text=f"| {hora} | São Paulo | {temperatura}", font="Helvetica 24", anchor="nw", fill="#FFFFFF")
    linha2 = canvas.create_text(
        20, 60, text=f"{dia_semana}, {data_completa}", font="Helvetica 24", anchor="nw", fill="#FFFFFF")
    destino = canvas.create_text(
        20, 100, text=f"DESTINO: {destino_text}", font="Helvetica 24 bold", anchor="nw", fill="#FFFFFF")
    linha = canvas.create_text(
        20, 140, text=f"LINHA: {linha_text}", font="Helvetica 24 bold", anchor="nw", fill="#FFFFFF")

    images = []  # Lista para manter referências das imagens
    load_image("Mapa_dos_Trilhos/Icons/8_diamante.png", 30, 37, 25, 25, canvas, images)

    # Exibir as informações do trajeto na horizontal, inclinadas em 60°
    canvas_center_x = 960
    total_items = len(trajeto_list)
    item_spacing = 50

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
                trajeto.get("image_5"),
            ]

            if text:
                canvas.create_text(x_position, y_position, text=text, font="Helvetica 24", angle=60, anchor="w")
                y_position += 5

            rect = canvas.create_rectangle(x_position - 20, y_position + 15, x_position + 40, y_position + 50, fill=cor_linha, outline=cor_linha)
            ball = canvas.create_oval(x_position - 10, y_position + 20, x_position + 10, y_position + 40, fill="#FFFFFF", outline="#FFFFFF")
            canvas.lift(ball)

            for image_path in image_paths:
                if image_path and os.path.exists(image_path):
                    load_image(image_path, x_position, y_position + 70, 30, 30, canvas, images)
                    y_position += 40
        else:
            canvas.create_text(x_position, y_position, text=trajeto, font="Helvetica 24", angle=60, anchor="w")
            y_position += 5
            rect = canvas.create_rectangle(x_position - 20, y_position + 15, x_position + 40, y_position + 50, fill=cor_linha, outline=cor_linha)
            ball = canvas.create_oval(x_position - 10, y_position + 20, x_position + 10, y_position + 40, fill="#FFFFFF", outline="#FFFFFF")

    # Funções para atualizar temperatura, data e alternar imagens
    def atualizar_temperatura():
        global temperatura
        temperatura = get_weather()
        canvas.itemconfigure(linha1, text=f"| {hora} | São Paulo | {temperatura}")
        root.after(1000, atualizar_temperatura)

    def atualizar_data_hora():
        global hora, dia_semana, data_completa
        hora = datetime.now().strftime("%H:%M")
        dia_semana = datetime.now().strftime("%A")
        data_completa = data_extenso()
        canvas.itemconfigure(linha1, text=f"| {hora} | São Paulo | {temperatura}")
        canvas.itemconfigure(linha2, text=f"{dia_semana}, {data_completa}")
        root.after(1000, atualizar_data_hora)

    def alternar_imagens(index=1):
        if index > 6:
            index = 1
        image_path = f"Mapa_dos_Trilhos/Imgs/{index}.png"
        load_image(image_path, 1440, 90, 960, 180, canvas, images)
        root.after(60000, alternar_imagens, index + 1)

    root.after(0, atualizar_temperatura)
    root.after(0, atualizar_data_hora)
    root.after(0, alternar_imagens)

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    mapa_linha()