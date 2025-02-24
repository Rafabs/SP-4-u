import webbrowser  # Importa o módulo webbrowser para abrir páginas da web
import folium  # Importa o módulo folium para criar mapas interativos
import geopandas as gpd  # Importa o módulo geopandas para trabalhar com dados geoespaciais
import json  # Importa o módulo json para trabalhar com dados no formato JSON
from folium.plugins import MarkerCluster, Draw, MousePosition  # Importa algumas funcionalidades específicas do folium
from datetime import datetime  # Importa a classe datetime do módulo datetime para trabalhar com datas e horas
import csv  # Importa o módulo csv para trabalhar com arquivos CSV (Comma Separated Values)
from pyproj import Transformer  # Importa a classe Transformer do módulo pyproj para realizar transformações de coordenadas
import os  # Importa o módulo os para interagir com o sistema operacional
import requests  # Importa o módulo requests para fazer requisições HTTP
import certifi  # Importa o módulo certifi para lidar com certificados SSL
import logging  # Importa o módulo logging para registrar mensagens de log
from screeninfo import get_monitors
import tkinter as tk

# Configuração do logger
logging.basicConfig(filename='Mapa_dos_Trilhos\\log.txt', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s') 

def passageiro_estacao():

    logging.info(f"Abrindo Mapa da Pesquisa Origem e Destino")
    
    # Coordenadas do centro de São Paulo
    latitude = -23.550520
    longitude = -46.633308
    root = tk.Toplevel()
    monitor = get_monitors()[0]
    screen_width = monitor.width
    screen_height = monitor.height
    root.geometry(f"{screen_width}x{screen_height}")
    root.attributes("-fullscreen", True)
    root.overrideredirect(True)
    root.title("Mapa da Pesquisa Origem e Destino")
        
    def sair(event=None):
        root.destroy()
        logging.info(f"Fechando Mapa da Pesquisa Origem e Destino")    

    root.bind("<Escape>", sair)

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    passageiro_estacao()