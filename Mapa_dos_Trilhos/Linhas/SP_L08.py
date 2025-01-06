import os
import json
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import locale
from temperatura import get_weather
from screeninfo import get_monitors
import subprocess

# Função para registrar a execução de comandos
def line_command(description):
    print(f"Abrindo Mapa - {description}")
    
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

with open('Mapa_dos_Trilhos/Linhas/subtitle.json', 'r', encoding='utf-8') as file:
    lines_data = json.load(file)
   
def get_destino_linha(script_name):
    dados = dados_linhas.get(script_name, {})
    destino = dados.get('DESTINO', 'DESTINO DESCONHECIDO')
    linha = dados.get('LINHA', '0000/00')
    trajeto = dados.get('TRAJETO', [])
    # Obtém a cor da linha, com um padrão branco se não existir
    cor_linha = dados.get('COR_LINHA', '#000000')
    # Obtém o caminho do logo, ou None se não existir
    logo_operador = dados.get('LOGO', None)
    operadora = dados.get('OPERADORA', None)
    return destino, linha, trajeto, cor_linha, logo_operador, operadora

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

'''
# Função para ajustar tamanho com parâmetro
def ajustar_tamanho(escala):
    return
'''

# INSERIR TRECHO ABAIXO ANTES DE >>>script_name = os.path.basename(__file__)
'''
    # Adicionando os botões na janela
    button_width = 5  # Largura fixa para todos os botões
    button_height = 1  # Altura fixa para todos os botões
    button_style = {
        "bg": "#D3D3D3",  # Cor de fundo azul
        "fg": "#000000",    # Cor do texto branco
        "font": ("Arial", 10, "bold"),  # Fonte Arial, tamanho 10, negrito
        "relief": "raised",  # Borda elevada
        "bd": 1.5,  # Largura da borda
    }

    button_25 = tk.Button(root, text="25%", command=lambda: ajustar_tamanho(0.25), width=button_width, height=button_height, **button_style)
    button_50 = tk.Button(root, text="50%", command=lambda: ajustar_tamanho(0.50), width=button_width, height=button_height, **button_style)
    button_75 = tk.Button(root, text="75%", command=lambda: ajustar_tamanho(0.75), width=button_width, height=button_height, **button_style)
    button_100 = tk.Button(root, text="100%", command=lambda: ajustar_tamanho(1), width=button_width, height=button_height, **button_style)

    # Posicionando os botões
    button_25.place(x=777, y=30)
    button_50.place(x=822, y=30)
    button_75.place(x=867, y=30)
    button_100.place(x=912, y=30)
'''

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
    destino_text, linha_text, trajeto_list, cor_linha, logo_operador, operadora = get_destino_linha(
        script_name)

    canvas.create_rectangle(0, 0, 1920, 60, fill="#000000", outline="#000000")
    canvas.create_rectangle(
        0, 60, 1920, 180, fill=cor_linha, outline=cor_linha)

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

    if logo_operador and os.path.exists(logo_operador):
        images = []  # Lista para armazenar as referências de imagem
        # Ajuste de posição e tamanho do logo
        load_image(logo_operador, 30, 37, 25, 25, canvas, images)

    # Exibir as informações do trajeto na horizontal, inclinadas em 60°
    canvas_center_x = 960
    total_items = len(trajeto_list)
    item_spacing = 55

    for line in lines_data["lines"]:
        if isinstance(line, list):  # Verifica se o item é uma lista
            for sub_item in line:  # Percorre cada sub-item da lista
                if sub_item.get("type") == "oval":  # Verifica se o tipo é oval
                    canvas.create_oval(
                        sub_item["position"]["x1"], sub_item["position"]["y1"],
                        sub_item["position"]["x2"], sub_item["position"]["y2"],
                        fill=sub_item["fill"], outline=sub_item["outline"]
                    )
                elif sub_item.get("type") == "text":  # Verifica se o tipo é texto
                    canvas.create_text(
                        sub_item["position"]["x"], sub_item["position"]["y"],
                        text=sub_item["text"], font=sub_item["font"],
                        anchor=sub_item["anchor"], fill=sub_item["color"]
                    )
                else:
                    print(f"Tipo inesperado: {sub_item}")
        
        elif "line" in line:
            # Processamento para linhas de separação
            canvas.create_line(
                line["line"]["x1"], line["line"]["y1"],
                line["line"]["x2"], line["line"]["y2"],
                fill=line["line"]["color"], width=line["line"]["width"]
            )
        
        elif "texts" in line:
            # Processamento de textos
            for text in line["texts"]:
                canvas.create_text(
                    text["position"]["x"], text["position"]["y"],
                    text=text["text"], font=text["font"],
                    anchor=text["anchor"], fill=text["color"]
                )
        
        elif "icon" in line:
            # Processamento de imagens
            load_image(
                line["icon"], line["coordinates"]["x"], line["coordinates"]["y"],
                line["size"]["width"], line["size"]["height"], canvas, images
            )
        
        else:
            print(f"Item inesperado: {line}")

    for i, trajeto in enumerate(trajeto_list):
        x_position = canvas_center_x + (i - total_items // 2) * item_spacing
        y_position = 420

        if isinstance(trajeto, dict):
            primary = trajeto.get("primary", "")
            secondary = trajeto.get("secondary", "")
            free_access = trajeto.get("free_access", False)
            bold_secondary = trajeto.get("bold_secondary", False)
            image_paths = [
                trajeto.get("image"),
                trajeto.get("image_1"),
                trajeto.get("image_2"),
                trajeto.get("image_3"),
                trajeto.get("image_4"),
                trajeto.get("image_5"),
            ]

            # Renderiza a estação com `primary` e `secondary`
            if primary and secondary:
                if bold_secondary:
                    # Renderiza `secondary` maior
                    canvas.create_text(
                        x_position, y_position, text=secondary,
                        font="Helvetica 20", angle=60, anchor="w"
                    )
                    # Renderiza `primary` menor
                    canvas.create_text(
                        x_position - 23, y_position, text=primary,
                        font="Helvetica 14", angle=60, anchor="w"
                    )
                else:
                    # Renderiza `primary` maior
                    canvas.create_text(
                        x_position, y_position, text=primary,
                        font="Helvetica 20", angle=60, anchor="w"
                    )
                    # Renderiza `secondary` menor
                    canvas.create_text(
                        x_position + 23, y_position, text=secondary,
                        font="Helvetica 14", angle=60, anchor="w"
                    )

            elif primary:  # Apenas `primary`
                canvas.create_text(
                    x_position, y_position, text=primary,
                    font="Helvetica 20", angle=60, anchor="w"
                )
            elif secondary:  # Apenas `secondary`
                canvas.create_text(
                    x_position, y_position, text=secondary,
                    font="Helvetica 20", angle=60, anchor="w"
                )

            # Desenha os círculos e imagens
            rect = canvas.create_rectangle(
                x_position - 20, y_position + 15, x_position + 40, y_position + 50,
                fill=cor_linha, outline=cor_linha
            )
            # Preto se `free_access`, caso contrário Branco
            ball_color = "#000000" if free_access else "#FFFFFF"
            ball_color_outline = "#000000"
            ball = canvas.create_oval(
                x_position - 10, y_position + 20, x_position + 10, y_position + 40,
                fill=ball_color, outline=ball_color_outline
            )
            canvas.lift(ball)
            for image_path in image_paths:
                if image_path and os.path.exists(image_path):
                    load_image(image_path, x_position, y_position +
                               70, 30, 30, canvas, images)
                    y_position += 40
        else:
            # Renderiza itens simples
            canvas.create_text(
                x_position, y_position, text=trajeto,
                font="Helvetica 20", angle=60, anchor="w"
            )
            rect = canvas.create_rectangle(
                x_position - 20, y_position + 15, x_position + 40, y_position + 50,
                fill=cor_linha, outline=cor_linha
            )
            ball = canvas.create_oval(
                x_position - 10, y_position + 20, x_position + 10, y_position + 40,
                fill="#FFFFFF", outline="#FFFFFF"
            )

    # Funções para atualizar temperatura, data e alternar imagens
    def atualizar_temperatura():
        global temperatura
        temperatura = get_weather()
        canvas.itemconfigure(
            linha1, text=f"| {hora} | São Paulo | {temperatura}")
        root.after(1000, atualizar_temperatura)

    def atualizar_data_hora():
        global hora, dia_semana, data_completa
        hora = datetime.now().strftime("%H:%M")
        dia_semana = datetime.now().strftime("%A")
        data_completa = data_extenso()
        canvas.itemconfigure(
            linha1, text=f"| {hora} | São Paulo | {temperatura}")
        canvas.itemconfigure(linha2, text=f"{dia_semana}, {data_completa}")
        root.after(1000, atualizar_data_hora)

    def alternar_imagens(index=1):
        if index > 6:
            index = 1

        # Define o caminho da imagem com base na operadora
        if operadora == "METRÔ":
            image_path = f"Mapa_dos_Trilhos/Imgs/METRÔ/{index}.png"
        elif operadora == "CPTM":
            image_path = f"Mapa_dos_Trilhos/Imgs/CPTM/{index}.png"
        elif operadora == "VIAQUATRO":
            image_path = f"Mapa_dos_Trilhos/Imgs/VIAQUATRO/{index}.png"
        elif operadora == "VIAMOBILIDADE_L5":
            image_path = f"Mapa_dos_Trilhos/Imgs/VIAMOBILIDADE_L5/{index}.png"
        elif operadora == "VIAMOBILIDADE_L8":
            image_path = f"Mapa_dos_Trilhos/Imgs/VIAMOBILIDADE_L8/{index}.png"
        elif operadora == "VIAMOBILIDADE_L9":
            image_path = f"Mapa_dos_Trilhos/Imgs/VIAMOBILIDADE_L9/{index}.png"                                                
        else:
            print(f"Operadora desconhecida: {operadora}")
            return  # Sai da função se a operadora for desconhecida

        # Carrega a imagem no canvas
        if os.path.exists(image_path):
            load_image(image_path, 1440, 90, 960, 180, canvas, images)
        else:
            print(f"Imagem não encontrada: {image_path}")            
        root.after(10000, alternar_imagens, index + 1)

    root.after(0, atualizar_temperatura)
    root.after(0, atualizar_data_hora)
    root.after(0, alternar_imagens)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    mapa_linha()