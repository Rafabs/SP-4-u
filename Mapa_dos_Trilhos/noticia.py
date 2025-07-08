# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte pÃºblico Metropolitano do Estado de SÃ£o Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "30/06/2025 00:42"

DESCRITIVO:
MÃ³dulo de funcionalidades especÃ­ficas
ARQUITETURA:
    Mapa_dos_Trilhos/noticia.py
"""
from GoogleNews import GoogleNews # Importa a classe GoogleNews do módulo GoogleNews para buscar notícias
import pandas as pd # Importa a classe pandas do módulo pandas para manipulação de dados em formato tabular

# Define uma função chamada notice_transp_sao_paulo
def notice_transp_sao_paulo():
    # Cria uma instância do GoogleNews com o período definido como 'd' (dia)
    googlenews = GoogleNews(period='d')
    # Define o idioma da pesquisa como português
    googlenews.setlang('pt')
    # Realiza uma pesquisa por notícias relacionadas ao "Transporte Público São Paulo"
    googlenews.search('Transporte Público São Paulo')
    # Obtém os resultados da pesquisa
    result = googlenews.result()

    # Verifica se há resultados antes de criar o DataFrame
    if result:
        # Converte os resultados em um DataFrame do pandas
        df = pd.DataFrame(result)
        # Seleciona apenas as colunas relevantes do DataFrame
        df_filtered = df[['title', 'link', 'date', 'desc', 'media', 'datetime', 'img']].head(50)
        # Retorna o DataFrame filtrado
        return df_filtered
    else:
        # Se não houver resultados, exibe uma mensagem indicando que nenhuma notícia foi encontrada
        print("Nenhuma notícia encontrada.")