from selenium import webdriver # Importa o módulo WebDriver do Selenium para automação de navegador web
from bs4 import BeautifulSoup # Importa a classe BeautifulSoup do módulo bs4 para fazer o parsing do HTML

# Define uma função para obter o status das linhas e operações de transporte
def status():
    # Inicializa o driver do Chrome
    driver = webdriver.Chrome()

    # Abre a página desejada
    driver.get("https://www.viamobilidade.com.br/")

    # Obtém o HTML da página carregada
    html_content = driver.page_source

    # Fecha o driver após obter o HTML
    driver.quit()

    # Faz o parsing do HTML com BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Encontra as informações das linhas e seus status
    linhas = [linha.span["title"] for linha in soup.select("li[class^='col-12 p-0 line-']")]
    status = [status.text for status in soup.select("li[class^='col-12 p-0 line-'] .status")]
    
    # Encontra as mensagens de status
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
        # Se não houver mensagens, adiciona uma mensagem indicando isso à lista
        lista_mensagens.append(f"Nenhuma ocorrência no momento.")

    # Retorna as listas de linhas, status e mensagens
    return linhas, status, lista_mensagens

# Comentário para instruir a desmarcação das linhas de código abaixo para testes isolados
#status() 
resultado_linhas, resultado_status, resultado_mensagens = status()
# Imprime os resultados um abaixo do outro
for i in range(len(resultado_linhas)):
    print("Linhas:", resultado_linhas[i])
    print("Status:", resultado_status[i])
    if i < len(resultado_mensagens):
        print("Mensagens:", resultado_mensagens[i])
    print()