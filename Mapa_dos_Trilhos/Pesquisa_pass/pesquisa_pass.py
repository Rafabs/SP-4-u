import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import json
import logging
import calendar
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton, QComboBox, QFrame, QSizePolicy, 
                            QScrollArea, QSplitter, QTabWidget)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QColor, QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import mplcursors
from screeninfo import get_monitors

# Configuração do logger
logging.basicConfig(filename="Mapa_dos_Trilhos/log.txt", filemode="a", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class ODApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Demanda de Passageiros - METRÔ-SP")
        self.setWindowIcon(QIcon('metro_icon.png'))
        
        # Carregar dados
        self.load_data()
        
        # Configurações da janela principal
        self.setup_ui()
        
        # Exibir em tela cheia
        monitor = get_monitors()[0]
        self.setGeometry(0, 0, monitor.width, monitor.height)
        
    def load_data(self):
        """Carrega os dados do CSV e JSON"""
        try:
            # Carregar CSV
            csv_file = "Mapa_dos_Trilhos/Demanda_Passageiros/data_passenger.csv"
            self.df = pd.read_csv(csv_file, sep=";", encoding="utf-8")
            
            # Carregar JSON
            json_file = "Mapa_dos_Trilhos/Linhas/trajeto.json"
            with open(json_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
            
            # Dicionários de mapeamento
            self.estacoes_dict = {}
            self.linhas_dict = {}
            
            self.mapa_linhas = {
                "LINHA 1": "01 - AZUL",
                "LINHA 2": "02 - VERDE",
                "LINHA 3": "03 - VERMELHA",
                "LINHA 4": "04 - AMARELA",
                "LINHA 5": "05 - LILÁS",
                "LINHA 15": "15 - PRATA"
            }
            
            for nome_arquivo, linha in self.data.items():
                if "LINHA" in linha:
                    self.linhas_dict[linha["LINHA"]] = linha["LINHA"]
                
                if "TRAJETO" in linha:
                    for estacao in linha["TRAJETO"]:
                        self.estacoes_dict[estacao["TAG"]] = estacao["primary"]
            
            # Aplicar mapeamento
            self.df["ESTACAO"] = self.df["ESTACAO"].map(self.estacoes_dict)
            self.df.dropna(subset=["ESTACAO"], inplace=True)
            self.df["LINHA"] = self.df["LINHA"].map(self.mapa_linhas)
            
            logging.info("Dados carregados com sucesso")
            
        except Exception as e:
            logging.error(f"Erro ao carregar dados: {str(e)}")
    
    def setup_ui(self):
        """Configura a interface do usuário"""
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Barra de controle
        self.setup_control_bar(main_layout)
        
        # Área de visualização
        self.setup_visualization_area(main_layout)
        
        # Aplicar estilos
        self.setup_styles()
    
    def setup_control_bar(self, parent_layout):
        """Configura a barra de controle com comboboxes"""
        control_frame = QFrame()
        control_frame.setFrameShape(QFrame.StyledPanel)
        control_layout = QHBoxLayout(control_frame)
        control_layout.setSpacing(20)
        
        # Combobox para linhas
        self.linha_label = QLabel("Selecione uma Linha:")
        self.linha_combo = QComboBox()
        self.linha_combo.addItems(sorted(self.linhas_dict.keys()))
        
        # Combobox para estações
        self.estacao_label = QLabel("Selecione uma Estação:")
        self.estacao_combo = QComboBox()
        
        # Botão para atualizar
        self.update_btn = QPushButton("Atualizar Gráfico")
        self.update_btn.setFixedWidth(150)
        
        # Adicionar widgets ao layout
        control_layout.addWidget(self.linha_label)
        control_layout.addWidget(self.linha_combo)
        control_layout.addWidget(self.estacao_label)
        control_layout.addWidget(self.estacao_combo)
        control_layout.addWidget(self.update_btn)
        control_layout.addStretch()
        
        parent_layout.addWidget(control_frame)
        
        # Conectar sinais
        self.linha_combo.currentTextChanged.connect(self.update_estacoes)
        self.update_btn.clicked.connect(self.update_graph)
    
    def setup_visualization_area(self, parent_layout):
        """Configura a área de visualização do gráfico"""
        # Splitter para gráfico e dados
        splitter = QSplitter(Qt.Vertical)
        
        # Frame do gráfico
        self.graph_frame = QFrame()
        self.graph_frame.setFrameShape(QFrame.StyledPanel)
        graph_layout = QVBoxLayout(self.graph_frame)
        
        # Canvas do matplotlib
        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        graph_layout.addWidget(self.canvas)
        
        # Frame de informações
        self.info_frame = QFrame()
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        info_layout = QVBoxLayout(self.info_frame)
        
        self.info_label = QLabel("Selecione uma linha e estação para visualizar os dados")
        self.info_label.setWordWrap(True)
        info_layout.addWidget(self.info_label)
        
        # Adicionar frames ao splitter
        splitter.addWidget(self.graph_frame)
        splitter.addWidget(self.info_frame)
        splitter.setSizes([600, 200])
        
        parent_layout.addWidget(splitter)
    
    def setup_styles(self):
        """Configura os estilos da aplicação"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QFrame {
                background-color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QLabel {
                color: #333333;
                font-size: 12px;
            }
            QComboBox {
                padding: 5px;
                min-width: 200px;
                border: 1px solid #cccccc;
                border-radius: 4px;
            }
            QPushButton {
                background-color: #0078d7;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
        """)
        
        # Estilos específicos
        self.linha_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.estacao_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.update_btn.setFont(QFont("Arial", 11))
        self.info_label.setFont(QFont("Arial", 11))
    
    def update_estacoes(self):
        """Atualiza as estações disponíveis para a linha selecionada"""
        linha_selecionada = self.linha_combo.currentText()
        
        if not linha_selecionada:
            return
            
        estacoes_filtradas = [
            estacao["primary"] for linha in self.data.values() if linha["LINHA"] == linha_selecionada
            for estacao in linha.get("TRAJETO", [])
        ]
        
        self.estacao_combo.clear()
        self.estacao_combo.addItems(sorted(estacoes_filtradas))
        
        if estacoes_filtradas:
            self.estacao_combo.setCurrentIndex(0)
    
    def update_graph(self):
        """Atualiza o gráfico com base nas seleções"""
        linha_selecionada = self.linha_combo.currentText()
        estacao_selecionada = self.estacao_combo.currentText()
        
        if not linha_selecionada or not estacao_selecionada:
            return
        
        try:
            # Verificar se a linha selecionada existe no mapa_linhas
            if linha_selecionada in self.mapa_linhas:
                linha_mapeada = self.mapa_linhas[linha_selecionada]
            else:
                # Tentar encontrar correspondência inversa
                linha_mapeada = next((k for k, v in self.mapa_linhas.items() if v == linha_selecionada), linha_selecionada)
            
            # Filtrar os dados
            df_filtrado = self.df[
                (self.df["ESTACAO"] == estacao_selecionada) &
                (self.df["LINHA"] == linha_mapeada)
            ].copy()
            
            if df_filtrado.empty:
                self.info_label.setText(f"Nenhum dado disponível para {estacao_selecionada} - {linha_selecionada}")
                return
            
            # Restante do código permanece o mesmo...
            colunas_necessarias = {"ANO", "MES", "MEDIA", "DETALHE_1", "DETALHE_2"}
            if not colunas_necessarias.issubset(df_filtrado.columns):
                self.info_label.setText("Dados incompletos para exibição")
                return

            # Converter dados
            meses_map = {
                "JANEIRO": 1, "FEVEREIRO": 2, "MARÇO": 3, "ABRIL": 4, "MAIO": 5, "JUNHO": 6,
                "JULHO": 7, "AGOSTO": 8, "SETEMBRO": 9, "OUTUBRO": 10, "NOVEMBRO": 11, "DEZEMBRO": 12
            }
            
            df_filtrado["MES"] = df_filtrado["MES"].str.upper().map(meses_map)
            df_filtrado.dropna(subset=["MES", "ANO"], inplace=True)
            df_filtrado["MES"] = df_filtrado["MES"].astype(int)
            df_filtrado["ANO"] = df_filtrado["ANO"].astype(int)
            df_filtrado["MEDIA"] = pd.to_numeric(df_filtrado["MEDIA"], errors="coerce")
            df_filtrado["MES_ANO"] = df_filtrado.apply(
                lambda x: f"{calendar.month_abbr[x['MES']]}-{x['ANO']}", axis=1)
            df_filtrado.sort_values(by=["ANO", "MES"], inplace=True)
            
            # Criar gráfico
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            
            # Configurar estilo
            sns.set_style("whitegrid")
            palette = sns.color_palette("Blues_d", n_colors=1)
            
            # Plotar dados
            scatter = ax.scatter(
                df_filtrado["MES_ANO"], 
                df_filtrado["MEDIA"], 
                color=palette[0], 
                s=100, 
                edgecolor="black",
                alpha=0.8
            )
            
            sns.lineplot(
                x=df_filtrado["MES_ANO"], 
                y=df_filtrado["MEDIA"], 
                marker="o", 
                color=palette[0], 
                linewidth=2, 
                ax=ax,
                alpha=0.6
            )
            
            # Configurações do gráfico
            ax.set_title(
                f"Demanda de Passageiros\n{estacao_selecionada} - {linha_selecionada}", 
                fontsize=14, 
                pad=20
            )
            ax.set_xlabel("Período", fontsize=12)
            ax.set_ylabel("Média de Passageiros (milhares)", fontsize=12)
            ax.grid(True, linestyle="--", alpha=0.6)
            plt.xticks(rotation=45)
            self.figure.tight_layout()
            
            # Tooltips interativos
            cursor = mplcursors.cursor(scatter, hover=True)
            cursor.connect(
                "add", 
                lambda sel: sel.annotation.set_text(
                    f"Período: {df_filtrado.iloc[sel.index]['MES_ANO']}\n"
                    f"Passageiros: {df_filtrado.iloc[sel.index]['MEDIA']:,.0f} mil\n"
                    f"{df_filtrado.iloc[sel.index]['DETALHE_1']}\n"
                    f"{df_filtrado.iloc[sel.index]['DETALHE_2']}"
                )
            )
            
            # Atualizar informações
            info_text = (
                f"<b>Estação:</b> {estacao_selecionada}<br>"
                f"<b>Linha:</b> {linha_selecionada}<br>"
                f"<b>Período analisado:</b> {len(df_filtrado)} meses<br>"
                f"<b>Média geral:</b> {df_filtrado['MEDIA'].mean():,.0f} mil passageiros"
            )
            self.info_label.setText(info_text)
            
            # Redesenhar o canvas
            self.canvas.draw()
            
        except KeyError as e:
            self.info_label.setText(f"Erro: Linha '{linha_selecionada}' não encontrada no mapeamento")
            logging.error(f"KeyError: {str(e)} - Linha selecionada: {linha_selecionada}")
        except Exception as e:
            self.info_label.setText("Ocorreu um erro ao processar os dados")
            logging.error(f"Erro inesperado: {str(e)}")

def passageiro_estacao():
    """Função principal para iniciar a aplicação"""
    logging.info("Abrindo Mapa da Pesquisa Origem e Destino")
    
    app = QApplication(sys.argv)
    window = ODApp()
    sys.exit(app.exec_())

if __name__ == "__main__":
    passageiro_estacao()