# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte público Metropolitano do Estado de São Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "22/07/2025 02:03"

DESCRITIVO:
MÃ³dulo de funcionalidades especÃ­ficas
ARQUITETURA:
    Mapa_dos_Trilhos/noticia.py
"""

from GoogleNews import GoogleNews
import pandas as pd

def notice_transp_sao_paulo():
    """Coleta as últimas notícias sobre transporte público em São Paulo.
    
    Realiza uma busca no Google News por notícias publicadas nas últimas 24 horas
    relacionadas ao transporte público na região metropolitana de São Paulo.
    
    Returns:
        pandas.DataFrame or None: Um DataFrame contendo as notícias encontradas com as colunas:
            - title: Título da notícia
            - link: URL da notícia
            - date: Data de publicação formatada
            - desc: Descrição/resumo da notícia
            - media: Veículo de comunicação que publicou
            - datetime: Data e hora completa da publicação
            - img: URL da imagem associada (quando disponível)
            
        Retorna None caso nenhuma notícia seja encontrada.
        
    Raises:
        Exception: Possíveis erros na conexão com a API do Google News ou no processamento dos dados
        
    Exemplo:
        >>> noticias = notice_transp_sao_paulo()
        >>> if noticias is not None:
        ...     print(noticias.head())
    """
    try:
        # Configuração da busca no Google News
        googlenews = GoogleNews(period='d')  # 'd' para buscar notícias do último dia
        googlenews.setlang('pt')  # Filtra apenas notícias em português
        
        # Realiza a busca com o termo específico
        googlenews.search('Transporte Público São Paulo')
        
        # Obtém os resultados da busca
        result = googlenews.result()

        # Processa os resultados se encontrados
        if result:
            # Converte para DataFrame e seleciona colunas relevantes
            df = pd.DataFrame(result)
            df_filtered = df[['title', 'link', 'date', 'desc', 'media', 'datetime', 'img']].head(50)
            return df_filtered
        else:
            print("Nenhuma notícia encontrada nas últimas 24 horas.")
            return None
            
    except Exception as e:
        print(f"Erro ao buscar notícias: {str(e)}")
        return None