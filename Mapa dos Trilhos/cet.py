from bs4 import BeautifulSoup  # Importa a classe BeautifulSoup do módulo bs4 para realizar web scraping
import requests  # Importa o módulo requests para realizar requisições HTTP
 
def transito():
    # Define a URL do site da CET
    cet = (f'http://www.cetsp.com.br/')
    # Faz uma requisição GET para obter o conteúdo da página
    pagina = requests.get(cet)
    # Cria um objeto BeautifulSoup para analisar o conteúdo HTML da página
    soup_transito = BeautifulSoup(pagina.content, 'html.parser')
    # Seleciona os elementos HTML com a classe 'CentroBairro'
    indicador_CentroBairro = soup_transito.select('.CentroBairro')
    # Seleciona os elementos HTML com a classe 'BairroCentro'
    indicador_BairroCentro = soup_transito.select('.BairroCentro')

    # Extrai as velocidades da lista de elementos selecionados para 'CentroBairro' e 'BairroCentro'
    vel_CentroBairro = list(map(lambda status: status.select(
        '.valor')[0].text, indicador_CentroBairro))
    vel_BairroCentro = list(map(lambda status: status.select(
        '.valor')[0].text, indicador_BairroCentro))

    return vel_CentroBairro, vel_BairroCentro