# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte público Metropolitano do Estado de São Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "22/07/2025 18:08"

DESCRITIVO:
MÃ³dulo de funcionalidades especÃ­ficas
ARQUITETURA:
    Mapa_dos_Trilhos/Guias/guias.py
"""
import fitz 
from PIL import Image, ImageTk 
from colorama import Fore, Back, Style, init 
from datetime import datetime 

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def mapa_rede():
    """
    Exibe o mapa da rede metroviária em formato PDF.
    
    Esta função abre o arquivo PDF contendo o mapa da rede do metrô,
    converte a primeira página para uma imagem e a exibe para o usuário.
    Também registra no console o horário de início da operação.
    """
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
    """
    Exibe o guia do passageiro do metrô em português (PT-BR).
    
    Abre o arquivo PDF do guia oficial do metrô na versão em português,
    converte a primeira página para imagem e a exibe para o usuário.
    Registra no console o horário de início da operação.
    """
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
    """
    Exibe o guia do passageiro do metrô em inglês (EN-US).
    
    Abre o arquivo PDF do guia oficial do metrô na versão em inglês,
    converte a primeira página para imagem e a exibe para o usuário.
    Registra no console o horário de início da operação.
    """
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
    """
    Exibe o guia regulamentar da CPTM (Companhia Paulista de Trens Metropolitanos).
    
    Abre o arquivo PDF contendo as regulamentações de viagem da CPTM,
    converte a primeira página para imagem e a exibe para o usuário.
    Registra no console o horário de início da operação.
    """
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
    """
    Exibe o guia do Expresso Turístico da CPTM.
    
    Abre o arquivo PDF contendo as regulamentações específicas do Expresso Turístico,
    converte a primeira página para imagem e a exibe para o usuário.
    Registra no console o horário de início da operação.
    """
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