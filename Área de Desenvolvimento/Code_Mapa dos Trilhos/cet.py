from bs4 import BeautifulSoup  # Web scraping
import requests  # Requisições HTTP

def transito():
    cet = (f'http://www.cetsp.com.br/')
    pagina = requests.get(cet)
    soup_transito = BeautifulSoup(pagina.content, 'html.parser')
    indicador_CentroBairro = soup_transito.select('.CentroBairro')
    indicador_BairroCentro = soup_transito.select('.BairroCentro')

    vel_CentroBairro = list(map(lambda status: status.select(
        '.valor')[0].text, indicador_CentroBairro))
    vel_BairroCentro = list(map(lambda status: status.select(
        '.valor')[0].text, indicador_BairroCentro))

    return vel_CentroBairro, vel_BairroCentro