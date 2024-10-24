import requests
from datetime import datetime
import time  # Importa o módulo time para gerenciar intervalos

# Chave de API
API_KEY = '16771021c6dc278a8a9ebdb23e682e50'

def get_weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Sao%20Paulo&appid={API_KEY}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    return f'{temperature} °C'

def main():
    while True:
        temperature = get_weather()
        print(f'Temperatura Atual: {temperature} - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        time.sleep(10)  # Aguarda 10 segundos antes de atualizar

if __name__ == "__main__":
    main()