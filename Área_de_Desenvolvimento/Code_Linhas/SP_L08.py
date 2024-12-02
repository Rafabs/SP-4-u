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
    item_spacing = 55

    ############## LEGENDA - INÍCIO ##############

    # Adiciona a linha de separação
    canvas.create_line(0, 740, 1920, 740, fill="#000000", width=1)
    canvas.create_line(0, 1060, 1920, 1060, fill="#000000", width=1)

    # Adiciona o texto "Legenda"
    canvas.create_text(5, 715, text="Legenda", font="Helvetica 14 ", anchor="nw", fill="#000000")

    # Adiciona o texto "Subtitle"
    canvas.create_text(90, 718, text="Subtitle", font="Helvetica 13 italic bold", anchor="nw", fill="#686868")

    # Adiciona o texto "Informações úteis"
    canvas.create_text(1375, 745, text="Informações úteis", font="Helvetica 14 ", anchor="nw", fill="#000000")

    # Adiciona o texto "Useful Information"
    canvas.create_text(1535, 748, text="Useful Information", font="Helvetica 12 italic bold", anchor="nw", fill="#686868")

    load_image("Mapa_dos_Trilhos/Icons/1.png", 20, 760, 25, 25, canvas, images)
    canvas.create_text(45, 745, text="Linha 1 • Azul", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(45, 760, text="Line 1-Blue", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(400, 760, text="METRÔ", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(0, 780, 400, 780, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/2.png", 20, 800, 25, 25, canvas, images)
    canvas.create_text(45, 785, text="Linha 2 • Verde", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(45, 800, text="Line 2-Green", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(400, 800, text="METRÔ", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(0, 820, 400, 820, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/3.png", 20, 840, 25, 25, canvas, images)
    canvas.create_text(45, 825, text="Linha 3 • Vermelha", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(45, 840, text="Line 3-Red", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(400, 840, text="METRÔ", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(0, 860, 400, 860, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/4.png", 20, 880, 25, 25, canvas, images)
    canvas.create_text(45, 865, text="Linha 4 • Amarela", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(45, 880, text="Line 4-Yellow", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(400, 880, text="VIQUATRO", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(0, 900, 400, 900, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/5.png", 20, 920, 25, 25, canvas, images)
    canvas.create_text(45, 905, text="Linha 5 • Lilás", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(45, 920, text="Line 5-Lilac", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(400, 920, text="VIAMOBILIDADE", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(0, 940, 400, 940, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/7.png", 20, 960, 25, 25, canvas, images)
    canvas.create_text(45, 945, text="Linha 7 • Rubi", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(45, 960, text="Line 7-Ruby", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(400, 960, text="CPTM", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(0, 980, 400, 980, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/8.png", 20, 1000, 25, 25, canvas, images)
    canvas.create_text(45, 985, text="Linha 8 • Diamante", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(45, 1000, text="Line 8-Diamond", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(400, 1000, text="VIAMOBILIDADE", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(0, 1020, 400, 1020, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/9.png", 20, 1040, 25, 25, canvas, images)
    canvas.create_text(45, 1025, text="Linha 9 • Esmeralda", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(45, 1040, text="Line 9-Emerald", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(400, 1040, text="VIAMOBILIDADE", font="Helvetica 13", anchor="e", fill="#000000")

    load_image("Mapa_dos_Trilhos/Icons/10.png", 450, 760, 25, 25, canvas, images)
    canvas.create_text(475, 745, text="Linha 10 • Turquesa", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(475, 760, text="Line 10-Turquoise", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(830, 760, text="CPTM", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(430, 780, 830, 780, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/11.png", 450, 800, 25, 25, canvas, images)
    canvas.create_text(475, 785, text="Linha 11 • Coral", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(475, 800, text="Line 11-Coral", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(830, 800, text="CPTM", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(430, 820, 830, 820, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/12.png", 450, 840, 25, 25, canvas, images)
    canvas.create_text(475, 825, text="Linha 12 • Safira", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(475, 840, text="Line 12-Sapphire", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(830, 840, text="CPTM", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(430, 860, 830, 860, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/13.png", 450, 880, 25, 25, canvas, images)
    canvas.create_text(475, 865, text="Linha 13 • Jade", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(475, 880, text="Line 13-Jade", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(830, 880, text="CPTM", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(430, 900, 830, 900, fill="#000000", width=1)
    
    load_image("Mapa_dos_Trilhos/Icons/15.png", 450, 920, 25, 25, canvas, images)
    canvas.create_text(475, 905, text="Linha 15 • Prata", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(475, 920, text="Line 15-Silver", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(830, 920, text="METRÔ", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(430, 940, 830, 940, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/A.png", 880, 760, 25, 25, canvas, images)
    canvas.create_text(905, 745, text="Corredor São Mateus-Jabaquara", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(905, 760, text="São Mateus-Jabaquara Corridor", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(1260, 760, text="EMTU", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(860, 780, 1260, 780, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/B.png", 880, 800, 25, 25, canvas, images)
    canvas.create_text(905, 785, text="Corredor Guarulhos-SP", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(905, 800, text="Guarulhos-SP Corridor", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(1260, 800, text="EMTU", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(860, 820, 1260, 820, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/C.png", 880, 840, 25, 25, canvas, images)
    canvas.create_text(905, 825, text="Corredor Itapevi-SP", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(905, 840, text="Itapevi-SP Corridor", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(1260, 840, text="EMTU", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(860, 860, 1260, 860, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/terminal_onibus.png", 880, 880, 25, 25, canvas, images)
    canvas.create_text(905, 865, text="Terminal Rodoviário", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(905, 880, text="Long Distance Bus Terminal", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_line(860, 900, 1260, 900, fill="#000000", width=1)
    
    load_image("Mapa_dos_Trilhos/Icons/aeroporto_GRU.png", 880, 920, 25, 25, canvas, images)
    canvas.create_text(905, 905, text="Aeroporto", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(905, 920, text="Airport", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_line(860, 940, 1260, 940, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/zoo.png", 880, 960, 25, 25, canvas, images)
    canvas.create_text(905, 945, text="Ponte Orca ao Zoológico", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(905, 960, text="Orca Shuttle to the Zoo", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(1260, 960, text="EMTU", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(860, 980, 1260, 980, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/onibus_emtu.png", 880, 1000, 25, 25, canvas, images)
    canvas.create_text(905, 985, text="Terminal de Ônibus Integrado", font="Helvetica 12 bold", anchor="nw", fill="#000000")
    canvas.create_text(905, 1000, text="Integrated Bus Terminal", font="Helvetica 10 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(1260, 1000, text="EMTU", font="Helvetica 13", anchor="e", fill="#000000")
    canvas.create_line(860, 1020, 1260, 1020, fill="#000000", width=1)

    canvas.create_text(1375, 789, text="CPTM", font="Helvetica 14", anchor="nw", fill="#000000")
    canvas.create_text(1540, 789, text="www.cptm.sp.gov.br", font="Helvetica 14", anchor="nw", fill="#000000")
    canvas.create_text(1910, 800, text="0800 055 0121", font="Helvetica 14 bold", anchor="e", fill="#000000")
    canvas.create_line(1375, 780, 1910, 780, fill="#000000", width=1)

    canvas.create_text(1375, 829, text="EMTU", font="Helvetica 14", anchor="nw", fill="#000000")
    canvas.create_text(1540, 829, text="www.emtu.sp.gov.br", font="Helvetica 14", anchor="nw", fill="#000000")
    canvas.create_text(1910, 840, text="0800 724 0555", font="Helvetica 14 bold", anchor="e", fill="#000000")
    canvas.create_line(1375, 820, 1910, 820, fill="#000000", width=1)

    canvas.create_text(1375, 869, text="METRÔ", font="Helvetica 14", anchor="nw", fill="#000000")
    canvas.create_text(1540, 869, text="www.metro.sp.gov.br", font="Helvetica 14", anchor="nw", fill="#000000")
    canvas.create_text(1910, 880, text="0800 770 7722", font="Helvetica 14 bold", anchor="e", fill="#000000")
    canvas.create_line(1375, 860, 1910, 860, fill="#000000", width=1)

    canvas.create_text(1375, 909, text="VIAQUATRO", font="Helvetica 14", anchor="nw", fill="#000000")
    canvas.create_text(1540, 909, text="www.viaquatro.com.br", font="Helvetica 14", anchor="nw", fill="#000000")
    canvas.create_text(1910, 920, text="0800 770 7100", font="Helvetica 14 bold", anchor="e", fill="#000000")
    canvas.create_line(1375, 900, 1910, 900, fill="#000000", width=1)
    
    canvas.create_text(1375, 949, text="VIAMOBILIDADE", font="Helvetica 14", anchor="nw", fill="#000000")
    canvas.create_text(1540, 949, text="www.viamobilidade.com.br", font="Helvetica 14", anchor="nw", fill="#000000")
    canvas.create_text(1910, 960, text="0800 770 7106", font="Helvetica 14 bold", anchor="e", fill="#000000")
    canvas.create_line(1375, 940, 1910, 940, fill="#000000", width=1)
    canvas.create_line(1375, 980, 1910, 980, fill="#000000", width=1)

    load_image("Mapa_dos_Trilhos/Icons/Cptm_logo_completo.png", 1427, 1000, 106, 31, canvas, images)
    load_image("Mapa_dos_Trilhos/Icons/EMTU_logo.png", 1650, 1000, 106, 31, canvas, images)
    load_image("Mapa_dos_Trilhos/Icons/Sao_Paulo_Metro_Logo.png", 1850, 1000, 126, 41, canvas, images)
    load_image("Mapa_dos_Trilhos/Icons/qr_code.png", 1397, 1040, 40, 40, canvas, images)
    canvas.create_text(1430, 1020, text="Utilize o código ao lado para obter a versão mais atual deste mapa. Consulte nos sites das empresas", font="Helvetica 7 bold", anchor="nw", fill="#000000")
    canvas.create_text(1430, 1030, text="os horários de funcionamento das estações e transferências entre linhas e outros conteúdos.", font="Helvetica 7 bold", anchor="nw", fill="#000000")
    canvas.create_text(1430, 1040, text="Please use the QR Code to get the latest version of this map. Address the websites of the metropolitan", font="Helvetica 7 italic bold", anchor="nw", fill="#686868")
    canvas.create_text(1430, 1050, text="transport companies for stations service hours, line interchange information and other contents.", font="Helvetica 7 italic bold", anchor="nw", fill="#686868")# INSERIR QR CODE
    ############## LEGENDA - FIM ##############
    
    for i, trajeto in enumerate(trajeto_list):
        x_position = canvas_center_x + (i - total_items // 2) * item_spacing
        y_position = 420

        if isinstance(trajeto, dict):
            primary = trajeto.get("primary", "")
            secondary = trajeto.get("secondary", "")
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
            ball = canvas.create_oval(
                x_position - 10, y_position + 20, x_position + 10, y_position + 40, 
                fill="#FFFFFF", outline="#FFFFFF"
            )
            canvas.lift(ball)
            for image_path in image_paths:
                if image_path and os.path.exists(image_path):
                    load_image(image_path, x_position, y_position + 70, 30, 30, canvas, images)
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