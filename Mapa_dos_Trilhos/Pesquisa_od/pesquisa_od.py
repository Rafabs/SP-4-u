import pandas as pd
import logging
import os
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, 
                            QHeaderView, QAbstractItemView, QScrollArea, QFrame, 
                            QSizePolicy, QTabWidget, QSplitter, QMessageBox, QProgressDialog, QDialog)
from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QColor, QIcon
import folium
from folium.plugins import HeatMap
from PyQt5.QtWebEngineWidgets import QWebEngineView
import tempfile
from pathlib import Path

# Configuração do logger
logging.basicConfig(filename='Mapa_dos_Trilhos/log.txt', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Dicionário com os caminhos dos arquivos usando Path para melhor manipulação
arquivos_od = {
    2017: {
        "Dados Gerais": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab01_OD2017.xlsx"),
        "População por Idade": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab02_OD2017.xlsx"),
        "População por Instrução": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab03_OD2017.xlsx"),
        "População por Gênero": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab04_OD2017.xlsx"),
        "População por Renda": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab05_OD2017.xlsx"),
        "Renda Familiar": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab06_OD2017.xlsx"),
        "Famílias por Automóveis": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab07_OD2017.xlsx"),
        "Vínculo Empregatício": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab08_OD2017.xlsx"),
        "Condição de Atividade": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab09_OD2017.xlsx"),
        "Matrículas Escolares": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab10_OD2017.xlsx"),
        "Empregos por Setor": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab11_OD2017.xlsx"),
        "Empregos por Classe": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab12_OD2017.xlsx"),
        "Empregos por Vínculo": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab13_OD2017.xlsx"),
        "Empregos por Localização": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab14_OD2017.xlsx"),
        "Empregos por Tipo Trabalho": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab15_OD2017.xlsx"),
        "Viagens por Modo": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab16_OD2017.xlsx"),
        "Viagens por Tipo": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab17_OD2017.xlsx"),
        "Viagens por Motivo": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab18_OD2017.xlsx"),
        "Viagens a Pé": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab19_OD2017.xlsx"),
        "Tempo Médio Viagens": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab20_OD2017.xlsx"),
        "Viagens Atraídas por Modo": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab21_OD2017.xlsx"),
        "Viagens Atraídas por Tipo": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab22_OD2017.xlsx"),
        "Viagens Atraídas por Motivo": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab23_OD2017.xlsx"),
        "Matriz Coletivo": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab24_OD2017.xlsx"),
        "Matriz Individual": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab25_OD2017.xlsx"),
        "Matriz Motorizado": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab26_OD2017.xlsx"),
        "Matriz a Pé": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab27_OD2017.xlsx"),
        "Matriz Bicicleta": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab28_OD2017.xlsx"),
        "Matriz Não-Motorizado": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab29_OD2017.xlsx"),
        "Matriz Total": Path("Mapa_dos_Trilhos/Pesquisa_Origem_Destino/OD2017/Tabelas-OD2017/Tab30_OD2017.xlsx")
    }
}

class ThreadCarregamento(QThread):
    """Thread para carregar os dados em segundo plano"""
    progresso_atualizado = pyqtSignal(int, str)
    dados_carregados = pyqtSignal(dict)
    erro_ocorrido = pyqtSignal(str)

    def __init__(self, arquivos):
        super().__init__()
        self.arquivos = arquivos
        self.dados = {}

    def run(self):
        try:
            total = len(self.arquivos)
            for i, (nome_tab, caminho) in enumerate(self.arquivos.items(), 1):
                self.progresso_atualizado.emit(int((i/total)*100), f"Carregando {nome_tab}...")
                
                if not caminho.exists():
                    logging.warning(f"Arquivo não encontrado: {caminho}")
                    continue
                
                try:
                    # Tratamento especial para matrizes
                    if "Matriz" in nome_tab:
                        df = pd.read_excel(caminho, header=None)
                        if df.shape[0] > 517:
                            df = pd.read_excel(caminho, skiprows=df.shape[0]-517, header=None)
                        # Resetar índice para garantir índices numéricos
                        df = df.reset_index(drop=True)
                        # Converter cabeçalhos para strings
                        df.columns = [str(col) for col in df.columns]
                    else:
                        df = pd.read_excel(caminho, skiprows=6, header=0)
                        # Resetar índice para garantir índices numéricos
                        df = df.reset_index(drop=True)
                        # Converter nomes de colunas para strings
                        df.columns = [str(col) for col in df.columns]
                    
                    # Processamento básico
                    df = df.dropna(how='all').dropna(axis=1, how='all')
                    
                    self.dados[nome_tab] = df
                    
                except Exception as e:
                    logging.warning(f"Erro ao carregar {nome_tab}: {str(e)}")
                    self.erro_ocorrido.emit(f"Erro ao carregar {nome_tab}: {str(e)}")
            
            self.dados_carregados.emit(self.dados)
            
        except Exception as e:
            logging.error(f"Erro crítico no carregamento: {str(e)}", exc_info=True)
            self.erro_ocorrido.emit(f"Erro crítico: {str(e)}")

class MplCanvas(FigureCanvas):
    """Canvas para gráficos matplotlib"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

class AbaDados(QWidget):
    """Aba para exibição de dados em tabela"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        # Configuração da área de rolagem
        self.area_rolagem = QScrollArea()
        self.area_rolagem.setWidgetResizable(True)
        
        # Configuração da tabela
        self.tabela = QTableWidget()
        self.tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela.setAlternatingRowColors(True)
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        
        self.area_rolagem.setWidget(self.tabela)
        self.layout.addWidget(self.area_rolagem)
        
        # Configurar estilo
        self.tabela.setStyleSheet("""
            QTableWidget {
                gridline-color: #e0e0e0;
                font-size: 11px;
            }
            QHeaderView::section {
                background-color: #0078d7;
                color: white;
                padding: 4px;
                font-weight: bold;
                border: none;
            }
        """)
    
    def carregar_dados(self, df):
        """Carrega dados do DataFrame na tabela"""
        self.tabela.clear()
        
        if df is None or df.empty:
            return
        
        # Converter os nomes das colunas para strings
        colunas = [str(col) for col in df.columns]
        
        self.tabela.setColumnCount(len(colunas))
        self.tabela.setHorizontalHeaderLabels(colunas)
        
        # Converter o índice para inteiros (caso seja string)
        try:
            linhas = [int(idx) for idx in df.index]
            self.tabela.setRowCount(len(linhas))
        except (ValueError, TypeError):
            # Se não puder converter para inteiro, usar índice numérico padrão
            self.tabela.setRowCount(len(df))
        
        for row_idx, row in df.iterrows():
            # Garantir que row_idx seja inteiro
            try:
                row_idx_int = int(row_idx)
            except (ValueError, TypeError):
                # Se não puder converter, usar o índice numérico
                row_idx_int = df.index.get_loc(row_idx)
            
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem()
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                
                if pd.isna(value):
                    item.setText("N/D")
                    item.setForeground(QColor(150, 150, 150))
                elif isinstance(value, (int, float)):
                    # Formatação numérica para o padrão brasileiro
                    if abs(value) >= 1000:
                        texto = f"{value:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
                    else:
                        texto = f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".").rstrip('0').rstrip(',')
                    item.setText(texto)
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                else:
                    item.setText(str(value))
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                
                self.tabela.setItem(row_idx_int, col_idx, item)
        
        self.tabela.resizeColumnsToContents()

class AppOD(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Categorias para organização
        self.categorias = {
            "Dados Demográficos": [
                "Dados Gerais", "População por Idade", "População por Instrução",
                "População por Gênero", "População por Renda", "Renda Familiar",
                "Famílias por Automóveis"
            ],
            "Dados de Emprego": [
                "Vínculo Empregatício", "Condição de Atividade", "Empregos por Setor",
                "Empregos por Classe", "Empregos por Vínculo", "Empregos por Localização",
                "Empregos por Tipo Trabalho"
            ],
            "Dados Educacionais": [
                "Matrículas Escolares"
            ],
            "Dados de Viagens": [
                "Viagens por Modo", "Viagens por Tipo", "Viagens por Motivo",
                "Viagens por Motivo Destino", "Viagens a Pé", "Tempo Médio Viagens",
                "Viagens Atraídas por Modo", "Viagens Atraídas por Tipo",
                "Viagens Atraídas por Motivo", "Viagens Atraídas por Motivo Destino"
            ],
            "Matrizes OD": [
                "Matriz Coletivo", "Matriz Individual", "Matriz Motorizado",
                "Matriz a Pé", "Matriz Bicicleta", "Matriz Não-Motorizado",
                "Matriz Total"
            ]
        }

        self.abas_dados = {}      
        self.dados_completos = None
        self.todos_dados = {}

        self.setWindowTitle("Pesquisa Origem-Destino - METRÔ-SP")
        self.setWindowIcon(QIcon('metro_icon.png'))
        self.setModal(True)
        
        # Substitua setCentralWidget por um layout principal
        self.widget_principal = QWidget()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.widget_principal)
        
        # Mantenha todo o resto do seu código de inicialização...
        self.setMinimumSize(1200, 800)

        # Inicializar interface
        self.iniciar_interface()
        
        # Carregar dados
        self.carregar_dados()
        
        self.showMaximized()

    def closeEvent(self, event):
        """Garante que todas as threads sejam encerradas corretamente"""
        if hasattr(self, 'thread_carregamento') and self.thread_carregamento.isRunning():
            self.thread_carregamento.quit()
            self.thread_carregamento.wait()
        event.accept()
        
    def iniciar_interface(self):
        """Configura a interface gráfica"""
        # Remova qualquer layout existente
        if self.layout():
            QWidget().setLayout(self.layout())
        
        # Crie um layout principal
        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)  # Define o layout no diálogo
        
        # Barra de controle
        self.configurar_barra_controle()
        
        # Área principal com abas
        self.widget_abas = QTabWidget()
        self.configurar_abas_principais()
        
        self.layout_principal.addWidget(self.widget_abas)
        
        # Estilos
        self.configurar_estilos()

    def configurar_barra_controle(self):
        """Configura a barra de controle superior"""
        frame_controle = QFrame()
        frame_controle.setFrameShape(QFrame.StyledPanel)
        layout_controle = QHBoxLayout(frame_controle)  # Layout no frame, não no diálogo
        
        # Botão para atualizar dados
        self.botao_atualizar = QPushButton("Atualizar Dados")
        self.botao_atualizar.clicked.connect(self.carregar_dados)
        layout_controle.addWidget(self.botao_atualizar)
        
        layout_controle.addStretch()
        
        self.layout_principal.addWidget(frame_controle)  # Adiciona o frame ao layout principal

    def configurar_abas_principais(self):
        """Cria as abas principais organizadas por categoria"""
        for categoria, tabelas in self.categorias.items():
            widget_abas_categoria = QTabWidget()
            
            # Criar sub-abas para cada tabela
            for tabela in tabelas:
                self.abas_dados[tabela] = AbaDados()
                widget_abas_categoria.addTab(self.abas_dados[tabela], tabela)
            
            self.widget_abas.addTab(widget_abas_categoria, categoria)

    def configurar_estilos(self):
        """Define os estilos visuais da aplicação"""
        self.setStyleSheet("""
            QMainWindow { background-color: #f0f0f0; }
            QFrame { 
                background-color: white; 
                border-radius: 5px; 
                padding: 5px;
            }
            QPushButton {
                background-color: #0078d7; 
                color: white; 
                border: none;
                border-radius: 4px; 
                padding: 5px 10px;
                min-width: 100px;
            }
            QPushButton:hover { background-color: #005fa3; }
            QPushButton:pressed { background-color: #003d7e; }
            QTabWidget::pane {
                border: 1px solid #d0d0d0;
                border-radius: 4px;
            }
            QTabBar::tab {
                padding: 5px 10px;
                background: #e0e0e0;
                border: 1px solid #d0d0d0;
                border-bottom: none;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background: #0078d7;
                color: white;
            }
        """)

    def carregar_dados(self):
        """Inicia o carregamento dos dados"""
        # Mostrar diálogo de progresso
        self.dialogo_progresso = QProgressDialog("Carregando dados...", "Cancelar", 0, 100, self)
        self.dialogo_progresso.setWindowTitle("Carregamento de Dados")
        self.dialogo_progresso.setWindowModality(Qt.WindowModal)
        self.dialogo_progresso.setAutoClose(True)
        
        # Criar e configurar thread de carregamento
        self.thread_carregamento = ThreadCarregamento(arquivos_od[2017])
        self.thread_carregamento.progresso_atualizado.connect(self.atualizar_progresso)
        self.thread_carregamento.dados_carregados.connect(self.dados_carregados)
        self.thread_carregamento.erro_ocorrido.connect(self.mostrar_erro)
        
        # Conectar cancelamento
        self.dialogo_progresso.canceled.connect(self.thread_carregamento.terminate)
        
        # Iniciar thread
        self.thread_carregamento.start()
        self.dialogo_progresso.show()

    def atualizar_progresso(self, valor, mensagem):
        """Atualiza a barra de progresso"""
        self.dialogo_progresso.setValue(valor)
        self.dialogo_progresso.setLabelText(mensagem)
        QApplication.processEvents()

    def dados_carregados(self, dados):
        """Processa os dados após carregamento completo"""
        self.todos_dados = dados
        self.dados_completos = dados.get("Dados Gerais")
        
        # Verifique se o atributo existe
        if not hasattr(self, 'abas_dados'):
            self.abas_dados = {}
        
        # Atualize as abas
        for nome_tab, df in dados.items():
            if nome_tab in self.abas_dados:
                self.abas_dados[nome_tab].carregar_dados(df)

    def mostrar_erro(self, mensagem_erro):
        """Exibe mensagens de erro"""
        self.dialogo_progresso.close()
        QMessageBox.critical(self, "Erro", mensagem_erro)
        self.statusBar().showMessage("Erro ao carregar dados!")

def pesquisa_od_metro(parent=None):
    """Função para iniciar como janela independente"""
    app = QApplication.instance() or QApplication(sys.argv)
    janela = AppOD(parent)
    janela.show()
    
    if not QApplication.instance():
        app.exec_()
    return janela

if __name__ == "__main__":
    pesquisa_od_metro()