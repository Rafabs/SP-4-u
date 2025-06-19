from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
from PyQt5.QtWidgets import (QLabel, QPushButton, QTextEdit, QVBoxLayout, 
                            QWidget, QApplication, QHBoxLayout, QFrame)
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QScrollArea, QFrame, QGroupBox, QGraphicsEllipseItem,
    QGraphicsTextItem, QGraphicsLineItem, QSplitter
)
from PyQt5.QtCore import Qt, QTimer, QDateTime
import sys
import os
import requests
import certifi
import json
import folium
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import logging
import subprocess
from screeninfo import get_monitors
from pathlib import Path

# Get the absolute path to the project root
PROJECT_ROOT = Path(__file__).parent.parent.parent  # Go up 3 levels from qualidade_ar.py
sys.path.append(str(PROJECT_ROOT))

try:
    from Mapa_dos_Trilhos.Sobre.config import API_TOKEN_QUALLITY_AR
except ImportError as e:
    print(f"Error: Could not import config. Full path being checked: {PROJECT_ROOT / 'Mapa_dos_Trilhos/Sobre/config.py'}")
    print(f"Python path: {sys.path}")
    raise

# Get the absolute path to the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
    
from Mapa_dos_Trilhos.utils.logger_config import configurar_logger
configurar_logger()

def mapa_qualidade_ar():
    """Executa o script de qualidade do ar de forma segura"""
    try:
        logging.info("Abrindo Mapa de Qualidade do Ar")
        
        # Caminho absoluto para o script
        script_path = Path(__file__).resolve()
        
        # Comando para executar - use sys.executable para garantir o Python correto
        command = [sys.executable, str(script_path)]
        
        # Executar o processo
        process = subprocess.run(command, 
                               check=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
        
        # Registrar saída
        if process.stdout:
            logging.info(f"Saída: {process.stdout}")
        if process.stderr:
            logging.warning(f"Erros: {process.stderr}")
            
    except subprocess.CalledProcessError as e:
        error_msg = f"Erro ao executar o script (código {e.returncode}): {e.stderr}"
        logging.error(error_msg)
        print(error_msg)
    except Exception as e:
        error_msg = f"Erro inesperado: {str(e)}"
        logging.error(error_msg)
        print(error_msg)

def obter_classificacao(indice):
    if indice <= 40:
        return "N1"
    elif 41 <= indice <= 80:
        return "N2"
    elif 81 <= indice <= 120:
        return "N3"
    elif 121 <= indice <= 200:
        return "N4"
    else:
        return "N5"

class QualidadeArApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qualidade do Ar - São Paulo")
        monitor = get_monitors()[0]
        self.setGeometry(0, 0, monitor.width, monitor.height)        
        self.setWindowState(Qt.WindowFullScreen)
        
        # Layout principal
        layout = QVBoxLayout()
        
        # Cabeçalho
        cabecalho = QVBoxLayout()
        self.titulo = QLabel("Qualidade do Ar em Tempo Real")
        self.titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
        cabecalho.addWidget(self.titulo)

        self.descricao = QLabel("Clique no botão abaixo para atualizar o mapa com os dados atuais da qualidade do ar.")
        self.descricao.setWordWrap(True)
        cabecalho.addWidget(self.descricao)

        self.status_label = QLabel("Última atualização: ...")
        cabecalho.addWidget(self.status_label)
        layout.addLayout(cabecalho)
        
        # Legenda dos níveis de qualidade
        layout.addWidget(self.criar_legenda())
        
        # Área de resultados
        self.resultado_text = QTextEdit()
        self.resultado_text.setReadOnly(True)
        layout.addWidget(self.resultado_text)

        # Gráfico
        self.figure = plt.figure(figsize=(6, 2))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Mapa
        self.webview = QtWebEngineWidgets.QWebEngineView()
        layout.addWidget(self.webview, stretch=1)

        # Botão
        self.botao_atualizar = QPushButton("Atualizar Mapa")
        self.botao_atualizar.clicked.connect(self.gerar_mapa_qualidade_ar)
        layout.addWidget(self.botao_atualizar)

        self.setLayout(layout)
        self.gerar_mapa_qualidade_ar()
        
        # Timer para atualização automática (5 minutos)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.gerar_mapa_qualidade_ar)
        self.timer.start(300000)

    def criar_legenda(self):
        """Cria e retorna um widget com a legenda dos níveis de qualidade"""
        legenda_frame = QFrame()
        legenda_frame.setFrameShape(QFrame.StyledPanel)
        legenda_layout = QHBoxLayout(legenda_frame)
        legenda_layout.setContentsMargins(5, 5, 5, 5)
        
        # Dados dos níveis
        niveis = [
            {"cor": "green", "texto": "N1 (0-40) - Boa", "icone": "N1 - Boa.png"},
            {"cor": "yellow", "texto": "N2 (41-80) - Moderada", "icone": "N2 - Moderada.png"},
            {"cor": "orange", "texto": "N3 (81-120) - Ruim", "icone": "N3 - Ruim.png"},
            {"cor": "red", "texto": "N4 (121-200) - Muito Ruim", "icone": "N4 - Muito Ruim.png"},
            {"cor": "purple", "texto": "N5 (>200) - Péssima", "icone": "N5 - Péssima.png"}
        ]
        
        for nivel in niveis:
            item = QWidget()
            item_layout = QHBoxLayout(item)
            item_layout.setContentsMargins(5, 2, 5, 2)
            
            # Ícone
            icone = QLabel()
            pixmap = QPixmap(f"Mapa_dos_Trilhos/Icons/{nivel['icone']}")
            icone.setPixmap(pixmap.scaled(20, 20, QtCore.Qt.KeepAspectRatio))
            item_layout.addWidget(icone)
            
            # Texto
            label = QLabel(nivel['texto'])
            label.setStyleSheet(f"color: {nivel['cor']}; font-weight: bold;")
            item_layout.addWidget(label)
            item_layout.addStretch()
            
            legenda_layout.addWidget(item)
        
        legenda_layout.addStretch()
        return legenda_frame

    def gerar_mapa_qualidade_ar(self):
        icone_mapping = {
            "N1": "Mapa_dos_Trilhos/Icons/N1 - Boa.png",
            "N2": "Mapa_dos_Trilhos/Icons/N2 - Moderada.png",
            "N3": "Mapa_dos_Trilhos/Icons/N3 - Ruim.png",
            "N4": "Mapa_dos_Trilhos/Icons/N4 - Muito Ruim.png",
            "N5": "Mapa_dos_Trilhos/Icons/N5 - Péssima.png",
        }

        classificacao_mapping = {
            "N1": "Boa",
            "N2": "Moderada",
            "N3": "Ruim",
            "N4": "Muito Ruim",
            "N5": "Péssima",
        }

        contagem_classificacao = {"Boa": 0, "Moderada": 0, "Ruim": 0, "Muito Ruim": 0, "Péssima": 0}

        try:
            with open('Mapa_dos_Trilhos/Dados/dados_estacoes_medicoes.json', 'r', encoding='utf-8') as file:
                data = json.load(file)

            m = folium.Map(location=[-23.5505205, -46.6333083], zoom_start=10)

            for local, info in data['base_medicoes'].items():
                lat, lon = info['latitude'], info['longitude']
                estacao = local
                endereco = info['endereco']

                response = requests.get(
                    f"https://api.waqi.info/feed/geo:{lat};{lon}/?token={API_TOKEN_QUALLITY_AR}",
                    verify=certifi.where()
                )
                air_quality_data = response.json()
                indice = air_quality_data['data']['aqi']
                classificacao = obter_classificacao(indice)
                qualidade = classificacao_mapping[classificacao]
                contagem_classificacao[qualidade] += 1
                icone = icone_mapping[classificacao]

                folium.Marker(
                    [lat, lon],
                    icon=folium.CustomIcon(icon_image=icone, icon_size=(30, 30)),
                    popup=folium.Popup(
                        f"<b>Estação: </b>{estacao}<br>"
                        f"<b>Endereço: </b>{endereco}<br>"
                        f"<b>Índice: </b>{indice}<br>"
                        f"<b>Qualidade do Ar: </b>{qualidade}<br>",
                        max_width=300
                    )
                ).add_to(m)

            mapa_path = os.path.abspath("Mapa_dos_Trilhos/mapa_qualidade_ar.html")
            m.save(mapa_path)

            self.webview.setUrl(QtCore.QUrl.fromLocalFile(mapa_path))

            timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            self.resultado_text.append(f"[OK] Mapa atualizado às {timestamp}")
            self.status_label.setText(f"Última atualização: {timestamp}")

            # Atualizar gráfico
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            categorias = list(contagem_classificacao.keys())
            valores = list(contagem_classificacao.values())
            ax.bar(categorias, valores, color=["green", "yellow", "orange", "red", "purple"])
            ax.set_ylabel("Número de Estações")
            ax.set_title("Distribuição da Qualidade do Ar")
            self.canvas.draw()

        except Exception as e:
            self.resultado_text.append(f"[ERRO] Falha ao atualizar os dados: {str(e)}")
            self.status_label.setText("Erro ao atualizar o mapa.")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            logging.info(f"Fechando Mapa de Qualidade do Ar")
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = QualidadeArApp()
    janela.show()
    sys.exit(app.exec_())