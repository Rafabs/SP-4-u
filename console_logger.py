from PyQt5.QtWidgets import QPlainTextEdit, QApplication
from PyQt5.QtCore import Qt, QTimer, QObject, pyqtSignal
from PyQt5.QtGui import QTextCursor, QColor, QTextCharFormat, QFont
import logging
from datetime import datetime
import sys

class ConsoleSignals(QObject):
    """Sinais para comunicação thread-safe"""
    log_received = pyqtSignal(str, str)  # level, message

class ConsoleLogHandler(logging.Handler):
    """Handler personalizado para enviar logs ao widget de console"""
    def __init__(self, console_widget):
        super().__init__()
        self.console_widget = console_widget
        self.setFormatter(logging.Formatter('%(message)s'))
        
    def emit(self, record):
        """Envia a mensagem de log para o widget de console"""
        try:
            msg = self.format(record)
            self.console_widget.append_log(record.levelname, msg)
        except Exception as e:
            sys.__stderr__.write(f"Erro no ConsoleLogHandler: {str(e)}\n")

class ConsoleLogger(QPlainTextEdit):
    """Widget de console com cores diferenciadas para timestamp, nível e mensagem"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.signals = ConsoleSignals()
        self._setup_format_palette()  # Configura paleta de cores
        self._initialize_ui()
        self._initialize_logging()
        self._setup_auto_scroll()
        
    def _setup_format_palette(self):
        """Configura as cores para cada parte do log"""
        # Formato base (comum a todas as partes)
        self.base_format = QTextCharFormat()
        self.base_format.setFontFamily("Consolas")
        self.base_format.setFontPointSize(10)
        
        # Cores específicas para cada componente
        self.timestamp_format = QTextCharFormat(self.base_format)
        self.timestamp_format.setForeground(QColor('#888888'))  # Cinza médio
        
        self.level_formats = {
            'INFO': self._create_level_format('#2ECC71'),      # Verde
            'WARNING': self._create_level_format('#F39C12'),   # Laranja
            'ERROR': self._create_level_format('#E74C3C'),     # Vermelho
            'CRITICAL': self._create_level_format('#E74C3C', bold=True),
            'DEBUG': self._create_level_format('#3498DB'),     # Azul
            'STDOUT': self._create_level_format('#ECF0F1'),    # Branco
            'STDERR': self._create_level_format('#E74C3C')     # Vermelho
        }
        
        self.message_format = QTextCharFormat(self.base_format)
        self.message_format.setForeground(QColor('#DDDDDD'))  # Branco acinzentado
        
    def _create_level_format(self, color, bold=False):
        """Cria formatação para o nível do log"""
        fmt = QTextCharFormat(self.base_format)
        fmt.setForeground(QColor(color))
        if bold:
            fmt.setFontWeight(QFont.Bold)
        return fmt
        
    def _initialize_ui(self):
        """Configura a aparência do widget"""
        self.setReadOnly(True)
        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.setStyleSheet("""
            QPlainTextEdit {
                background-color: #1A1A1A;
                border: 1px solid #333;
                padding: 5px;
            }
        """)
        self.setMaximumHeight(250)
        self.log_buffer = []
        
    def _initialize_logging(self):
        """Configura o handler de logging"""
        console_handler = ConsoleLogHandler(self)
        console_handler.setLevel(logging.INFO)
        logging.getLogger().addHandler(console_handler)
        self.signals.log_received.connect(self._append_log_threadsafe)

    def _setup_auto_scroll(self):
        """Configura o sistema de auto-scroll"""
        self.auto_scroll = True
        self.user_scrolled = False
        self.scroll_bar = self.verticalScrollBar()
        self.scroll_bar.valueChanged.connect(self._check_scroll_position)
        self.buffer_timer = QTimer(self)
        self.buffer_timer.timeout.connect(self._flush_buffer)
        self.buffer_timer.start(100)

    def _append_log_threadsafe(self, level, message):
        """Adiciona log ao buffer de forma thread-safe"""
        try:
            safe_msg = self._process_message(message)
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.log_buffer.append((level, timestamp, safe_msg))
            
            if len(self.log_buffer) > 1000:
                self.log_buffer.pop(0)
        except Exception as e:
            error_msg = f"[ERROR] Falha ao processar log: {str(e)}"
            self.log_buffer.append(('ERROR', datetime.now().strftime("%H:%M:%S"), error_msg))

    def _process_message(self, message):
        """Processa a mensagem para exibição segura"""
        if not isinstance(message, str):
            try:
                message = str(message)
            except:
                message = "[MENSAGEM NÃO LEGÍVEL]"
        return ' '.join(message.split())

    def _flush_buffer(self):
        """Exibe os logs do buffer com formatação diferenciada"""
        if not self.log_buffer:
            return
            
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.End)
        
        for level, timestamp, message in self.log_buffer:
            # Timestamp (cinza)
            cursor.setCharFormat(self.timestamp_format)
            cursor.insertText(f"[{timestamp}] ")
            
            # Nível do log (colorido)
            cursor.setCharFormat(self.level_formats.get(level, self.level_formats['INFO']))
            cursor.insertText(f"[{level}] ")
            
            # Mensagem (branco)
            cursor.setCharFormat(self.message_format)
            cursor.insertText(f"{message}\n")
            
        self.log_buffer.clear()
        
        if self.auto_scroll and not self.user_scrolled:
            self.ensureCursorVisible()
        
    def _check_scroll_position(self, value):
        """Verifica se o usuário está rolando manualmente"""
        max_scroll = self.scroll_bar.maximum()
        self.user_scrolled = value < max_scroll - 10

    def append_log(self, level, message):
        """Interface pública para adicionar logs"""
        self.signals.log_received.emit(level, message)

    def copy_to_clipboard(self):
        """Copia todo o conteúdo do console para a área de transferência"""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.toPlainText())

    def clear(self):
        """Limpa todo o conteúdo do console"""
        super().clear()
        self.log_buffer.clear()