# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte público Metropolitano do Estado de São Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "22/07/2025 17:18"

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
    """Classe para configuração otimizada de logging do projeto SP4U.
    
    Atributos:
        logger (logging.Logger): Instância do logger configurado
    """
    
    def __init__(self):
        """Inicializa o logger com configurações padrão do projeto."""
        self.logger = logging.getLogger('SP4U')
        self.logger.setLevel(logging.INFO)
        self._configure_handlers()
        
    def _configure_handlers(self):
        """Configura os handlers de logging para arquivo e console.
        
        Realiza:
        - Remove handlers existentes
        - Cria diretório de logs se não existir
        - Configura handler para arquivo com formatação detalhada
        - Configura handler para console apenas para níveis WARNING+
        """
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
    """Função principal para configuração do logger do sistema.
    
    Returns:
        logging.Logger: Instância do logger configurado
        
    Configura:
        - Handlers para arquivo e console
        - Captura de exceções não tratadas
        - Formatação padronizada
        
    Exemplo:
        >>> logger = configurar_logger()
        >>> logger.info("Mensagem informativa")
    """
    logger = OptimizedLogger().logger
    
    # Redirecionamento seguro de exceções
    def handle_exception(exc_type, exc_value, exc_traceback):
        """Handler para captura de exceções não tratadas."""
        logger.error("Exceção não capturada", 
                    exc_info=(exc_type, exc_value, exc_traceback))
    
    sys.excepthook = handle_exception
    
    return logger