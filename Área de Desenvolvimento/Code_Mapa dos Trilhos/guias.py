import fitz
from PIL import Image, ImageTk  # Manipular imagens
from colorama import Fore, Back, Style, init
from datetime import datetime

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def mapa_rede():
    pdf = fitz.open('Mapa dos Trilhos\\Data\\mapa-da-rede-metro.pdf')
    imagem = pdf[0].get_pixmap()
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    imagem_pil.show()
    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa da Rede iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")
    
def guia_pt_metro():
    pdf = fitz.open('Mapa dos Trilhos\\Data\\Guia_do_passageiro_abr_2022.pdf')
    imagem = pdf[0].get_pixmap()
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    imagem_pil.show()
    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Guia do Metrô em PT/BR iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")

def guia_en_metro():
    pdf = fitz.open('Mapa dos Trilhos\\Data\\Desktop_Guide_abr_2022_v2.pdf')
    imagem = pdf[0].get_pixmap()
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    imagem_pil.show()
    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Guia do Metrô em EN/US iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")

def guia_cptm():
    pdf = fitz.open('Mapa dos Trilhos\\Data\\Regulamento-Viagem.pdf')
    imagem = pdf[0].get_pixmap()
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    imagem_pil.show()
    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Guia da CPTM iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")

def guia_cptm_expresso_turistico():
    pdf = fitz.open('Mapa dos Trilhos\\Data\\Regulamento de Viagem Expresso Turístico.pdf')
    imagem = pdf[0].get_pixmap()
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    imagem_pil.show()
    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Guia do Expresso Turístico iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")

'''Para testes isolados nesse código, desmarque a função em que esteja trabalhando.'''

#mapa_rede()
#guia_pt_metro()
#guia_en_metro()
#guia_cptm()
#guia_cptm_expresso_turistico()
