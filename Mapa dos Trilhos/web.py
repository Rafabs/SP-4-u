from selenium import webdriver
from bs4 import BeautifulSoup

def status():
    # Inicializa o driver do Chrome
    driver = webdriver.Chrome()

    # Abre a página
    driver.get("https://www.viamobilidade.com.br/")

    # Obtém o HTML da página
    html_content = driver.page_source

    # Fecha o driver
    driver.quit()

    # Faz o parse do HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Encontra as informações das linhas e operações
    linhas = [linha.span["title"] for linha in soup.select("li[class^='col-12 p-0 line-']")]
    status = [status.text for status in soup.select("li[class^='col-12 p-0 line-'] .status")]
    
    # Encontra as mensagens
    mensagens = soup.select(".msg")

    lista_mensagens = []

    # Verifica se existem mensagens
    if mensagens:
        # Adiciona as mensagens a uma lista
        for msg in mensagens:
            titulo = msg.find("h4").text
            texto = msg.find("p").text
            lista_mensagens.append(f"{titulo}: {texto}")
    else:
        lista_mensagens.append(f"Nenhuma ocorrência no momento.")

    return linhas, status, lista_mensagens