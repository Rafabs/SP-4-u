# Mapa_dos_Trilhos/utils/logger_config.py
import logging
import sys
from pathlib import Path

class StreamToLogger:
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            if self.log_level == logging.WARNING:
                self.logger.warning(line.rstrip())
            elif self.log_level == logging.DEBUG:
                self.logger.debug(line.rstrip())
            elif self.log_level == logging.CRITICAL:
                self.logger.critical(line.rstrip())
            else:
                self.logger.info(line.rstrip())

    def flush(self):
        pass

def configurar_logger():
    # Define onde o log vai ser salvo
    BASE_DIR = Path(__file__).resolve().parent.parent
    LOG_DIR = BASE_DIR / "Mapa_dos_Trilhos"
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    LOG_FILE = LOG_DIR / "log.log"

    logging.basicConfig(
        filename=str(LOG_FILE),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    sys.stdout = StreamToLogger(logging.getLogger('STDOUT'), logging.INFO)
    sys.stderr = StreamToLogger(logging.getLogger('STDERR'), logging.ERROR)
