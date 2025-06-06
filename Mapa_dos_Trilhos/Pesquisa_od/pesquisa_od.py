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
                            QSizePolicy, QTabWidget, QSplitter)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QColor, QIcon

# Configuração do logger
logging.basicConfig(filename='Mapa_dos_Trilhos\\log.txt', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Dicionário com os caminhos dos arquivos por ano
arquivos_od = {
    1997: "Mapa_dos_Trilhos\\Pesquisa_Origem_Destino\\OD1997\\Tabelas-OD1997\\Tab01_OD97.xls",
    2007: "Mapa_dos_Trilhos\\Pesquisa_Origem_Destino\\OD2007\\Tabelas-OD2007\\Tab01_OD2007.xlsx",
    2017: "Mapa_dos_Trilhos\\Pesquisa_Origem_Destino\\OD2017\\Tabelas-OD2017\\Tab01_OD2017.xlsx"
}

class MplCanvas(FigureCanvas):
    """Classe para integração do matplotlib com PyQt5"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

class ODApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pesquisa Origem e Destino - METRÔ-SP")
        self.setWindowIcon(QIcon('metro_icon.png'))
        
        # Configurações da janela principal
        self.setMinimumSize(1000, 700)
        self.current_df = None
        
        # Widget central e layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        
        # Barra de controle
        self.setup_control_bar()
        
        # Área principal com abas
        self.setup_main_area()
        
        # Carregar estilos
        self.setup_styles()
        
        # Conectar sinais
        self.btn_carregar.clicked.connect(self.carregar_dados_selecionado)
        self.btn_gerar_graficos.clicked.connect(self.gerar_graficos)
        
        # Exibir
        self.showMaximized()
    
    def setup_control_bar(self):
        """Configura a barra de controle com combobox e botões"""
        control_frame = QFrame()
        control_frame.setFrameShape(QFrame.StyledPanel)
        control_layout = QHBoxLayout(control_frame)
        
        # Label
        lbl_ano = QLabel("Selecione o ano dos dados:")
        lbl_ano.setFont(QFont("Arial", 12))
        
        # Combobox
        self.combobox_anos = QComboBox()
        self.combobox_anos.setFont(QFont("Arial", 12))
        self.combobox_anos.addItems([str(ano) for ano in arquivos_od.keys()])
        self.combobox_anos.setFixedWidth(150)
        
        # Botões
        self.btn_carregar = QPushButton("Carregar Dados")
        self.btn_carregar.setFont(QFont("Arial", 12))
        self.btn_carregar.setFixedSize(150, 40)
        
        self.btn_gerar_graficos = QPushButton("Gerar Gráficos")
        self.btn_gerar_graficos.setFont(QFont("Arial", 12))
        self.btn_gerar_graficos.setFixedSize(150, 40)
        self.btn_gerar_graficos.setEnabled(False)
        
        # Adicionar widgets ao layout
        control_layout.addWidget(lbl_ano)
        control_layout.addWidget(self.combobox_anos)
        control_layout.addWidget(self.btn_carregar)
        control_layout.addWidget(self.btn_gerar_graficos)
        control_layout.addStretch()
        
        self.main_layout.addWidget(control_frame)
    
    def setup_main_area(self):
        """Configura a área principal com abas para tabela e gráficos"""
        self.tab_widget = QTabWidget()
        
        # Tab 1 - Tabela de dados
        self.tab_table = QWidget()
        self.setup_table_tab()
        
        # Tab 2 - Visualização de gráficos
        self.tab_graphs = QWidget()
        self.setup_graphs_tab()
        
        self.tab_widget.addTab(self.tab_table, "Dados Tabulares")
        self.tab_widget.addTab(self.tab_graphs, "Visualizações")
        
        self.main_layout.addWidget(self.tab_widget)
    
    def setup_table_tab(self):
        """Configura a aba da tabela"""
        layout = QVBoxLayout(self.tab_table)
        
        # Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        
        # Container para a tabela
        table_container = QWidget()
        table_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        table_layout = QVBoxLayout(table_container)
        table_layout.setContentsMargins(0, 0, 0, 0)
        
        # Tabela
        self.table = QTableWidget()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        
        table_layout.addWidget(self.table)
        scroll_area.setWidget(table_container)
        
        layout.addWidget(scroll_area)
    
    def setup_graphs_tab(self):
        """Configura a aba de gráficos"""
        layout = QVBoxLayout(self.tab_graphs)
        
        # Splitter para dividir os gráficos
        splitter = QSplitter(Qt.Vertical)
        
        # Gráfico 1 - Barras
        self.graph_frame1 = QFrame()
        self.graph_frame1.setFrameShape(QFrame.StyledPanel)
        graph_layout1 = QVBoxLayout(self.graph_frame1)
        self.canvas1 = MplCanvas(self, width=8, height=4, dpi=100)
        graph_layout1.addWidget(self.canvas1)
        
        # Gráfico 2 - Pizza
        self.graph_frame2 = QFrame()
        self.graph_frame2.setFrameShape(QFrame.StyledPanel)
        graph_layout2 = QVBoxLayout(self.graph_frame2)
        self.canvas2 = MplCanvas(self, width=8, height=4, dpi=100)
        graph_layout2.addWidget(self.canvas2)
        
        splitter.addWidget(self.graph_frame1)
        splitter.addWidget(self.graph_frame2)
        
        layout.addWidget(splitter)
    
    def setup_styles(self):
        """Configura os estilos da aplicação"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QFrame {
                background-color: white;
                border-radius: 5px;
            }
            QLabel {
                color: #333333;
            }
            QPushButton {
                background-color: #0078d7;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
            QComboBox {
                padding: 5px;
                border: 1px solid #cccccc;
                border-radius: 4px;
            }
            QTableWidget {
                border: none;
                alternate-background-color: #f8f8f8;
            }
            QHeaderView::section {
                background-color: #0078d7;
                color: white;
                padding: 5px;
                font-weight: bold;
            }
            QTabWidget::pane {
                border: none;
            }
            QTabBar::tab {
                background: #e0e0e0;
                padding: 8px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background: #0078d7;
                color: white;
            }
        """)
    
    def carregar_dados(self, ano):
        """Carrega os dados do arquivo correspondente ao ano selecionado"""
        if ano not in arquivos_od:
            logging.error(f"Erro: Ano {ano} não disponível.")
            return
        
        file_path = arquivos_od[ano]
        
        if not os.path.exists(file_path):
            logging.error(f"Erro: Arquivo não encontrado para {ano}: {file_path}")
            return
        
        try:
            if ano == 1977:
                df = pd.read_excel(file_path, skiprows=3, usecols=[0, 1], names=["Município", "Nome do Município"])
            elif ano in [1997, 2007, 2017]:
                df = pd.read_excel(file_path, skiprows=6)
            else:
                df = pd.read_excel(file_path)

            logging.info(f"Dados do ano {ano} carregados com sucesso.")
            self.current_df = df
            self.exibir_dados(df)
            self.btn_gerar_graficos.setEnabled(True)

        except Exception as e:
            logging.error(f"Erro ao carregar os dados do ano {ano}: {str(e)}")
            self.btn_gerar_graficos.setEnabled(False)
    
    def exibir_dados(self, df):
        """Exibe os dados na tabela formatados"""
        self.table.clear()
        
        # Configurar colunas
        self.table.setColumnCount(len(df.columns))
        self.table.setHorizontalHeaderLabels(df.columns)
        
        # Configurar linhas
        self.table.setRowCount(len(df))
        
        # Preencher dados
        for row_idx, row in df.iterrows():
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem()
                
                # Formatar números
                if isinstance(value, (int, float)):
                    text = f"{value:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
                    item.setData(Qt.DisplayRole, text)
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                else:
                    item.setText(str(value))
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                
                self.table.setItem(row_idx, col_idx, item)
        
        # Ajustar largura das colunas
        self.table.resizeColumnsToContents()
        
        # Adicionar destaque para linhas alternadas
        for i in range(self.table.rowCount()):
            if i % 2 == 0:
                for j in range(self.table.columnCount()):
                    if self.table.item(i, j):
                        self.table.item(i, j).setBackground(QColor(240, 240, 240))
    
    def gerar_graficos(self):
        """Gera visualizações gráficas dos dados carregados"""
        if self.current_df is None:
            return
        
        df = self.current_df
        
        try:
            # Limpar gráficos anteriores
            self.canvas1.axes.clear()
            self.canvas2.axes.clear()
            
            # Gráfico 1 - Barras (top 10 municípios)
            if 'Município' in df.columns and len(df.columns) > 1:
                numeric_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
                if numeric_cols:
                    col = numeric_cols[0]  # Primeira coluna numérica
                    top10 = df.nlargest(10, col)
                    
                    bars = self.canvas1.axes.barh(
                        top10['Município'].astype(str), 
                        top10[col],
                        color='#0078d7'
                    )
                    
                    # Adicionar valores nas barras
                    for bar in bars:
                        width = bar.get_width()
                        self.canvas1.axes.text(
                            width, bar.get_y() + bar.get_height()/2,
                            f'{width:,.0f}'.replace(',', '.'),
                            va='center', ha='left', color='black'
                        )
                    
                    self.canvas1.axes.set_title(f'Top 10 Municípios - {col}')
                    self.canvas1.axes.set_xlabel('Quantidade')
                    self.canvas1.axes.grid(axis='x', linestyle='--', alpha=0.6)
            
            # Gráfico 2 - Pizza (distribuição percentual)
            if len(df.columns) >= 2 and len(df) > 1:
                numeric_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
                if numeric_cols:
                    col = numeric_cols[0]  # Primeira coluna numérica
                    top5 = df.nlargest(5, col)
                    outros = df[col].sum() - top5[col].sum()
                    
                    sizes = list(top5[col]) + [outros]
                    labels = list(top5.iloc[:, 0].astype(str)) + ['Outros']
                    colors = ['#0078d7', '#005fa3', '#003f72', '#7fb6e6', '#c2d9f0', '#e6e6e6']
                    
                    self.canvas2.axes.pie(
                        sizes, labels=labels, colors=colors,
                        autopct='%1.1f%%', startangle=90,
                        wedgeprops={'edgecolor': 'white', 'linewidth': 1}
                    )
                    
                    self.canvas2.axes.set_title('Distribuição Percentual')
                    self.canvas2.axes.axis('equal')  # Garante que o gráfico fique circular
            
            # Atualizar os canvas
            self.canvas1.draw()
            self.canvas2.draw()
            
            # Mudar para a aba de gráficos
            self.tab_widget.setCurrentIndex(1)
            
        except Exception as e:
            logging.error(f"Erro ao gerar gráficos: {str(e)}")
    
    def carregar_dados_selecionado(self):
        """Obtém o ano selecionado pelo usuário e chama carregar_dados"""
        ano = int(self.combobox_anos.currentText())
        self.carregar_dados(ano)

def pesquisa_od_metro():
    """Função principal para iniciar a aplicação"""
    logging.info("Abrindo Mapa da Pesquisa Origem e Destino")
    
    app = QApplication(sys.argv)
    window = ODApp()
    sys.exit(app.exec_())

if __name__ == "__main__":
    pesquisa_od_metro()