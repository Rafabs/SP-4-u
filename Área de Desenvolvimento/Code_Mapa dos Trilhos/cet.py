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

'''Para testes isolados nesse código, desmarque as 4 linhas abaixo.'''
transito() 
resultado_CentroBairro, resultado_BairroCentro = transito()
print("Velocidades Centro para Bairro:", resultado_CentroBairro)
print("Velocidades Bairro para Centro:", resultado_BairroCentro)

def cet_cores():
    url = 'http://www.cetsp.com.br/transito-agora/transito-nas-principais-vias.aspx'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    colors = {
        'Norte': 'blue',
        'Oeste': 'orange',
        'Centro': 'white',
        'Leste': 'yellow',
        'Sul': 'cyan'
    }

    items = []

    for region, color in colors.items():
        region_link = soup.find('a', href=f"/transito-agora/{region.lower()}/mapa-de-fluidez.aspx")
        if region_link:
            items.append((region, color))

    return items

test_dados = cet_cores()
print(test_dados)