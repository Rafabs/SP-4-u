import requests
from io import BytesIO
import json
import sys
import os
import platform
import tempfile
import atexit
import webbrowser
import re
import locale
import difflib
import csv
from pathlib import Path
from datetime import datetime
from PIL import Image
from colorama import Fore, Back, Style, init
import logging
from screeninfo import get_monitors
import traceback

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    logging.critical(f"Exceção não tratada:\n{tb}")
    QMessageBox.critical(None, "Erro", f"Exceção não tratada:\n{str(exc_value)}")
    QApplication.quit()

sys.excepthook = excepthook

# Configurações de caminho
sys.path.extend([
    r'Mapa_dos_Trilhos',
    r'Mapa_dos_Trilhos\\Linhas',
    r'Mapa_dos_Trilhos\\Qualidade_ar',
    r'Mapa_dos_Trilhos\\Sobre'
])

# PyQt5 imports
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QScrollArea, QFrame, QGroupBox, QGraphicsEllipseItem,
    QGraphicsTextItem, QGraphicsLineItem, QSplitter, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtGui import QPixmap, QIcon, QFont, QColor, QPainter, QImage

# Módulos personalizados
from SP_L17 import line17
from SP_L15 import line15
from SP_L13 import line13
from SP_L12 import line12
from SP_L11 import line11
from SP_L10 import line10
from SP_L09 import line9
from SP_L08 import line8
from SP_L07 import line7
from SP_L06 import line6
from SP_L05 import line5
from SP_L04 import line4
from SP_L03 import line3
from SP_L02 import line2
from SP_L01 import line1
from noticia import notice_transp_sao_paulo
from varredura import verificacao
from Pesquisa_pass.pesquisa_pass import passageiro_estacao
from mapa import mapa_global
from gtfs_emtu import emtu
from gtfs_sptrans import sptrans
from temperatura import get_weather
from Guias.guias import *
from qualidade_ar import mapa_qualidade_ar

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
    except locale.Error:
        print("Não foi possível configurar o locale para português brasileiro. Usando padrão do sistema.")
        locale.setlocale(locale.LC_ALL, '')

init()

def log_close_time():
    logging.info(f"{'=' * 30} PROGRAMA FECHADO {'=' * 30}")

atexit.register(log_close_time)

def dados_usuario():
    """Coleta e exibe informações do sistema"""
    hora_atual = datetime.now().strftime("%d/%m/%Y | %H:%M:%S")
    print(f"=" * 30, "INFORMAÇÕES DO USUÁRIO", "=" * 30)
    print(hora_atual)
    
    info = {
        'Sistema Operacional': (os.name, platform.system()),
        'Diretório Atual': os.getcwd(),
        'Usuário': os.getlogin(),
        'Versão do SO': platform.version(),
        'Arquitetura': platform.machine(),
        'Python': platform.python_version(),
        'Processador': platform.processor(),
        'Temp Dir': tempfile.gettempdir(),
        'Home Dir': os.path.expanduser("~")
    }
    
    for key, value in info.items():
        print(f'<<<{key}>>> {value}')
    
    print("=" * 90)

class StreamToLogger:
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            if self.log_level == logging.WARNING:
                self.logger.warning(line.rstrip())
            elif self.log_level == logging.DEBUG:
                self.logger.debug(line.rstrip())
            elif self.log_level == logging.CRITICAL:
                self.logger.critical(line.rstrip())
            else:
                self.logger.info(line.rstrip())

    def flush(self):
        pass

logging.basicConfig(filename='Mapa_dos_Trilhos\\log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

sys.stdout = StreamToLogger(logging.getLogger('STDOUT'), logging.INFO)
sys.stderr = StreamToLogger(logging.getLogger('STDERR'), logging.ERROR)

dados_usuario()

with open(r'Mapa_dos_Trilhos/Linhas/subtitle.json', 'r', encoding='utf-8') as file:
    lines_data = json.load(file)

def abrir_link(url):
    url = re.sub(r'/[^/]*$', '', url)
    webbrowser.open_new(url)

def fazer_varredura():
    itens_arquivos = verificacao()

class NewsWidget(QWidget):
    def __init__(self, title, link, image_url=None, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QWidget {
                background-color: #444444;
                border-radius: 8px;
                padding: 5px;
            }
        """)
        
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(10)  # 🔹 Maior espaçamento entre imagem e texto

        # 🔹 Título da notícia com efeito hover e ícone de link
        self.title_label = QLabel(f"🔗 {title}")  # 🔹 Ícone indicador de link
        self.title_label.setStyleSheet("""
            QLabel {
                color: white;
                font: bold 12pt Arial;
                text-decoration: underline;
                padding: 5px;
            }
            QLabel:hover {
                color: #00BFFF;  /* 🔹 Mudança de cor ao passar o mouse */
            }
        """)
        self.title_label.setWordWrap(True)
        self.title_label.setCursor(Qt.PointingHandCursor)
        self.title_label.setAlignment(Qt.AlignVCenter)
        self.title_label.setToolTip(link)  # 🔹 Exibe o link ao passar o mouse
        self.title_label.mousePressEvent = lambda event: abrir_link(link)

        # 🔹 Limitando altura para evitar problemas com textos longos
        self.title_label.setMaximumHeight(40)

        self.layout.addWidget(self.title_label, stretch=1)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SAMPA 4U")
        self.setWindowIcon(QIcon('Mapa_dos_Trilhos\\Favicon\\SP4U_LOGO.ico'))
        self.setStyleSheet("background-color: #cecece;")  # Cinza escuro

        # Configuração da janela principal
        monitor = get_monitors()[0]
        self.setGeometry(0, 0, monitor.width, monitor.height)
        self.setWindowState(Qt.WindowFullScreen)
        self.screen_width = monitor.width
        self.screen_height = monitor.height

        # Widget central e layout horizontal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)  # 🔹 Agora temos três áreas lado a lado

        # 🔹 Criando layouts antes de usá-los
        self.left_layout = QVBoxLayout()  # 🔹 Botões de guias
        self.center_layout = QVBoxLayout()  # 🔹 Notícias (NOVO)
        self.right_layout = QVBoxLayout()  # 🔹 Botões de linhas
        
        # 🔹 Containers para os layouts
        left_container = QWidget()
        left_container.setLayout(self.left_layout)
        center_container = QWidget()
        center_container.setLayout(self.center_layout)
        right_container = QWidget()
        right_container.setLayout(self.right_layout)

        # 🔹 Adicionando ao layout principal
        self.main_layout.addWidget(left_container, stretch=2)
        self.main_layout.addWidget(center_container, stretch=3)  # 🔹 Área do meio para notícias
        self.main_layout.addWidget(right_container, stretch=2)

        # 🔹 Configuração dos elementos
        self.setup_top_frames()  # 🔹 Botões de guias na esquerda
        self.setup_line_buttons()  # 🔹 Botões das linhas na direita
        self.setup_news_area()  # 🔹 Notícias agora no meio!

        # 🔹 Configuração do rodapé
        self.setup_footer()
        
        # 🔹 Carrega as notícias
        self.exibir_noticias()
        
        # 🔹 Atualizações periódicas
        self.setup_updates()
        
        # 🔹 Faz a varredura inicial
        fazer_varredura()
    
    def abrir_pesquisa_od(self):
        """Abre a janela de Pesquisa OD como diálogo modal"""
        from Pesquisa_od.pesquisa_od import pesquisa_od_metro
        pesquisa_od_metro(self)  # Passa self como parent
        
    def setup_top_frames(self):
        self.left_layout.setSpacing(5)  # Maior espaçamento para melhor organização
        self.left_layout.setContentsMargins(5, 5, 5, 5)  # Margens mais visíveis
        
        def criar_frame(titulo, altura_max, largura_max):
            frame = QGroupBox(titulo)
            frame.setStyleSheet("QGroupBox { font-weight: bold; padding: 8px; }")
            frame.setMaximumHeight(altura_max)  # Limita altura
            frame.setMaximumWidth(largura_max)  # Limita largura
            frame_layout = QVBoxLayout()
            frame.setLayout(frame_layout)
            return frame, frame_layout

        # Frame Mapas
        frame_mapas, layout_mapas = criar_frame("Mapas - Capital e RMSP", 120, 250)
        self.criar_botao(layout_mapas, "Acessar Mapa", mapa_global, "black", "#C0C0C0", "#A9A9A9", "mapa")
        self.left_layout.addWidget(frame_mapas)

        # Frame Sistemas
        frame_sistemas, layout_sistemas = criar_frame("Sistemas de Buscas de Linhas", 120, 250)
        self.criar_botao(layout_sistemas, "SPTRANS", sptrans, "black", "#FF2F2F", "#FF8080", "gtfs_sptrans")
        self.criar_botao(layout_sistemas, "EMTU", emtu, "black", "blue", "#5A79FF", "gtfs_emtu")
        self.left_layout.addWidget(frame_sistemas)
        
        # Frame Mapas da Rede
        frame_mapa_guia, layout_mapa_guia = criar_frame("Mapa da Rede - /Abr.25", 120, 250)
        self.criar_botao(layout_mapa_guia, "Mapa da Rede", mapa_rede, "black", "#00B352", "#5AFF7E", "mapa")
        self.left_layout.addWidget(frame_mapa_guia)
        
        # Frame Guias
        frame_guia_metro, layout_guia_metro = criar_frame("Guia de Usuário - METRÔ", 140, 250)
        self.criar_botao(layout_guia_metro, "Guia do Usuário - PT/BR", guia_pt_metro, "black", "blue", "#0073E6", "guias")
        self.criar_botao(layout_guia_metro, "Guia do Usuário - EN/US", guia_en_metro, "black", "blue", "#0073E6", "guias")
        self.left_layout.addWidget(frame_guia_metro)
        
        # Frame Pesquisas
        frame_pesquisas_metro, layout_pesquisas_metro = criar_frame("Pesquisas", 140, 250)
        self.criar_botao(layout_pesquisas_metro, "Pesquisa Origem e Destino", self.abrir_pesquisa_od, "black", "#00c9c4", "#007875", "pesquisa_od")
        self.criar_botao(layout_pesquisas_metro, "Demanda por Estação", passageiro_estacao, "black", "#00c9c4", "#007875", "pesquisa_pass")
        self.left_layout.addWidget(frame_pesquisas_metro)
        
        # Frame Mapa Qualidade do Ar
        frame_qualidade_ar, layout_qualidade_ar = criar_frame("Qualidade do Ar - São Paulo", 140, 250)
        self.criar_botao(layout_qualidade_ar, "Qualidade do Ar", mapa_qualidade_ar, "black", "#00c91b", "#00690e95", "qualidade_ar")
        self.left_layout.addWidget(frame_qualidade_ar)

    def criar_botao(self, parent, text, command, bg, fg, hovercolor, modulo=None):
        container = QWidget()
        container_layout = QHBoxLayout(container)
        
        if modulo:
            status_label = QLabel()
            status_label.setFixedSize(20, 20)
            self.atualizar_status(status_label, modulo)
            container_layout.addWidget(status_label)
        
        button = QPushButton(text)
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg};
                color: {fg};
                border: none;
                padding: 5px;
                text-align: left;
            }}
            QPushButton:hover {{
                background-color: {hovercolor};
            }}
        """)
        button.clicked.connect(command)
        container_layout.addWidget(button)
        parent.addWidget(container)
    
    def atualizar_status(self, label, modulo):
        try:
            cor = "green" if self.verificar_modulo(modulo) else "red"
        except Exception as e:
            cor = "red"
            print(f"Erro ao verificar o módulo '{modulo}': {e}")
        
        # Cria um pixmap com um círculo colorido
        pixmap = QPixmap(20, 20)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setBrush(QColor(cor))
        painter.setPen(QColor(cor))
        painter.drawEllipse(2, 2, 16, 16)
        painter.end()
        
        label.setPixmap(pixmap)
        
        # Agenda a próxima atualização
        QTimer.singleShot(2000, lambda: self.atualizar_status(label, modulo))
    
    def verificar_modulo(self, modulo):
        def normalizar_nome(nome: str) -> str:
            return nome.lower().replace("_", "").replace(" ", "")

        base_dir = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
        raiz = base_dir / "Mapa_dos_Trilhos"

        if not raiz.exists():
            print(f"❌ Pasta 'Mapa_dos_Trilhos' não encontrada em {base_dir}")
            return False

        caminho_normalizado = normalizar_nome(modulo)
        extensoes_validas = {".zip", ".csv", ".json", ".xlsx", ".xls", ".txt", ".png", ".jpg", ".pdf", ".parquet"}

        for item in raiz.rglob('*'):
            nome_item_normalizado = normalizar_nome(item.name)
            if caminho_normalizado in nome_item_normalizado and item.is_dir():
                arquivos = list(item.glob('*'))
                if arquivos:
                    print(f"✅ Diretório '{item}' existe e contém {len(arquivos)} arquivo(s).")
                    return True
                else:
                    print(f"⚠️ Diretório '{item}' encontrado, mas está vazio.")
                    return False

        subdirs = [p for p in raiz.iterdir() if p.is_dir()]
        nomes_normalizados = {normalizar_nome(p.name): p for p in subdirs}

        correspondencias = difflib.get_close_matches(caminho_normalizado, nomes_normalizados.keys(), n=1, cutoff=0.6)

        if correspondencias:
            match = correspondencias[0]
            pasta = nomes_normalizados[match]

            arquivos_validos = [arq for arq in pasta.glob("*") if arq.suffix.lower() in extensoes_validas]
            if arquivos_validos:
                print(f"✅ Diretório '{pasta}' contém arquivos válidos: {[a.name for a in arquivos_validos]}")
                return True
            else:
                print(f"⚠️ Diretório '{pasta}' encontrado, mas sem arquivos úteis.")
                return False

        print(f"❌ Erro: Nenhum caminho aproximado encontrado para '{modulo}'")
        return False
    
    def setup_news_area(self):
        news_label = QLabel("Notícias:")
        news_label.setStyleSheet("font-weight: bold;")
        self.center_layout.addWidget(news_label)  # 🔹 Agora corretamente no meio

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("background-color: #333333; border: none;")

        self.news_container = QWidget()
        self.news_layout = QVBoxLayout(self.news_container)
        self.news_layout.setAlignment(Qt.AlignTop)

        self.scroll_area.setWidget(self.news_container)
        self.center_layout.addWidget(self.scroll_area)  # 🔹 Movido para `center_layout`
        
        self.msg_noticias = QLabel()
        self.msg_noticias.setStyleSheet("color: red;")
        self.center_layout.addWidget(self.msg_noticias)  # 🔹 Correto agora!
    
    def exibir_noticias(self):
        noticias = notice_transp_sao_paulo()
        
        if noticias is not None:
            # Limpa notícias anteriores
            for i in reversed(range(self.news_layout.count())): 
                self.news_layout.itemAt(i).widget().setParent(None)
            
            for index, row in noticias.iterrows():
                title = row['title']
                link = row['link']
                image_url = row.get('image_url')
                
                news_widget = NewsWidget(title, link, image_url)
                self.news_layout.addWidget(news_widget)
                
                # Adiciona linha de separação
                separator = QFrame()
                separator.setFrameShape(QFrame.HLine)
                separator.setFrameShadow(QFrame.Sunken)
                separator.setStyleSheet("color: #555555;")
                self.news_layout.addWidget(separator)
        else:
            self.msg_noticias.setText("Nenhuma notícia encontrada.")
    
    def setup_line_buttons(self):
        # Carrega os dados das rotas
        self.routes = self.load_routes("Mapa_dos_Trilhos\\Gtfs_SPTRANS\\routes.txt")
        
        # Carrega os trajetos
        with open('Mapa_dos_Trilhos/Linhas/trajeto.json', 'r', encoding='utf-8') as file:
            self.trajetos = json.load(file)
        
        # Cores das linhas
        self.cor_linha_01 = self.trajetos["SP_L01.py"]["COR_LINHA"]
        self.cor_linha_02 = self.trajetos["SP_L02.py"]["COR_LINHA"]
        self.cor_linha_03 = self.trajetos["SP_L03.py"]["COR_LINHA"]
        self.cor_linha_04 = self.trajetos["SP_L04.py"]["COR_LINHA"]
        self.cor_linha_05 = self.trajetos["SP_L05.py"]["COR_LINHA"]
        self.cor_linha_07 = self.trajetos["SP_L07.py"]["COR_LINHA"]
        self.cor_linha_08 = self.trajetos["SP_L08.py"]["COR_LINHA"]
        self.cor_linha_09 = self.trajetos["SP_L09.py"]["COR_LINHA"]
        self.cor_linha_10 = self.trajetos["SP_L10.py"]["COR_LINHA"]
        self.cor_linha_11 = self.trajetos["SP_L11.py"]["COR_LINHA"]
        self.cor_linha_12 = self.trajetos["SP_L12.py"]["COR_LINHA"]
        self.cor_linha_13 = self.trajetos["SP_L13.py"]["COR_LINHA"]
        self.cor_linha_15 = self.trajetos["SP_L15.py"]["COR_LINHA"]
        
        # Cores adicionais
        self.laranja = "#999999"
        self.ouro = "#999999"
        
        # Configura os botões das linhas
        self.setup_line_button("Azul", line1, self.cor_linha_01, "white", "L1", "1.png", "1_azul.png", "METRÔ")
        self.setup_line_button("Verde", line2, self.cor_linha_02, "white", "L2", "2.png", "2_verde.png", "METRÔ")
        self.setup_line_button("Vermelha", line3, self.cor_linha_03, "black", "L3", "3.png", "3_vermelha.png", "METRÔ")
        self.setup_line_button("Amarela", line4, self.cor_linha_04, "black", "L4", "4.png", "4_amarela.png", "VIAQUATRO")
        self.setup_line_button("Lilás", line5, self.cor_linha_05, "white", "L5", "5.png", "5_lilas.png", "VIAMOBILIDADE")
        self.setup_line_button("Laranja", line6, self.laranja, "white", "L6", None, None, None)
        self.setup_line_button("Rubi", line7, self.cor_linha_07, "white", "L07", "7.png", "cptm.png", "CPTM")
        self.setup_line_button("Diamante", line8, self.cor_linha_08, "black", "L08", "8.png", "8_diamante.png", "VIAMOBILIDADE")
        self.setup_line_button("Esmeralda", line9, self.cor_linha_09, "black", "L09", "9.png", "9_esmeralda.png", "VIAMOBILIDADE")
        self.setup_line_button("Turquesa", line10, self.cor_linha_10, "black", "L10", "10.png", "cptm.png", "CPTM")
        self.setup_line_button("Coral", line11, self.cor_linha_11, "black", "L11", "11.png", "cptm.png", "CPTM")
        self.setup_line_button("Safira", line12, self.cor_linha_12, "white", "L12", "12.png", "cptm.png", "CPTM")
        self.setup_line_button("Jade", line13, self.cor_linha_13, "black", "L13", "13.png", "cptm.png", "CPTM")
        self.setup_line_button("Prata", line15, self.cor_linha_15, "black", "L15", "15.png", "15_prata.png", "METRÔ")
        self.setup_line_button("Ouro", line17, self.ouro, "white", "L17", None, None, "VIAMOBILIDADE")
    
    def load_routes(self, filepath):
        routes = {}
        with open(filepath, encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 4:
                    continue
                line_name = row[0].replace('"', '').strip()
                station_str = row[3].replace('"', '').strip()

                station_parts = [s.strip() for s in station_str.split(' - ') if s.strip()]
                nparts = len(station_parts)

                if nparts >= 2:
                    mid = nparts // 2
                    origin = " - ".join(station_parts[:mid])
                    destination = " - ".join(station_parts[mid:])
                elif nparts == 1:
                    origin = destination = station_parts[0]
                else:
                    origin = destination = ""

                if 'L' in line_name:
                    key = 'L' + line_name.split('L')[-1]
                else:
                    continue

                routes[key] = {
                    "origin": origin,
                    "destination": destination
                }
        return routes
    
    def setup_line_button(self, text, command, bg, fg, route_key, colored_icon_path=None, icon_path=None, operator=None):
        container = QWidget()
        container.setStyleSheet("background-color: transparent;")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(1,0,1,0)
        layout.setSpacing(0)  

        # 🔹 Coluna de status 
        status_label = QLabel("Status: ⚠️ Em Implantação")  # Exemplo: Status da linha
        status_label.setStyleSheet("font: bold 9pt; color: #0073E6; padding: 4px;")
        status_label.setFixedWidth(350)
        layout.addWidget(status_label)

        # 🔹 Criando um container horizontal para os itens
        button_row = QWidget()
        row_layout = QHBoxLayout(button_row)
        row_layout.setContentsMargins(0,0,0,0)
        row_layout.setSpacing(0)

        # 🔹 Ícones alinhados horizontalmente
        icon_row = QHBoxLayout()
        icon_row.setContentsMargins(0, 0, 0, 0)
        icon_row.setSpacing(0)

        if icon_path:
            icon1 = QLabel()
            pixmap1 = QPixmap(f"Mapa_dos_Trilhos/Icons/{icon_path}")
            icon1.setPixmap(pixmap1.scaled(18, 18, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            icon_row.addWidget(icon1)

        if colored_icon_path:
            icon2 = QLabel()
            pixmap2 = QPixmap(f"Mapa_dos_Trilhos/Icons/{colored_icon_path}")
            icon2.setPixmap(pixmap2.scaled(18, 18, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            icon_row.addWidget(icon2)

        icon_widget = QWidget()
        icon_widget.setLayout(icon_row)
        icon_widget.setFixedWidth(40)
        row_layout.addWidget(icon_widget)

        # 🔹 Coluna: Operador
        operator_label = QLabel(operator if operator else "")
        operator_label.setStyleSheet("font: 9pt; color: #555;")
        operator_label.setFixedWidth(95)
        row_layout.addWidget(operator_label)

        # 🔹 Coluna: Botão estilizado
        button = QPushButton(text)
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg};
                color: {fg};
                border-radius: 8px;
                padding: 6px;
                font-size: 10pt;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {fg};
                color: {bg};
            }}
        """)
        button.setFixedWidth(100)
        button.setFixedHeight(30)
        button.clicked.connect(command)
        row_layout.addWidget(button)

        # 🔹 Origem e destino
        route = self.routes.get(route_key, {})
        dest_container = QWidget()
        dest_layout = QVBoxLayout(dest_container)
        dest_layout.setContentsMargins(0, 0, 0, 0)
        dest_layout.setSpacing(1)

        origin = QLabel(route.get("origin", ""))
        origin.setStyleSheet("font: 8pt; color: #333;")
        origin.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        origin.setFixedHeight(16)
        dest_layout.addWidget(origin)

        destination = QLabel(route.get("destination", ""))
        destination.setStyleSheet("font: 8pt; color: #333;")
        destination.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        destination.setFixedHeight(16)
        dest_layout.addWidget(destination)

        dest_container.setFixedWidth(145)
        row_layout.addWidget(dest_container)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Plain)  
        separator.setStyleSheet("background-color: #eee; height: 1px;") 

        layout.addWidget(button_row)  # Adiciona a linha de botões ao layout vertical
        layout.addWidget(separator)   # Adiciona a barra de separação mais discreta
        
        self.right_layout.addWidget(container)
    
    def setup_footer(self):
        footer = QWidget()
        footer.setStyleSheet("background-color: #333333;")
        footer_layout = QHBoxLayout(footer)
        
        # Data e hora
        self.datetime_label = QLabel()
        self.datetime_label.setStyleSheet("color: white; font: bold 12pt;")
        footer_layout.addWidget(self.datetime_label, alignment=Qt.AlignRight)
        
        # Temperatura
        self.temp_label = QLabel(get_weather())
        self.temp_label.setStyleSheet("color: #00ff00; font: bold 14pt;")
        footer_layout.addWidget(self.temp_label, alignment=Qt.AlignRight)
        
        self.right_layout.addWidget(footer)
        footer.setVisible(True)  # Garante que o rodapé está visível

    def setup_updates(self):
        # Atualizações periódicas
        self.datetime_timer = QTimer(self)
        self.datetime_timer.timeout.connect(self.update_datetime)
        self.datetime_timer.start(1000)  # Atualiza a cada segundo
        
        self.temp_timer = QTimer(self)
        self.temp_timer.timeout.connect(self.update_temp)
        self.temp_timer.start(60000)  # Atualiza a cada minuto
    
    def update_datetime(self):
        now = QDateTime.currentDateTime()
        self.datetime_label.setText(now.toString("dd/MM/yyyy HH:mm"))
    
    def update_temp(self):
        self.temp_label.setText(get_weather())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            logging.info(f"Fechando Página Principal")
            self.close()
            
if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        logging.critical(f"Erro não tratado: {str(e)}", exc_info=True)
        QMessageBox.critical(None, "Erro Fatal", f"Ocorreu um erro crítico:\n{str(e)}")