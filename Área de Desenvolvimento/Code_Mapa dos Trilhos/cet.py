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

'''Para testes isolados nesse código, desmarque as 4 linhas abaixo.'''
# Chama a função 'transito' para obter as velocidades
transito() 
# Obtém os resultados das velocidades para 'CentroBairro' e 'BairroCentro'
resultado_CentroBairro, resultado_BairroCentro = transito()
# Imprime as velocidades obtidas para 'CentroBairro'
print("Velocidades Centro para Bairro:", resultado_CentroBairro)
# Imprime as velocidades obtidas para 'BairroCentro'
print("Velocidades Bairro para Centro:", resultado_BairroCentro)

def cet_cores():
    # Define a URL da página que contém as informações sobre as cores da CET
    url = 'http://www.cetsp.com.br/transito-agora/transito-nas-principais-vias.aspx'
    # Faz uma requisição GET para obter o conteúdo da página
    page = requests.get(url)
    # Cria um objeto BeautifulSoup para analisar o conteúdo HTML da página
    soup = BeautifulSoup(page.content, 'html.parser')

    # Dicionário com as cores correspondentes às regiões
    colors = {
        'Norte': 'blue',
        'Oeste': 'orange',
        'Centro': 'white',
        'Leste': 'yellow',
        'Sul': 'cyan'
    }

    items = []

    # Itera sobre as regiões e suas cores correspondentes
    for region, color in colors.items():
        # Encontra o link da região na página
        region_link = soup.find('a', href=f"/transito-agora/{region.lower()}/mapa-de-fluidez.aspx")
        # Se o link for encontrado, adiciona a região e sua cor à lista de itens
        if region_link:
            items.append((region, color))

    return items

# Chama a função 'cet_cores' para obter as cores das regiões da CET
test_dados = cet_cores()
# Imprime os dados obtidos
print(test_dados)