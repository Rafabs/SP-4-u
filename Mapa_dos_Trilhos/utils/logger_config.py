# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte pÃºblico Metropolitano do Estado de SÃ£o Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
$128/06/2025 15:56"

DESCRITIVO:
MÃ³dulo de funcionalidades especÃ­ficas
ARQUITETURA:
    Mapa_dos_Trilhos/utils/logger_config.py
"""
import logging
from pathlib import Path
import sys
from datetime import datetime

class OptimizedLogger:
    def __init__(self):
        self.logger = logging.getLogger('SP4U')
        self.logger.setLevel(logging.INFO)
        self._configure_handlers()
        
    def _configure_handlers(self):
        # Remove handlers existentes
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
            
        # Configura arquivo de log
        log_dir = Path(__file__).parent.parent.parent / "logs"
        log_dir.mkdir(exist_ok=True)
        
        file_handler = logging.FileHandler(
            filename=log_dir / f"exec_{datetime.now().strftime('%Y%m%d_%H%M')}.log",
            encoding='utf-8'
        )
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', 
                           datefmt='%Y-%m-%d %H:%M:%S')
        )
        self.logger.addHandler(file_handler)
        
        # Console somente para erros
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        self.logger.addHandler(console_handler)

def configurar_logger():
    logger = OptimizedLogger().logger
    
    # Redirecionamento seguro de exceções
    def handle_exception(exc_type, exc_value, exc_traceback):
        logger.error("Exceção não capturada", 
                    exc_info=(exc_type, exc_value, exc_traceback))
    
    sys.excepthook = handle_exception
    
    return logger