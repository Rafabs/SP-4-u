# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte pÃºblico Metropolitano do Estado de SÃ£o Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "14/07/2025 18:02"

DESCRITIVO:
MÃ³dulo de funcionalidades especÃ­ficas
ARQUITETURA:
    Mapa_dos_Trilhos/Guias/guias.py
"""
import fitz # Importa fitz para trabalhar com arquivos PDF
from PIL import Image, ImageTk # Importa Image e ImageTk do PIL para manipular imagens
from colorama import Fore, Back, Style, init # Importa as cores do módulo colorama para colorir o texto no console
from datetime import datetime # Importa datetime do módulo datetime para obter a hora atual

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def mapa_rede():
    # Abre o arquivo PDF do mapa da rede do metrô
    pdf = fitz.open('Mapa_dos_Trilhos/Dados/mapa-da-rede-metro.pdf')
    # Obtém a imagem da primeira página do PDF
    imagem = pdf[0].get_pixmap()
    # Converte a imagem para o formato PIL
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    # Mostra a imagem
    imagem_pil.show()
    # Imprime o texto formatado indicando o início do processo
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da Rede iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")

def guia_pt_metro():
    # Abre o arquivo PDF do guia do passageiro do metrô em PT/BR
    pdf = fitz.open('Mapa_dos_Trilhos/Dados/Guia_do_passageiro_abr_2022.pdf')
    # Obtém a imagem da primeira página do PDF
    imagem = pdf[0].get_pixmap()
    # Converte a imagem para o formato PIL
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    # Mostra a imagem
    imagem_pil.show()
    # Imprime o texto formatado indicando o início do processo
    print(f"{Style.BRIGHT}{Fore.WHITE}Guia do Metrô em PT/BR iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")

def guia_en_metro():
    # Abre o arquivo PDF do guia do passageiro do metrô em EN/US
    pdf = fitz.open('Mapa_dos_Trilhos/Dados/Desktop_Guide_abr_2022_v2.pdf')
    # Obtém a imagem da primeira página do PDF
    imagem = pdf[0].get_pixmap()
    # Converte a imagem para o formato PIL
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    # Mostra a imagem
    imagem_pil.show()
    # Imprime o texto formatado indicando o início do processo
    print(f"{Style.BRIGHT}{Fore.WHITE}Guia do Metrô em EN/US iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")

def guia_cptm():
    # Abre o arquivo PDF do guia da CPTM
    pdf = fitz.open('Mapa_dos_Trilhos/Dados/Regulamento-Viagem.pdf')
    # Obtém a imagem da primeira página do PDF
    imagem = pdf[0].get_pixmap()
    # Converte a imagem para o formato PIL
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    # Mostra a imagem
    imagem_pil.show()
    # Imprime o texto formatado indicando o início do processo
    print(f"{Style.BRIGHT}{Fore.WHITE}Guia da CPTM iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")

def guia_cptm_expresso_turistico():
    # Abre o arquivo PDF do guia do expresso turístico da CPTM
    pdf = fitz.open('Mapa_dos_Trilhos/Dados/Regulamento de Viagem Expresso Turístico.pdf')
    # Obtém a imagem da primeira página do PDF
    imagem = pdf[0].get_pixmap()
    # Converte a imagem para o formato PIL
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    # Mostra a imagem
    imagem_pil.show()
    # Imprime o texto formatado indicando o início do processo
    print(f"{Style.BRIGHT}{Fore.WHITE}Guia do Expresso Turístico iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")