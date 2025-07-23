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
Ponto de entrada principal do sistema SAMPA 4U - AplicaÃ§Ã£o Qt que consolida:
- Monitoramento em tempo real das linhas de metrÃ´/trem de SP
- VisualizaÃ§Ã£o de mapas e rotas interativas
- NotÃ­cias atualizadas sobre transporte
- Pesquisas de origem-destino (OD)
- Qualidade do ar e condiÃ§Ãµes climÃ¡ticas com diversos dados
- Console de logs integrado
- Interface responsiva para mÃºltiplos monitores
- ConfirmaÃ§Ã£o de encerramento de janela GUI
ARQUITETURA:
    main.py
"""

from PyQt5.QtGui import QPixmap, QIcon, QFont, QColor, QPainter, QImage
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QFrame, QGroupBox, QGraphicsEllipseItem,
    QGraphicsTextItem, QGraphicsLineItem, QSplitter, QMessageBox
)
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
from console_logger import ConsoleLogger, ConsoleLogHandler
from logging.handlers import RotatingFileHandler
from cmsp import get_metro_status
from cptm import get_cptm_status

init()

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    except:
        try:
            locale.setlocale(locale.LC_ALL, 'pt_BR')
        except:
            try:
                locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
            except locale.Error:
                print("Não foi possível configurar o locale para português brasileiro. Usando padrão do sistema.")
                locale.setlocale(locale.LC_ALL, '')


def excepthook(exc_type, exc_value, exc_tb):
    """Hook para tratamento de exceções não capturadas.
    
    Args:
        exc_type: Tipo da exceção
        exc_value: Valor da exceção
        exc_tb: Traceback da exceção
    """
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    logging.critical(f"Exceção não tratada:\n{tb}")
    QMessageBox.critical(
        None, "Erro", f"Exceção não tratada:\n{str(exc_value)}")
    QApplication.quit()


sys.excepthook = excepthook

base_dir = Path(__file__).resolve().parent
sys.path.extend([
    str(base_dir / 'Mapa_dos_Trilhos'),
    str(base_dir / 'Mapa_dos_Trilhos' / 'Linhas'),
    str(base_dir / 'Mapa_dos_Trilhos' / 'Qualidade_ar'),
    str(base_dir / 'Mapa_dos_Trilhos' / 'Sobre')
])


def log_close_time():
    """Registra o horário de fechamento do programa no log."""
    logging.info(f"{'=' * 30} PROGRAMA FECHADO {'=' * 30}")


atexit.register(log_close_time)


def dados_usuario():
    """Coleta e exibe informações do sistema do usuário.
    
    Mostra informações como sistema operacional, diretório atual, versão do Python,
    processador e outros dados relevantes para diagnóstico.
    """
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
    """Classe para redirecionar stdout/stderr para o sistema de logging.
    
    Attributes:
        logger (logging.Logger): Instância do logger para redirecionamento
        log_level (int): Nível de log (INFO, ERROR, etc.)
        buffer (str): Buffer para armazenamento temporário de mensagens
    """

    def __init__(self, logger, log_level=logging.INFO):
        """Inicializa o StreamToLogger.
        
        Args:
            logger: Instância do logger
            log_level: Nível de log padrão (default: logging.INFO)
        """
        self.logger = logger
        self.log_level = log_level
        self.buffer = ''

    def write(self, buf):
        """Escreve no buffer e envia para o logger quando houver quebra de linha.
        
        Args:
            buf: Mensagem a ser escrita no buffer
        """
        try:
            if buf and buf.strip():
                self.buffer += buf
                while '\n' in self.buffer:
                    line, self.buffer = self.buffer.split('\n', 1)
                    if line.strip():
                        self.logger.log(self.log_level, line.strip())
        except Exception as e:
            sys.__stderr__.write(f"Erro no StreamToLogger: {str(e)}\n")
            sys.__stderr__.write(f"Conteúdo do buffer: {self.buffer}\n")

    def flush(self):
        """Força o envio do buffer restante para o logger."""
        if self.buffer.strip():
            self.logger.log(self.log_level, self.buffer.strip())
            self.buffer = ''


BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / "Mapa_dos_Trilhos"
LOG_FILE = LOG_DIR / "log.log"

LOG_DIR.mkdir(parents=True, exist_ok=True)


def setup_logging():
    """Configura o sistema de logging da aplicação.
    
    Cria handlers para arquivo de log e redirecionamento de stdout/stderr.
    Configura rotação de logs com tamanho máximo de 5MB e 3 backups.
    """
    # Remove todos os handlers existentes
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
        handler.close()

    # Configura handler de arquivo
    file_handler = RotatingFileHandler(
        str(LOG_FILE),
        encoding='utf-8',
        maxBytes=5*1024*1024,
        backupCount=3
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    ))

    # Configura logger principal apenas com file handler
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)

    # Configura logger separado para stdout/stderr
    std_logger = logging.getLogger('STD_OUT_ERR')
    std_logger.setLevel(logging.INFO)
    std_logger.propagate = False  # Evita que mensagens sejam enviadas ao root logger

    # Redireciona stdout/stderr
    sys.stdout = StreamToLogger(std_logger, logging.INFO)
    sys.stderr = StreamToLogger(std_logger, logging.ERROR)


# Inicializa o logging
setup_logging()

dados_usuario()

with open(base_dir / 'Mapa_dos_Trilhos' / 'Linhas' / 'subtitle.json', 'r', encoding='utf-8') as file:
    lines_data = json.load(file)


def abrir_link(url):
    """Abre um URL no navegador padrão do sistema.
    
    Args:
        url: URL a ser aberto
    """
    url = re.sub(r'/[^/]*$', '', url)
    webbrowser.open_new(url)


class NewsWidget(QWidget):
    """Widget para exibição de notícias sobre transporte público.
    
    Attributes:
        layout (QHBoxLayout): Layout principal do widget
        title_label (QLabel): Label com título da notícia
    """

    def __init__(self, title, link, image_url=None, parent=None):
        """Inicializa o NewsWidget.
        
        Args:
            title: Título da notícia
            link: URL da notícia
            image_url: URL da imagem (opcional)
            parent: Widget pai (opcional)
        """
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
        self.layout.setSpacing(10)

        self.title_label = QLabel(f"🔗 {title}")
        self.title_label.setStyleSheet("""
            QLabel {
                color: white;
                font: bold 12pt Arial;
                text-decoration: underline;
                padding: 5px;
            }
            QLabel:hover {
                color: #00BFFF;
            }
        """)
        self.title_label.setWordWrap(True)
        self.title_label.setCursor(Qt.PointingHandCursor)
        self.title_label.setAlignment(Qt.AlignVCenter)
        self.title_label.setToolTip(link)
        self.title_label.mousePressEvent = lambda event: abrir_link(link)
        self.title_label.setMaximumHeight(40)
        self.layout.addWidget(self.title_label, stretch=1)


class MainWindow(QMainWindow):
    """Classe principal da janela da aplicação SAMPA 4U.
    
    Attributes:
        central_widget (QWidget): Widget central da janela
        main_layout (QHBoxLayout): Layout principal
        left_layout (QVBoxLayout): Layout do painel esquerdo
        center_layout (QVBoxLayout): Layout do painel central
        right_layout (QVBoxLayout): Layout do painel direito
        screen_width (int): Largura da tela
        screen_height (int): Altura da tela
        console_logger (ConsoleLogger): Logger para console integrado
    """

    def __init__(self):
        """Inicializa a janela principal com todos os componentes."""
        super().__init__()
        self.setWindowTitle("SAMPA 4U")
        icon_path = BASE_DIR / "Mapa_dos_Trilhos" / "Favicon" / "SP4U_LOGO.ico"
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setStyleSheet("background-color: #cecece;")

        monitor = get_monitors()[0]
        self.setGeometry(0, 0, monitor.width, monitor.height)
        self.setWindowState(Qt.WindowFullScreen)
        self.screen_width = monitor.width
        self.screen_height = monitor.height

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)

        self.left_layout = QVBoxLayout()
        self.center_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()

        left_container = QWidget()
        left_container.setLayout(self.left_layout)
        center_container = QWidget()
        center_container.setLayout(self.center_layout)
        right_container = QWidget()
        right_container.setLayout(self.right_layout)

        self.main_layout.addWidget(left_container, stretch=2)
        self.main_layout.addWidget(center_container, stretch=3)
        self.main_layout.addWidget(right_container, stretch=2)

        self.setup_top_frames()
        self.setup_line_buttons()
        self.setup_news_area()

        self.setup_footer()

        self.exibir_noticias()

        self.setup_updates()

        self.setup_console_logger()

    def setup_console_logger(self):
        """Configura o console de logs integrado na interface.
        
        Cria um painel de logs com controles para limpar, copiar e ativar/desativar
        auto-scroll. Conecta o logger da GUI ao root logger do Python.
        """
        self.console_logger = ConsoleLogger()

        # Cria logger específico para a GUI
        gui_logger = logging.getLogger('GUI_Console')
        gui_logger.setLevel(logging.INFO)
        gui_logger.propagate = False

        # Adiciona handler para o console gráfico
        console_handler = ConsoleLogHandler(self.console_logger)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        ))
        gui_logger.addHandler(console_handler)

        # Conecta o logger da GUI ao root logger
        root_logger = logging.getLogger()
        root_logger.addHandler(console_handler)

        # Painel de controle (mantenha o existente)
        control_panel = QWidget()
        control_layout = QHBoxLayout(control_panel)
        control_layout.setContentsMargins(0, 0, 0, 0)

        # Botão Limpar
        btn_clear = QPushButton("Limpar")
        btn_clear.setStyleSheet("padding: 3px;")
        btn_clear.clicked.connect(self.console_logger.clear)

        # Botão Copiar
        btn_copy = QPushButton("Copiar")
        btn_copy.setStyleSheet("padding: 3px;")
        btn_copy.clicked.connect(self.console_logger.copy_to_clipboard)

        # Botão Auto-scroll
        self.btn_autoscroll = QPushButton("Auto-scroll")
        self.btn_autoscroll.setStyleSheet("padding: 3px;")
        self.btn_autoscroll.setCheckable(True)
        self.btn_autoscroll.setChecked(True)
        self.btn_autoscroll.toggled.connect(
            lambda checked: setattr(
                self.console_logger, 'auto_scroll', checked)
        )

        # Adiciona botões ao painel
        control_layout.addWidget(btn_clear)
        control_layout.addWidget(btn_copy)
        control_layout.addWidget(self.btn_autoscroll)
        control_layout.addStretch()

        # Adiciona ao layout
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)

        self.center_layout.addWidget(separator)
        self.center_layout.addWidget(QLabel("Console de Logs:"))
        self.center_layout.addWidget(control_panel)
        self.center_layout.addWidget(self.console_logger)

        logging.info("Console de logs inicializado")

    def abrir_pesquisa_od(self):
        """Abre a janela de Pesquisa Origem-Destino (OD) como diálogo modal."""
        from Pesquisa_od.pesquisa_od import pesquisa_od_metro
        pesquisa_od_metro(self)

    def setup_top_frames(self):
        """Configura os frames superiores do painel esquerdo.
        
        Cria grupos de botões para mapas, sistemas de busca, guias do usuário,
        pesquisas e qualidade do ar.
        """
        self.left_layout.setSpacing(5)
        self.left_layout.setContentsMargins(5, 5, 5, 5)

        def criar_frame(titulo, altura_max, largura_max):
            """Função auxiliar para criar frames com estilo consistente.
            
            Args:
                titulo: Título do frame
                altura_max: Altura máxima do frame
                largura_max: Largura máxima do frame
                
            Returns:
                Tuple: (frame, layout) criados
            """
            frame = QGroupBox(titulo)
            frame.setStyleSheet(
                "QGroupBox { font-weight: bold; padding: 8px; }")
            frame.setMaximumHeight(altura_max)
            frame.setMaximumWidth(largura_max)
            frame_layout = QVBoxLayout()
            frame.setLayout(frame_layout)
            return frame, frame_layout

        frame_mapas, layout_mapas = criar_frame(
            "Mapas - Capital e RMSP", 120, 250)
        self.criar_botao(layout_mapas, "Acessar Mapa",
                         mapa_global, "black", "#C0C0C0", "#A9A9A9", "mapa")
        self.left_layout.addWidget(frame_mapas)

        frame_sistemas, layout_sistemas = criar_frame(
            "Sistemas de Buscas de Linhas", 120, 250)
        self.criar_botao(layout_sistemas, "SPTRANS", sptrans,
                         "black", "#FF2F2F", "#FF8080", "gtfs_sptrans")
        self.criar_botao(layout_sistemas, "EMTU", emtu,
                         "black", "blue", "#5A79FF", "gtfs_emtu")
        self.left_layout.addWidget(frame_sistemas)

        frame_mapa_guia, layout_mapa_guia = criar_frame(
            "Mapa da Rede - /Abr.25", 120, 250)
        self.criar_botao(layout_mapa_guia, "Mapa da Rede",
                         mapa_rede, "black", "#00B352", "#5AFF7E", "mapa")
        self.left_layout.addWidget(frame_mapa_guia)

        frame_guia_metro, layout_guia_metro = criar_frame(
            "Guia de Usuário - METRÔ", 140, 250)
        self.criar_botao(layout_guia_metro, "Guia do Usuário - PT/BR",
                         guia_pt_metro, "black", "blue", "#0073E6", "guias")
        self.criar_botao(layout_guia_metro, "Guia do Usuário - EN/US",
                         guia_en_metro, "black", "blue", "#0073E6", "guias")
        self.left_layout.addWidget(frame_guia_metro)

        frame_pesquisas_metro, layout_pesquisas_metro = criar_frame(
            "Pesquisas", 140, 250)
        self.criar_botao(layout_pesquisas_metro, "Pesquisa Origem e Destino",
                         self.abrir_pesquisa_od, "black", "#00c9c4", "#007875", "pesquisa_od")
        self.criar_botao(layout_pesquisas_metro, "Demanda por Estação",
                         passageiro_estacao, "black", "#00c9c4", "#007875", "pesquisa_pass")
        self.left_layout.addWidget(frame_pesquisas_metro)

        frame_qualidade_ar, layout_qualidade_ar = criar_frame(
            "Qualidade do Ar - São Paulo", 140, 250)
        self.criar_botao(layout_qualidade_ar, "Qualidade do Ar",
                         mapa_qualidade_ar, "black", "#00c91b", "#00690e95", "qualidade_ar")
        self.left_layout.addWidget(frame_qualidade_ar)

    def get_line_status(self, line_name):
        """Obtém o status atual de uma linha de transporte.
        
        Realiza web scraping para obter o status em tempo real das linhas do metrô e CPTM.
        
        Args:
            line_name: Nome da linha (ex: "Azul", "Rubi")
            
        Returns:
            str: Status da linha ou "Em implantação" para linhas não encontradas
        """
        # Mapeamento de nomes para os sistemas
        metro_lines = {
            "Azul": "1",
            "Verde": "2",
            "Vermelha": "3",
            "Amarela": "4",
            "Lilás": "5",
            "Prata": "15"
        }

        cptm_lines = {
            "Rubi": "7",
            "Turquesa": "10",
            "Coral": "11",
            "Safira": "12",
            "Jade": "13",
            "Diamante": "8",
            "Esmeralda": "9"
        }

        # Verifica se é uma linha do Metrô
        if line_name in metro_lines:
            status_data = get_metro_status()
            if 'erro' in status_data:
                return "Dados indisponíveis"

            for linha in status_data['linhas']:
                if linha['numero'] == metro_lines[line_name]:
                    return linha['status']

        # Verifica se é uma linha da CPTM/ViaMobilidade
        elif line_name in cptm_lines:
            status_data = get_cptm_status()
            if 'erro' in status_data:
                return "Dados indisponíveis"

            for linha in status_data['linhas']:
                if linha['nome'] == line_name:
                    return linha['status']

        # Para linhas em implantação
        return "Em implantação"

    def criar_botao(self, parent, text, command, bg, fg, hovercolor, modulo=None):
        """Cria um botão personalizado com status de módulo opcional.
        
        Args:
            parent: Layout pai onde o botão será adicionado
            text: Texto do botão
            command: Função a ser chamada no clique
            bg: Cor de fundo do botão
            fg: Cor do texto do botão
            hovercolor: Cor quando o mouse está sobre o botão
            modulo: Nome do módulo para verificação de status (opcional)
        """
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
        """Atualiza o status de um módulo exibido como um indicador circular.
        
        Args:
            label: QLabel onde o status será exibido
            modulo: Nome do módulo a ser verificado
        """
        try:
            cor = "green" if self.verificar_modulo(modulo) else "red"
        except Exception as e:
            cor = "red"
            print(f"Erro ao verificar o módulo '{modulo}': {e}")

        pixmap = QPixmap(20, 20)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setBrush(QColor(cor))
        painter.setPen(QColor(cor))
        painter.drawEllipse(2, 2, 16, 16)
        painter.end()

        label.setPixmap(pixmap)

        QTimer.singleShot(2000, lambda: self.atualizar_status(label, modulo))

    def verificar_modulo(self, modulo):
        """Verifica se um módulo existe e contém arquivos válidos.
        
        Args:
            modulo: Nome do módulo/diretório a ser verificado
            
        Returns:
            bool: True se o módulo existe e contém arquivos válidos, False caso contrário
        """
        def normalizar_nome(nome: str) -> str:
            return nome.lower().replace("_", "").replace(" ", "")

        base_dir = Path(__file__).resolve(
        ).parent if "__file__" in globals() else Path.cwd()
        raiz = base_dir / "Mapa_dos_Trilhos"

        if not raiz.exists():
            print(f"Pasta 'Mapa_dos_Trilhos' não encontrada em {base_dir}")
            return False

        caminho_normalizado = normalizar_nome(modulo)
        extensoes_validas = {".zip", ".csv", ".json", ".xlsx",
                             ".xls", ".txt", ".png", ".jpg", ".pdf", ".parquet"}

        for item in raiz.rglob('*'):
            nome_item_normalizado = normalizar_nome(item.name)
            if caminho_normalizado in nome_item_normalizado and item.is_dir():
                arquivos = list(item.glob('*'))
                if arquivos:
                    print(
                        f"Diretório '{item}' existe e contém {len(arquivos)} arquivo(s).")
                    return True
                else:
                    print(f"Diretório '{item}' encontrado, mas está vazio.")
                    return False

        subdirs = [p for p in raiz.iterdir() if p.is_dir()]
        nomes_normalizados = {normalizar_nome(p.name): p for p in subdirs}

        correspondencias = difflib.get_close_matches(
            caminho_normalizado, nomes_normalizados.keys(), n=1, cutoff=0.6)

        if correspondencias:
            match = correspondencias[0]
            pasta = nomes_normalizados[match]

            arquivos_validos = [arq for arq in pasta.glob(
                "*") if arq.suffix.lower() in extensoes_validas]
            if arquivos_validos:
                print(
                    f"Diretório '{pasta}' contém arquivos válidos: {[a.name for a in arquivos_validos]}")
                return True
            else:
                print(
                    f"Diretório '{pasta}' encontrado, mas sem arquivos úteis.")
                return False

        print(f"Erro: Nenhum caminho aproximado encontrado para '{modulo}'")
        return False

    def setup_news_area(self):
        """Configura a área de notícias na interface.
        
        Cria um scroll area para exibição de notícias sobre transporte público.
        """
        news_label = QLabel("Notícias:")
        news_label.setStyleSheet("font-weight: bold;")
        self.center_layout.addWidget(news_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet(
            "background-color: #333333; border: none;")

        self.news_container = QWidget()
        self.news_layout = QVBoxLayout(self.news_container)
        self.news_layout.setAlignment(Qt.AlignTop)

        self.scroll_area.setWidget(self.news_container)
        self.center_layout.addWidget(self.scroll_area)

        self.msg_noticias = QLabel()
        self.msg_noticias.setStyleSheet("color: red;")
        self.center_layout.addWidget(self.msg_noticias)

    def exibir_noticias(self):
        """Exibe notícias sobre transporte público na área designada.
        
        Obtém notícias da função notice_transp_sao_paulo() e as exibe em widgets
        individuais com links clicáveis.
        """
        noticias = notice_transp_sao_paulo()

        if noticias is not None:

            for i in reversed(range(self.news_layout.count())):
                self.news_layout.itemAt(i).widget().setParent(None)

            for index, row in noticias.iterrows():
                title = row['title']
                link = row['link']
                image_url = row.get('image_url')

                news_widget = NewsWidget(title, link, image_url)
                self.news_layout.addWidget(news_widget)

                separator = QFrame()
                separator.setFrameShape(QFrame.HLine)
                separator.setFrameShadow(QFrame.Sunken)
                separator.setStyleSheet("color: #555555;")
                self.news_layout.addWidget(separator)
        else:
            self.msg_noticias.setText("Nenhuma notícia encontrada.")

    def setup_line_buttons(self):
        """Configura os botões das linhas de transporte no painel direito.
        
        Carrega dados das linhas e cria botões coloridos para cada linha do metrô e trem.
        """
        base_path = os.path.dirname(os.path.abspath(__file__))
        mapa_path = base_path

        routes_path = os.path.join(
            mapa_path, 'Mapa_dos_Trilhos', 'Gtfs_SPTRANS', 'routes.txt')
        trajeto_path = os.path.join(
            mapa_path, 'Mapa_dos_Trilhos', 'Linhas', 'trajeto.json')

        self.routes = self.load_routes(os.path.normpath(routes_path))

        try:
            with open(trajeto_path, 'r', encoding='utf-8') as file:
                self.trajetos = json.load(file)
        except FileNotFoundError:
            print(f"[ERRO] Arquivo não encontrado: {trajeto_path}")
            self.trajetos = {}

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

        self.laranja = "#999999"
        self.ouro = "#999999"

        self.setup_line_button(
            "Azul", line1, self.cor_linha_01, "white", "L1", "1.png", "1_azul.png", "METRÔ")
        self.setup_line_button("Verde", line2, self.cor_linha_02,
                               "white", "L2", "2.png", "2_verde.png", "METRÔ")
        self.setup_line_button("Vermelha", line3, self.cor_linha_03,
                               "black", "L3", "3.png", "3_vermelha.png", "METRÔ")
        self.setup_line_button("Amarela", line4, self.cor_linha_04,
                               "black", "L4", "4.png", "4_amarela.png", "VIAQUATRO")
        self.setup_line_button("Lilás", line5, self.cor_linha_05,
                               "white", "L5", "5.png", "5_lilas.png", "VIAMOBILIDADE")
        self.setup_line_button(
            "Laranja", line6, self.laranja, "white", "L6", None, None, None)
        self.setup_line_button(
            "Rubi", line7, self.cor_linha_07, "white", "L07", "7.png", "cptm.png", "CPTM")
        self.setup_line_button("Diamante", line8, self.cor_linha_08,
                               "black", "L08", "8.png", "8_diamante.png", "VIAMOBILIDADE")
        self.setup_line_button("Esmeralda", line9, self.cor_linha_09,
                               "black", "L09", "9.png", "9_esmeralda.png", "VIAMOBILIDADE")
        self.setup_line_button("Turquesa", line10, self.cor_linha_10,
                               "black", "L10", "10.png", "cptm.png", "CPTM")
        self.setup_line_button(
            "Coral", line11, self.cor_linha_11, "black", "L11", "11.png", "cptm.png", "CPTM")
        self.setup_line_button("Safira", line12, self.cor_linha_12,
                               "white", "L12", "12.png", "cptm.png", "CPTM")
        self.setup_line_button(
            "Jade", line13, self.cor_linha_13, "black", "L13", "13.png", "cptm.png", "CPTM")
        self.setup_line_button("Prata", line15, self.cor_linha_15,
                               "black", "L15", "15.png", "15_prata.png", "METRÔ")
        self.setup_line_button("Ouro", line17, self.ouro,
                               "white", "L17", None, None, "VIAMOBILIDADE")

    def load_routes(self, filepath):
        """Carrega dados das rotas a partir de um arquivo routes.txt.
        
        Args:
            filepath: Caminho para o arquivo routes.txt
            
        Returns:
            dict: Dicionário com informações das rotas (origem e destino)
        """
        routes = {}

        if not os.path.exists(filepath):
            print(f"[ERRO] routes.txt não encontrado em: {filepath}")
            return routes

        with open(filepath, encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 4:
                    continue
                line_name = row[0].replace('"', '').strip()
                station_str = row[3].replace('"', '').strip()

                station_parts = [s.strip()
                                 for s in station_str.split(' - ') if s.strip()]
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
        """Configura um botão de linha de transporte com informações detalhadas.
        
        Args:
            text: Nome da linha
            command: Função a ser chamada no clique
            bg: Cor de fundo do botão
            fg: Cor do texto do botão
            route_key: Chave para buscar informações da rota
            colored_icon_path: Caminho para ícone colorido (opcional)
            icon_path: Caminho para ícone padrão (opcional)
            operator: Operadora da linha (opcional)
        """
        container = QWidget()
        container.setStyleSheet("background-color: transparent;")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(1, 0, 1, 0)
        layout.setSpacing(0)

        # Obtém o status real da linha
        line_status = self.get_line_status(text)

        # Cria o label de status com bordas arredondadas
        status_label = QLabel(f" {line_status} ")  # Espaços para melhor visualização
        status_label.setAlignment(Qt.AlignCenter)
        
        # Define a cor de fundo baseada no status
        if "Operação Normal" in line_status:
            bg_color = "#00AA00"  # Verde
        elif any(word in line_status for word in ["Paralisada", "Interrompida"]):
            bg_color = "#FF0000"  # Vermelho
        elif any(word in line_status for word in ["Velocidade reduzida", "Operação parcial", "Operação com Impacto Pontual", "Atividade Programada"]):
            bg_color = "#E5FF00" # Amarelo
        elif any(word in line_status for word in ["Dados Indisponíveis", "Em implantação", "Encerrada"]):
            bg_color = "#949494"  # Cinza
        else:
            bg_color = "#0073E6"  # Azul padrão

        # Aplica o estilo minimalista
        status_label.setStyleSheet(f"""
            QLabel {{
                background-color: {bg_color};
                color: black;
                font: bold 9pt;
                padding: 2px 8px;
                border-radius: 8px;
                min-width: 120px;
            }}
        """)
        
        layout.addWidget(status_label)

        button_row = QWidget()
        row_layout = QHBoxLayout(button_row)
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.setSpacing(0)

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

        operator_label = QLabel(operator if operator else "")
        operator_label.setStyleSheet("font: 9pt; color: #555;")
        operator_label.setFixedWidth(95)
        row_layout.addWidget(operator_label)

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

        layout.addWidget(button_row)
        layout.addWidget(separator)

        self.right_layout.addWidget(container)

    def setup_footer(self):
        """Configura o rodapé da janela principal.
        
        Adiciona informações de data/hora e condições climáticas atualizadas em tempo real.
        """
        footer = QWidget()
        footer.setStyleSheet("background-color: #333333;")
        footer_layout = QHBoxLayout(footer)

        self.datetime_label = QLabel()
        self.datetime_label.setStyleSheet("color: white; font: bold 12pt;")
        footer_layout.addWidget(self.datetime_label, alignment=Qt.AlignRight)

        # Obtem texto e ícone
        weather_data = get_weather()

        # Verifica se a resposta é válida (pode ser string em caso de erro)
        if isinstance(weather_data, tuple) and len(weather_data) == 2:
            weather_text, weather_icon = weather_data
        else:
            weather_text = weather_data if isinstance(weather_data, str) else "Dados indisponíveis"
            weather_icon = QPixmap()  # Ícone vazio

        # Layout horizontal para ícone + texto
        weather_layout = QHBoxLayout()

        # QLabel do ícone (agora como atributo da classe)
        self.icon_label = QLabel()
        self.icon_label.setPixmap(weather_icon.scaled(36, 36, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.icon_label.setFixedSize(40, 40)
        self.icon_label.setStyleSheet("margin-right: 6px;")

        # QLabel do texto
        self.temp_label = QLabel(weather_text)
        self.temp_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.temp_label.setWordWrap(True)
        self.temp_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 12pt; 
                font-weight: 600;
                font-family: "Segoe UI", "Arial", sans-serif;
                padding: 4px 8px;
                border-radius: 8px;
                background-color: rgba(255, 255, 255, 0.04);
            }
        """)

        # Adiciona ao layout
        weather_layout.addWidget(self.icon_label)
        weather_layout.addWidget(self.temp_label)
        weather_layout.addStretch()

        # Configuração do label de data/hora
        self.datetime_label = QLabel()
        self.datetime_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 11pt;
                font-weight: 500;
                font-family: "Segoe UI", "Arial", sans-serif;
                padding: 4px 8px;
                border-radius: 8px;
                background-color: rgba(255, 255, 255, 0.05);
            }
        """)
        self.datetime_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.update_datetime()

        # Adiciona ao footer_layout principal
        footer_layout.addLayout(weather_layout)
        footer_layout.addWidget(self.datetime_label, alignment=Qt.AlignLeft)  # Alinhado à esquerda

        self.right_layout.addWidget(footer)
        footer.setVisible(True)

    def update_temp(self):
        """Atualiza as informações de temperatura e clima no rodapé."""
        try:
            weather_data = get_weather()

            # Verifica se a resposta é válida
            if isinstance(weather_data, tuple) and len(weather_data) == 2:
                weather_text, weather_icon = weather_data
                self.temp_label.setText(weather_text)
                self.icon_label.setPixmap(
                    weather_icon.scaled(36, 36, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            else:
                error_msg = weather_data if isinstance(weather_data, str) else "Dados indisponíveis"
                self.temp_label.setText(error_msg)
                self.icon_label.clear()  # Limpa o ícone
        except Exception as e:
            print(f"Erro ao atualizar temperatura: {e}")
            self.temp_label.setText("Erro na atualização")
            self.icon_label.clear()

    def setup_updates(self):
        """Configura os timers para atualizações automáticas.
        
        Inicializa timers para atualização de:
        - Data e hora
        - Temperatura e clima
        - Status das linhas de transporte
        """
        self.datetime_timer = QTimer(self)
        self.datetime_timer.timeout.connect(self.update_datetime)
        self.datetime_timer.start(1000)

        self.temp_timer = QTimer(self)
        self.temp_timer.timeout.connect(self.update_temp)
        self.temp_timer.start(60000)

        # Timer para atualizar os status das linhas a cada 5 minutos
        self.status_timer = QTimer(self)
        self.status_timer.timeout.connect(self.update_line_statuses)
        self.status_timer.start(300000)  # 5 minutos em milissegundos
        self.update_line_statuses()  # Atualiza imediatamente

    def update_line_statuses(self):
        """Atualiza os status de todas as linhas de transporte.
        
        Percorre todos os widgets no painel direito para atualizar os status
        das linhas com base nos dados obtidos em tempo real.
        """
        logging.info("Atualizando status das linhas...")
        # Percorre todos os widgets no right_layout para atualizar os status
        for i in range(self.right_layout.count()):
            widget = self.right_layout.itemAt(i).widget()
            if widget:
                # Encontra o label de status (primeiro widget no layout vertical)
                status_label = widget.layout().itemAt(0).widget()
                if isinstance(status_label, QLabel) and status_label.text().startswith("Status:"):
                    # Extrai o nome da linha do botão (segundo widget no layout vertical)
                    button_row = widget.layout().itemAt(1).widget()
                    button = button_row.layout().itemAt(2).widget()  # O botão está na posição 2
                    if isinstance(button, QPushButton):
                        line_name = button.text()
                        line_status = self.get_line_status(line_name)

                        # Atualiza a cor com base no status
                        status_color = "#0073E6"  # Azul padrão
                        if "Operação Normal" in line_status:
                            status_color = "#00AA00"  # Verde
                        elif any(word in line_status for word in ["Paralisada", "Interrompida"]):
                            status_color = "#FF0000"  # Vermelho
                        elif any(word in line_status for word in ["Velocidade reduzida", "Operação parcial", "Operação com Impacto Pontual", "Atividade Programada"]):
                            status_color = "#E5FF00"  # Laranja
                        elif any(word in line_status for word in ["Dados Indisponíveis", "Em implantação", "Encerrada"]):
                            status_color = "#949494"  # Cinza

                        status_label.setText(f"{line_status}")
                        status_label.setStyleSheet(
                            f"font: bold 9pt; color: {status_color}; padding: 4px;")

    def update_datetime(self):
        """Atualiza a exibição de data e hora no rodapé."""
        now = QDateTime.currentDateTime()
        formatted_datetime = f"📅 {now.toString('dd/MM/yyyy')}\n🕒 {now.toString('HH:mm')}"
        self.datetime_label.setText(formatted_datetime)

    def keyPressEvent(self, event):
        """Trata eventos de teclado, especialmente o ESC para fechar a aplicação.
        
        Args:
            event: Evento de tecla pressionada
        """
        if event.key() == Qt.Key_Escape:
            # Cria uma caixa de diálogo de confirmação
            reply = QMessageBox.question(
                self,
                'Confirmação',
                'Tem certeza que deseja sair?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            # Se o usuário confirmar, fecha a aplicação
            if reply == QMessageBox.Yes:
                logging.info(f"Fechando Página Principal")
                self.close()

if __name__ == "__main__":
    try:
        os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"
        from PyQt5.QtCore import Qt
        from PyQt5.QtWidgets import QApplication

        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

        app = QApplication(sys.argv)

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
        from Pesquisa_pass.pesquisa_pass import passageiro_estacao
        from mapa import mapa_global
        from gtfs_emtu import emtu
        from gtfs_sptrans import sptrans
        from temperatura import get_weather
        from Guias.guias import *
        from qualidade_ar import mapa_qualidade_ar

        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        logging.critical(f"Erro não tratado: {str(e)}", exc_info=True)
        QMessageBox.critical(None, "Erro Fatal", f"Ocorreu um erro crítico:\n{str(e)}")