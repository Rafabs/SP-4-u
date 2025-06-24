import requests
from datetime import datetime
import time
import pytz  # Adicionado para tratamento de fuso horário
import sys
from pathlib import Path

# Adiciona o diretório raiz ao PATH
from Mapa_dos_Trilhos.Sobre.config import API_TOKEN_QUALLITY_AR

def get_weather():
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q=Sao%20Paulo&appid={API_TOKEN_QUALLITY_AR}&units=metric&lang=pt'
        response = requests.get(url)
        response.raise_for_status()  # Levanta exceção para erros HTTP
        weather_data = response.json()
        
        temperature = weather_data['main']['temp']
        
        # Obtém o horário de São Paulo
        tz = pytz.timezone('America/Sao_Paulo')
        now = datetime.now(tz).strftime("%H:%M")
        print(url)
        return f'{temperature:.1f}°C'
        
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return "Dados indisponíveis"
    except (KeyError, ValueError) as e:
        print(f"Erro ao processar dados: {e}")
        return "Dados incompletos"

def main():
    while True:
        weather_info = get_weather()
        print(f'Tempo em SP: {weather_info}')
        time.sleep(600)  # Atualiza a cada 10 minutos

if __name__ == "__main__":
    main()