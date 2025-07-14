# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte pÃºblico Metropolitano do Estado de SÃ£o Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.4"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "08/07/2025 01:41"

DESCRITIVO:
MÃ³dulo de funcionalidades especÃ­ficas
ARQUITETURA:
    Mapa_dos_Trilhos/utils/dir_logger.py
"""
import logging
from pathlib import Path

class DirectoryLogger:
    _logged_dirs = set()

    @classmethod
    def log_directory(cls, path):
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