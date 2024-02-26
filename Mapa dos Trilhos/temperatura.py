import requests  # Importa o módulo requests para fazer requisições HTTP
from colorama import Fore, Back, Style, init # Importa as classes Fore, Back, Style e a função init do módulo colorama para formatação de texto colorido no terminal
from datetime import datetime # Importa a classe datetime do módulo datetime para trabalhar com datas e horas

# Define uma função para obter a hora atual e formatá-la
def obter_hora_atual():
    # Retorna a hora atual formatada como string no formato HH:MM:SS
    return datetime.now().strftime("%H:%M:%S")

# Imprime uma mensagem formatada no terminal com a hora atual
print(f"{Style.BRIGHT}{Fore.WHITE}Coletando informações de Temperatura às {Fore.GREEN}{obter_hora_atual()}{Style.RESET_ALL}")

# Define uma função para obter a temperatura atual de São Paulo a partir da API OpenWeatherMap
def get_weather():
    # Chave de API para acessar os dados meteorológicos
    api_key = '16771021c6dc278a8a9ebdb23e682e50'
    # URL da API com a cidade (São Paulo), chave de API e unidades métricas
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Sao%20Paulo&appid={api_key}&units=metric'
    # Faz uma requisição GET para a URL da API
    response = requests.get(url)
    # Converte a resposta da API em formato JSON
    weather_data = response.json()
    # Extrai a temperatura atual da resposta JSON
    temperature = weather_data['main']['temp']
    # Retorna a temperatura formatada como string com o símbolo de grau Celsius
    return f'{temperature} °C'