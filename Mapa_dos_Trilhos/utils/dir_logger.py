# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte público Metropolitano do Estado de São Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.4"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "22/07/2025 17:19"

DESCRITIVO:
MÃ³dulo de funcionalidades especÃ­ficas
ARQUITETURA:
    Mapa_dos_Trilhos/utils/dir_logger.py
"""
import logging
from pathlib import Path

class DirectoryLogger:
    """Classe para registro e monitoramento de diretórios acessados.
    
    Atributos de Classe:
        _logged_dirs (set): Conjunto de diretórios já registrados em log
        
    Métodos:
        log_directory: Registra informações sobre um diretório
    """
    _logged_dirs = set()

    @classmethod
    def log_directory(cls, path):
        """Registra informações sobre um diretório no log de debug.
        
        Args:
            path (str or Path): Caminho do diretório a ser registrado
            
        Returns:
            bool: True se o diretório foi registrado com sucesso, False se já estava registrado
                  ou ocorreu um erro
                  
        Comportamento:
            - Converte o caminho para Path absoluto
            - Verifica se o diretório já foi registrado
            - Conta os arquivos no diretório
            - Registra no log com formato: "DIR: {path} | Arquivos: {count}"
            - Adiciona o diretório ao conjunto de diretórios registrados
            - Captura e loga exceções como warnings
            
        Exemplo:
            >>> DirectoryLogger.log_directory('/caminho/do/diretorio')
            True
        """
        path = Path(path).resolve()
        if str(path) not in cls._logged_dirs:
            try:
                file_count = len(list(path.glob('*')))
                logging.getLogger('SP4U.debug').debug(
                    f"DIR: {path} | Arquivos: {file_count}"
                )
                cls._logged_dirs.add(str(path))
                return True
            except Exception as e:
                logging.getLogger('SP4U.debug').warning(
                    f"Falha ao verificar diretório {path}: {str(e)}"
                )
        return False