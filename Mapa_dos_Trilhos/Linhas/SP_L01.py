# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte público Metropolitano do Estado de São Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "22/07/2025 16:40"

DESCRITIVO:
MÃ³dulo de funcionalidades especÃ­ficas
ARQUITETURA:
    Mapa_dos_Trilhos/Linhas/SP_L01.py
"""
import os
import json
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                            QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, 
                            QVBoxLayout, QGraphicsRectItem, QGraphicsEllipseItem,
                            QGraphicsTextItem, QGraphicsLineItem)
from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor, QFont, QTransform, QIcon
from PyQt5.QtCore import Qt, QTimer, QRectF, QPointF
from PIL import Image
from datetime import datetime
import locale
from Mapa_dos_Trilhos.temperatura import get_weather
from screeninfo import get_monitors
import subprocess
import logging
from pathlib import Path
from Mapa_dos_Trilhos.utils.status_manager import StatusManager

# Get the absolute path to the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
    
from Mapa_dos_Trilhos.utils.logger_config import configurar_logger
configurar_logger()

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
    except locale.Error:
        print("Não foi possível configurar o locale para português brasileiro. Usando padrão do sistema.")
        locale.setlocale(locale.LC_ALL, '')

def line1():
    try:
        # Obtém o caminho absoluto do script
        script_path = Path(__file__).resolve()
        
        # Configura o ambiente Python corretamente
        env = os.environ.copy()
        env["PYTHONPATH"] = str(script_path.parent.parent.parent) + os.pathsep + env.get("PYTHONPATH", "")
        
        print(f"Executando linha 1: {sys.executable} {script_path}")
        
        # Executa o script em um novo processo
        result = subprocess.run(
            [sys.executable, str(script_path)],
            check=True,
            env=env,
            cwd=str(script_path.parent.parent.parent),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        print("Linha 1 executada com sucesso!")
        return True
        
    except subprocess.CalledProcessError as e:
        error_msg = f"Erro ao executar linha 1:\n{e.stderr}"
        print(error_msg)
        logging.error(error_msg)
        return False
    except Exception as e:
        error_msg = f"Erro inesperado em line1: {str(e)}"
        print(error_msg)
        logging.error(error_msg)
        return False

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

base_path = os.path.dirname(os.path.abspath(__file__))

# Caminhos absolutos para os arquivos JSON
trajeto_path = os.path.join(base_path, 'trajeto.json')
subtitle_path = os.path.join(base_path, 'subtitle.json')

# Carrega os dados do arquivo trajeto.json
with open(trajeto_path, 'r', encoding='utf-8') as file:
    dados_linhas = json.load(file)

# Carrega os dados do arquivo subtitle.json
with open(subtitle_path, 'r', encoding='utf-8') as file:
    lines_data = json.load(file)
    
def get_destino_linha(script_name):
    dados = dados_linhas.get(script_name, {})
    destino = dados.get('DESTINO', 'DESTINO DESCONHECIDO')
    linha = dados.get('LINHA', '0000/00')
    trajeto = dados.get('TRAJETO', [])
    cor_linha = dados.get('COR_LINHA', '#000000')
    logo_operador = dados.get('LOGO', None)
    operadora = dados.get('OPERADORA', None)
    return destino, linha, trajeto, cor_linha, logo_operador, operadora

class MapaLinhaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status_manager = StatusManager()
        self.setWindowTitle("Linha 1 - Azul")
        self.setWindowIcon(QIcon('Mapa_dos_Trilhos/Favicon/1_azul.ico'))
        self.setWindowFlags(Qt.FramelessWindowHint)

        monitor = get_monitors()[0]
        self.setGeometry(0, 0, monitor.width, monitor.height)
        self.setWindowState(Qt.WindowFullScreen)
        self.screen_width = monitor.width
        self.screen_height = monitor.height
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.view)
        
        self.images = []
        
        self.script_name = os.path.basename(__file__)
        self.destino_text, self.linha_text, self.trajeto_list, self.cor_linha, self.logo_operador, self.operadora = get_destino_linha(
            self.script_name)
        
        self.setup_ui()
        self.setup_timers()
        
    def setup_ui(self):
        # Fundo cinza
        self.scene.setBackgroundBrush(QColor("#D3D3D3"))
        
        # Cabeçalho preto
        header = QGraphicsRectItem(0, 0, 1920, 60)
        header.setBrush(QColor("#000000"))
        header.setPen(QColor("#000000"))
        self.scene.addItem(header)
        
        # Barra colorida
        color_bar = QGraphicsRectItem(0, 60, 1920, 120)
        color_bar.setBrush(QColor(self.cor_linha))
        color_bar.setPen(QColor(self.cor_linha))
        self.scene.addItem(color_bar)
        
        # Informações de temperatura, hora e status
        self.temperatura = get_weather()
        self.hora = datetime.now().strftime("%H:%M")
        self.dia_semana = datetime.now().strftime("%A")
        self.data_completa = self.data_extenso()
        self.status_linha = self.status_manager.get_line_status("Linha 1 - Azul")
        
        # Cria os elementos de texto
        self.create_header_texts()
        
        # Destino e linha
        destino_text = self.scene.addText(f"DESTINO: {self.destino_text}")
        destino_text.setDefaultTextColor(QColor("#FFFFFF"))
        destino_text.setFont(QFont("Helvetica", 24, QFont.Bold))
        destino_text.setPos(20, 90)
        
        linha_text = self.scene.addText(f"LINHA: {self.linha_text}")
        linha_text.setDefaultTextColor(QColor("#FFFFFF"))
        linha_text.setFont(QFont("Helvetica", 24, QFont.Bold))
        linha_text.setPos(20, 130)
        
        # Logo do operador
        if self.logo_operador and os.path.exists(self.logo_operador):
            self.load_image(self.logo_operador, 30, 37, 25, 25)
        
        # Processa os dados do subtitle.json
        self.process_lines_data()
        
        # Processa o trajeto
        self.process_trajeto()

    def create_header_texts(self):
        """Cria os textos do cabeçalho com formatação condicional"""
        # Texto de hora e localização
        # Obtém os dados completos
        weather_data = get_weather()
        
        if isinstance(weather_data, tuple) and len(weather_data) > 0:
            full_text = weather_data[0]  # Pega o texto completo
            # Extrai apenas o valor numérico da temperatura
            temp_part = full_text.split('|')[0]  # Pega a parte antes do primeiro |
            temperatura = temp_part.replace('🌡', '').strip()  # Remove o emoji e espaços
        else:
            temperatura = "N/D"  # Caso de falha
        
        self.temperatura = temperatura        
        self.time_text = self.scene.addText(f"| {self.hora} | São Paulo | {self.temperatura} | ")
        self.time_text.setDefaultTextColor(QColor("#FFFFFF"))
        self.time_text.setFont(QFont("Helvetica", 24))
        self.time_text.setPos(50, 10)
        
        # Texto de status com cor condicional
        self.status_text = self.scene.addText(f"{self.status_linha}")
        self.status_text.setDefaultTextColor(self._get_status_color(self.status_linha))
        self.status_text.setFont(QFont("Helvetica", 24, QFont.Bold))
        status_x = 50 + self.time_text.boundingRect().width()
        self.status_text.setPos(status_x, 10)
        
        # Data completa
        self.date_text = self.scene.addText(f"{self.dia_semana}, {self.data_completa}")
        self.date_text.setDefaultTextColor(QColor("#FFFFFF"))
        self.date_text.setFont(QFont("Helvetica", 24))
        self.date_text.setPos(20, 50)
    
    def _get_status_color(self, status):
        """Retorna a cor apropriada para o status"""
        if "Operação Normal" in status:
            return QColor("#00AA00")  # Verde
        elif any(word in status for word in ["Paralisada", "Interrompida", "Encerrada"]):
            return QColor("#FF0000")  # Vermelho
        elif any(word in status for word in ["Velocidade reduzida", "Operação parcial", "Operação com Impacto Pontual", "Atividade Programada"]):
            return QColor("#E5FF00")  # Amarelo
        return QColor("#FFFFFF")  # Branco (padrão)
    
    def data_extenso(self):
        now = datetime.now()
        return now.strftime("%d de %B de %Y")
    
    def load_image(self, image_path, x, y, width, height):
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((width, height), Image.LANCZOS)
            
            img = img.convert("RGBA")
            data = img.tobytes("raw", "RGBA")
            qimg = QImage(data, img.size[0], img.size[1], QImage.Format_RGBA8888)
            
            pixmap = QPixmap.fromImage(qimg)
            pixmap_item = QGraphicsPixmapItem(pixmap)
            pixmap_item.setPos(x - width/2, y - height/2)
            self.scene.addItem(pixmap_item)
            self.images.append(pixmap_item)
            
            return pixmap_item
        return None
    
    def process_lines_data(self):
        for line in lines_data["lines"]:
            if isinstance(line, list):
                for sub_item in line:
                    self.process_line_item(sub_item)
            elif "line" in line:
                self.create_line_item(line["line"])
            elif "text_blocks" in line:
                for block in line["text_blocks"]:
                    self.create_text_block(block)
            elif "texts" in line:
                for text in line["texts"]:
                    self.create_text_item(text)
            elif "icon" in line:
                self.load_image(
                    line["icon"], 
                    line["coordinates"]["x"], 
                    line["coordinates"]["y"],
                    line["size"]["width"], 
                    line["size"]["height"]
                )
    
    def process_line_item(self, item):
        if item.get("type") == "oval":
            self.create_oval_item(item)
        elif item.get("type") == "text":
            self.create_text_item(item)
    
    def create_oval_item(self, item):
        ellipse = QGraphicsEllipseItem(
            item["position"]["x1"], item["position"]["y1"],
            item["position"]["x2"] - item["position"]["x1"],
            item["position"]["y2"] - item["position"]["y1"]
        )
        ellipse.setBrush(QColor(item["fill"]))
        ellipse.setPen(QColor(item["outline"]))
        self.scene.addItem(ellipse)
    
    def create_line_item(self, line):
        line_item = QGraphicsLineItem(
            line["x1"], line["y1"],
            line["x2"], line["y2"]
        )
        line_item.setPen(QColor(line["color"]))
        line_item.setZValue(1)
        self.scene.addItem(line_item)
    
    def create_text_block(self, block):
        text_item = QGraphicsTextItem(block["text"])
        text_item.setDefaultTextColor(QColor(block["color"]))
        
        font_parts = block["font"].split()
        font_name = font_parts[0]
        font_size = int(font_parts[1]) if len(font_parts) > 1 else 12
        font = QFont(font_name, font_size)
        
        if "bold" in block["font"].lower():
            font.setBold(True)
        if "italic" in block["font"].lower():
            font.setItalic(True)
            
        text_item.setFont(font)
        text_item.setTextWidth(block.get("width", 400))
        text_item.setPos(block["position"]["x"], block["position"]["y"])
        self.scene.addItem(text_item)
    
    def create_text_item(self, text):
        text_item = QGraphicsTextItem(text["text"])
        text_item.setDefaultTextColor(QColor(text["color"]))
        
        font_parts = text["font"].split()
        font_name = font_parts[0]
        font_size = int(font_parts[1]) if len(font_parts) > 1 else 12
        font = QFont(font_name, font_size)
        
        if "bold" in text["font"].lower():
            font.setBold(True)
        if "italic" in text["font"].lower():
            font.setItalic(True)
        
        text_item.setFont(font)
        
        x = text["position"]["x"]
        y = text["position"]["y"]
        
        if any(op in text["text"] for op in ["METRÔ", "CPTM", "EMTU", "VIAQUATRO", "VIAMOBILIDADE"]):
            y += -15
        
        if x > 1800:
            x -= 0
        
        if "0800" in text["text"]:
            x = text["position"]["x"] + 20

        anchor = text.get("anchor", "nw")
        rect = text_item.boundingRect()
        
        if "center" in anchor:
            x -= rect.width() / 2
        elif "e" in anchor:
            x -= rect.width()
        
        if "center" in anchor:
            y -= rect.height() / 2
        elif "s" in anchor:
            y -= rect.height()
        
        text_item.setPos(x, y)
        self.scene.addItem(text_item)
    
    def process_trajeto(self):
        canvas_center_x = 960
        total_items = len(self.trajeto_list)
        item_spacing = 55
        
        for i, trajeto in enumerate(self.trajeto_list):
            x_position = canvas_center_x + (i - total_items // 2) * item_spacing
            y_position = 420
            
            if isinstance(trajeto, dict):
                self.create_station_item(trajeto, x_position, y_position)
            else:
                self.create_simple_item(trajeto, x_position, y_position)
    
    def create_station_item(self, trajeto, x, y):
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
        
        if primary and secondary:
            if bold_secondary:
                self.create_rotated_text(secondary, x - 23, y - 6, 20)
                self.create_rotated_text(primary, x - 43, y - 6, 14)
            else:
                self.create_rotated_text(primary, x - 23, y - 6, 20)
                self.create_rotated_text(secondary, x + 8, y - 6, 14)
        elif primary:
            self.create_rotated_text(primary, x - 23, y - 6, 20)
        elif secondary:
            self.create_rotated_text(secondary, x - 23, y - 6, 20)
        
        # Retângulo e círculo
        rect = QGraphicsRectItem(x - 20, y + 15, 60, 35)
        rect.setBrush(QColor(self.cor_linha))
        rect.setPen(QColor(self.cor_linha))
        self.scene.addItem(rect)
        
        ball_color = QColor("#000000") if free_access else QColor("#FFFFFF")
        ball = QGraphicsEllipseItem(x - 10, y + 20, 20, 20)
        ball.setBrush(ball_color)
        ball.setPen(QColor("#000000"))
        self.scene.addItem(ball)
        
        # Imagens adicionais
        for image_path in image_paths:
            if image_path and os.path.exists(image_path):
                self.load_image(image_path, x, y + 70, 30, 30)
                y += 40
    
    def create_rotated_text(self, text, x, y, size):
        text_item = QGraphicsTextItem(text)
        text_item.setDefaultTextColor(QColor("#000000"))
        text_item.setFont(QFont("Helvetica", size))
        text_item.setPos(x, y)
        transform = QTransform().rotate(-60)
        text_item.setTransform(transform)
        self.scene.addItem(text_item)
    
    def create_simple_item(self, text, x, y):
        self.create_rotated_text(text, x - 23, y, 20)
        
        rect = QGraphicsRectItem(x - 20, y + 15, 60, 35)
        rect.setBrush(QColor(self.cor_linha))
        rect.setPen(QColor(self.cor_linha))
        self.scene.addItem(rect)
        
        ball = QGraphicsEllipseItem(x - 10, y + 20, 20, 20)
        ball.setBrush(QColor("#FFFFFF"))
        ball.setPen(QColor("#FFFFFF"))
        self.scene.addItem(ball)
    
    def setup_timers(self):
        # Timer para atualizar informações
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_display)
        self.update_timer.start(60000)  # Atualiza a cada minuto
        
        # Timer para alternar imagens
        self.image_timer = QTimer()
        self.image_timer.timeout.connect(self.alternar_imagens)
        self.image_timer.start(10000)
        self.current_image_index = 1
    
    def update_display(self):
        """Atualiza todas as informações dinâmicas"""
        # Atualiza temperatura e status
        self.temperatura = get_weather()
        self.status_linha = self.status_manager.get_line_status("Linha 1 - Azul")
        
        # Atualiza hora e data
        self.hora = datetime.now().strftime("%H:%M")
        self.dia_semana = datetime.now().strftime("%A")
        self.data_completa = self.data_extenso()
        
        # Atualiza os textos
        self.time_text.setPlainText(f"| {self.hora} | São Paulo | {self.temperatura} | ")
        self.status_text.setPlainText(f"{self.status_linha}")
        self.status_text.setDefaultTextColor(self._get_status_color(self.status_linha))
        self.date_text.setPlainText(f"{self.dia_semana}, {self.data_completa}")
        
        # Reposiciona o status_text caso o tamanho do time_text tenha mudado
        status_x = 50 + self.time_text.boundingRect().width()
        self.status_text.setPos(status_x, 10)
    
    def alternar_imagens(self):
        self.current_image_index += 1
        if self.current_image_index > 6:
            self.current_image_index = 1
        
        if self.operadora == "METRÔ":
            image_path = f"Mapa_dos_Trilhos/Imgs/METRÔ/{self.current_image_index}.png"
        elif self.operadora == "CPTM":
            image_path = f"Mapa_dos_Trilhos/Imgs/CPTM/{self.current_image_index}.png"
        elif self.operadora == "VIAQUATRO":
            image_path = f"Mapa_dos_Trilhos/Imgs/VIAQUATRO/{self.current_image_index}.png"
        elif self.operadora == "VIAMOBILIDADE_L5":
            image_path = f"Mapa_dos_Trilhos/Imgs/VIAMOBILIDADE_L5/{self.current_image_index}.png"
        elif self.operadora == "VIAMOBILIDADE_L8":
            image_path = f"Mapa_dos_Trilhos/Imgs/VIAMOBILIDADE_L8/{self.current_image_index}.png"
        elif self.operadora == "VIAMOBILIDADE_L9":
            image_path = f"Mapa_dos_Trilhos/Imgs/VIAMOBILIDADE_L9/{self.current_image_index}.png"                                                
        else:
            return
        
        if os.path.exists(image_path):
            self.load_image(image_path, 1440, 90, 960, 180)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            with open('Mapa_dos_Trilhos/log.log', 'a', encoding='utf-8') as f:
                f.write(f"{datetime.now()} - Fechando Linha 1 - Azul\n")
            self.close()

def main():
    app = QApplication(sys.argv)
    window = MapaLinhaWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()