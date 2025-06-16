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
from temperatura import get_weather
from screeninfo import get_monitors
import subprocess
import logging
from pathlib import Path

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
    except locale.Error:
        print("Não foi possível configurar o locale para português brasileiro. Usando padrão do sistema.")
        locale.setlocale(locale.LC_ALL, '')

# Configuração do logger
logging.basicConfig(filename='Mapa_dos_Trilhos/log.txt', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def line7():
    try:
        # Obtém o caminho absoluto do interpretador Python atual
        python_exe = sys.executable
        script_path = Path(__file__).resolve()
        
        print(f"Iniciando linha 7 com: {python_exe} {script_path}")
        
        # Verifica se o arquivo existe
        if not script_path.exists():
            raise FileNotFoundError(f"Arquivo da linha 7 não encontrado: {script_path}")
        
        # Executa o próprio script
        import subprocess
        subprocess.run([python_exe, str(script_path)], check=True)
        
    except Exception as e:
        print(f"Erro ao abrir linha 7: {str(e)}")
        logging.error(f"Erro em line7: {str(e)}")
        raise

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
    cor_linha = dados.get('COR_LINHA', '#000000')
    logo_operador = dados.get('LOGO', None)
    operadora = dados.get('OPERADORA', None)
    return destino, linha, trajeto, cor_linha, logo_operador, operadora

class MapaLinhaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linha 7 - Rubi")
        self.setWindowIcon(QIcon('Mapa_dos_Trilhos/Favicon/7_rubi.ico'))
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
        
        # Informações de temperatura e hora
        self.temperatura = get_weather()
        self.hora = datetime.now().strftime("%H:%M")
        self.dia_semana = datetime.now().strftime("%A")
        self.data_completa = self.data_extenso()
        
        self.linha1_text = self.scene.addText(f"| {self.hora} | São Paulo | {self.temperatura}")
        self.linha1_text.setDefaultTextColor(QColor("#FFFFFF"))
        self.linha1_text.setFont(QFont("Helvetica", 24))
        self.linha1_text.setPos(50, 10)
        
        self.linha2_text = self.scene.addText(f"{self.dia_semana}, {self.data_completa}")
        self.linha2_text.setDefaultTextColor(QColor("#FFFFFF"))
        self.linha2_text.setFont(QFont("Helvetica", 24))
        self.linha2_text.setPos(20, 50)
        
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
        
    def data_extenso(self):
        now = datetime.now()
        return now.strftime("%d de %B de %Y")
    
    def load_image(self, image_path, x, y, width, height):
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((width, height), Image.LANCZOS)
            
            # Convert PIL Image to QImage
            img = img.convert("RGBA")
            data = img.tobytes("raw", "RGBA")
            qimg = QImage(data, img.size[0], img.size[1], QImage.Format_RGBA8888)
            
            pixmap = QPixmap.fromImage(qimg)
            pixmap_item = QGraphicsPixmapItem(pixmap)
            pixmap_item.setPos(x - width/2, y - height/2)  # Centraliza a imagem
            self.scene.addItem(pixmap_item)
            self.images.append(pixmap_item)  # Mantém referência
            
            return pixmap_item
        else:
            print(f"Imagem não encontrada: {image_path}")
            return None
    
    def process_lines_data(self):
        for line in lines_data["lines"]:
            if isinstance(line, list):
                for sub_item in line:
                    if sub_item.get("type") == "oval":
                        ellipse = QGraphicsEllipseItem(
                            sub_item["position"]["x1"], sub_item["position"]["y1"],
                            sub_item["position"]["x2"] - sub_item["position"]["x1"],
                            sub_item["position"]["y2"] - sub_item["position"]["y1"]
                        )
                        ellipse.setBrush(QColor(sub_item["fill"]))
                        ellipse.setPen(QColor(sub_item["outline"]))
                        self.scene.addItem(ellipse)
                    
                    elif sub_item.get("type") == "text":
                        text = QGraphicsTextItem(sub_item["text"])
                        text.setDefaultTextColor(QColor(sub_item["color"]))
                        
                        # Processa a fonte (ex: "Helvetica 12" -> QFont("Helvetica", 12))
                        font_parts = sub_item["font"].split()
                        font_name = font_parts[0]
                        font_size = int(font_parts[1]) if len(font_parts) > 1 else 12
                        text.setFont(QFont(font_name, font_size))
                        
                        # Ajuste de posição com base na âncora
                        x = sub_item["position"]["x"]
                        y = sub_item["position"]["y"]
                        anchor = sub_item.get("anchor", "nw")  # Padrão: northwest
                        
                        # Ajusta a posição baseado na âncora
                        rect = text.boundingRect()
                        if "center" in anchor:
                            x -= rect.width() / 2
                        elif "e" in anchor:
                            x -= rect.width()
                        if "center" in anchor:
                            y -= rect.height() / 2
                        elif "s" in anchor:
                            y -= rect.height()
                        
                        text.setPos(x, y)
                        self.scene.addItem(text)
            
            elif "line" in line:
                line_item = QGraphicsLineItem(
                    line["line"]["x1"], line["line"]["y1"],
                    line["line"]["x2"], line["line"]["y2"]
                )
                line_item.setPen(QColor(line["line"]["color"]))
                line_item.setZValue(1)  # Garante que a linha fique acima de outros elementos
                self.scene.addItem(line_item)

            elif "text_blocks" in line:  # Novo tipo para blocos de texto com quebra automática
                for block in line["text_blocks"]:
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
                    text_item.setTextWidth(block.get("width", 400))  # Largura máxima para quebra de linha
                    text_item.setPos(block["position"]["x"], block["position"]["y"])
                    self.scene.addItem(text_item)

            elif "texts" in line:
                for text in line["texts"]:
                    text_item = QGraphicsTextItem(text["text"])
                    text_item.setDefaultTextColor(QColor(text["color"]))
                    
                    # Processamento da fonte
                    font_parts = text["font"].split()
                    font_name = font_parts[0]
                    font_size = int(font_parts[1]) if len(font_parts) > 1 else 12
                    font = QFont(font_name, font_size)
                    
                    # Verifica se tem estilo (bold/italic)
                    if "bold" in text["font"].lower():
                        font.setBold(True)
                    if "italic" in text["font"].lower():
                        font.setItalic(True)
                    
                    text_item.setFont(font)
                    
                    # Posição base
                    x = text["position"]["x"]
                    y = text["position"]["y"]
                    
                    # Ajuste especial para operadoras (METRÔ, CPTM, etc.)
                    if any(op in text["text"] for op in ["METRÔ", "CPTM", "EMTU", "VIAQUATRO", "VIAMOBILIDADE"]):
                        y += -15  # Desce o texto para ficar abaixo da linha
                    
                    # Ajuste especial para última coluna (telefones)
                    if x > 1800:  # Itens muito à direita
                        x -= 0  # Move para a esquerda
                    
                    # No bloco de textos, adicione este caso especial:
                    if "0800" in text["text"]:  # Detecta os textos de telefone
                        x = text["position"]["x"] + 20  # Move significativamente para esquerda
                        text_item.setPos(x, y)

                    # Tratamento da âncora
                    anchor = text.get("anchor", "nw")
                    rect = text_item.boundingRect()
                    
                    if "center" in anchor:
                        x -= rect.width() / 2
                    elif "e" in anchor:  # anchor = 'e' (leste/direita)
                        x -= rect.width()
                    
                    if "center" in anchor:
                        y -= rect.height() / 2
                    elif "s" in anchor:  # anchor = 's' (sul/baixo)
                        y -= rect.height()
                    
                    text_item.setPos(x, y)
                    self.scene.addItem(text_item)
            
            elif "icon" in line:
                self.load_image(
                    line["icon"], 
                    line["coordinates"]["x"], 
                    line["coordinates"]["y"],
                    line["size"]["width"], 
                    line["size"]["height"]
                )
    
    def process_trajeto(self):
        canvas_center_x = 960
        total_items = len(self.trajeto_list)
        item_spacing = 55
        
        for i, trajeto in enumerate(self.trajeto_list):
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
                
                # Renderiza a estação
                if primary and secondary:
                    if bold_secondary:
                        # Secondary maior
                        text = QGraphicsTextItem(secondary)
                        text.setDefaultTextColor(QColor("#000000"))
                        text.setFont(QFont("Helvetica", 20))
                        text.setPos(x_position - 23, y_position - 6)
                        transform = QTransform().rotate(-60)
                        text.setTransform(transform)
                        self.scene.addItem(text)
                        
                        # Primary menor
                        text = QGraphicsTextItem(primary)
                        text.setDefaultTextColor(QColor("#000000"))
                        text.setFont(QFont("Helvetica", 14))
                        text.setPos(x_position - 43, y_position - 6)
                        transform = QTransform().rotate(-60)
                        text.setTransform(transform)
                        self.scene.addItem(text)
                    else:
                        # Primary maior
                        text = QGraphicsTextItem(primary)
                        text.setDefaultTextColor(QColor("#000000"))
                        text.setFont(QFont("Helvetica", 20))
                        text.setPos(x_position - 23, y_position - 6)
                        transform = QTransform().rotate(-60)
                        text.setTransform(transform)
                        self.scene.addItem(text)
                        
                        # Secondary menor
                        text = QGraphicsTextItem(secondary)
                        text.setDefaultTextColor(QColor("#000000"))
                        text.setFont(QFont("helvetica", 14))
                        text.setPos(x_position + 8, y_position - 6)
                        transform = QTransform().rotate(-60)
                        text.setTransform(transform)
                        self.scene.addItem(text)
                
                elif primary:
                    text = QGraphicsTextItem(primary)
                    text.setDefaultTextColor(QColor("#000000"))
                    text.setFont(QFont("Helvetica", 20))
                    text.setPos(x_position - 23, y_position - 6)
                    transform = QTransform().rotate(-60)
                    text.setTransform(transform)
                    self.scene.addItem(text)
                
                elif secondary:
                    text = QGraphicsTextItem(secondary)
                    text.setDefaultTextColor(QColor("#000000"))
                    text.setFont(QFont("Helvetica", 20))
                    text.setPos(x_position - 23, y_position - 6)
                    transform = QTransform().rotate(-60)
                    text.setTransform(transform)
                    self.scene.addItem(text)
                
                # Retângulo e círculo
                rect = QGraphicsRectItem(x_position - 20, y_position + 15, 60, 35)
                rect.setBrush(QColor(self.cor_linha))
                rect.setPen(QColor(self.cor_linha))
                self.scene.addItem(rect)
                
                ball_color = QColor("#000000") if free_access else QColor("#FFFFFF")
                ball = QGraphicsEllipseItem(x_position - 10, y_position + 20, 20, 20)
                ball.setBrush(ball_color)
                ball.setPen(QColor("#000000"))
                self.scene.addItem(ball)
                
                # Imagens adicionais
                for image_path in image_paths:
                    if image_path and os.path.exists(image_path):
                        self.load_image(image_path, x_position, y_position + 70, 30, 30)
                        y_position += 40
            
            else:
                # Item simples
                text = QGraphicsTextItem(trajeto)
                text.setDefaultTextColor(QColor("#000000"))
                text.setFont(QFont("Helvetica", 20))
                text.setPos(x_position - 23, y_position)
                transform = QTransform().rotate(-60)
                text.setTransform(transform)
                self.scene.addItem(text)
                
                rect = QGraphicsRectItem(x_position - 20, y_position + 15, 60, 35)
                rect.setBrush(QColor(self.cor_linha))
                rect.setPen(QColor(self.cor_linha))
                self.scene.addItem(rect)
                
                ball = QGraphicsEllipseItem(x_position - 10, y_position + 20, 20, 20)
                ball.setBrush(QColor("#FFFFFF"))
                ball.setPen(QColor("#FFFFFF"))
                self.scene.addItem(ball)
    
    def setup_timers(self):
        # Timer para atualizar temperatura
        self.temp_timer = QTimer()
        self.temp_timer.timeout.connect(self.atualizar_temperatura)
        self.temp_timer.start(1000)
        
        # Timer para atualizar data/hora
        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self.atualizar_data_hora)
        self.clock_timer.start(1000)
        
        # Timer para alternar imagens
        self.image_timer = QTimer()
        self.image_timer.timeout.connect(self.alternar_imagens)
        self.image_timer.start(10000)
        self.current_image_index = 1
    
    def atualizar_temperatura(self):
        self.temperatura = get_weather()
        self.linha1_text.setPlainText(f"| {self.hora} | São Paulo | {self.temperatura}")
    
    def atualizar_data_hora(self):
        self.hora = datetime.now().strftime("%H:%M")
        self.dia_semana = datetime.now().strftime("%A")
        self.data_completa = self.data_extenso()
        self.linha1_text.setPlainText(f"| {self.hora} | São Paulo | {self.temperatura}")
        self.linha2_text.setPlainText(f"{self.dia_semana}, {self.data_completa}")
    
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
            print(f"Operadora desconhecida: {self.operadora}")
            return
        
        if os.path.exists(image_path):
            self.load_image(image_path, 1440, 90, 960, 180)
        else:
            print(f"Imagem não encontrada: {image_path}")
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            logging.info(f"Fechando Linha 7 - Rubi")
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapaLinhaWindow()
    window.show()
    sys.exit(app.exec_())