import requests  # Requisições HTTP
from colorama import Fore, Back, Style, init
from datetime import datetime

# Obtém a hora atual
def obter_hora_atual():
    return datetime.now().strftime("%H:%M:%S")

# Imprime o texto formatado
print(f"{Style.BRIGHT}{Fore.WHITE}Coletando informações de Temperatura às {Fore.GREEN}{obter_hora_atual()}{Style.RESET_ALL}")

def get_weather():
    
    api_key = '16771021c6dc278a8a9ebdb23e682e50'
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Sao%20Paulo&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    return f'{temperature} °C'
