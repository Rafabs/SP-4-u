# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte pÃºblico Metropolitano do Estado de SÃ£o Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "30/06/2025 00:38"

DESCRITIVO:
MÃ³dulo de funcionalidades especÃ­ficas
ARQUITETURA:
    Mapa_dos_Trilhos/mapa.py
"""
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
from datetime import datetime, timedelta  # Importa novamente a classe datetime e a classe timedelta para manipulação de datas
from colorama import Fore, Back, Style, init  # Importa algumas funcionalidades para manipulação de cores no terminal
import certifi  # Importa o módulo certifi para lidar com certificados SSL
from Mapa_dos_Trilhos.Sobre.config import API_TOKEN_QUALITY_AR  # Importa o token da API do arquivo de configuração

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

def mapa_global():

    # Imprime o texto formatado
    print(f"{Style.BRIGHT}{Fore.WHITE}Mapa iniciado às {Fore.GREEN}{hora_atual}{Fore.WHITE}, aguarde{Style.RESET_ALL}")
    
    # Coordenadas do centro de São Paulo
    latitude = -23.550520
    longitude = -46.633308

    # Função para carregar dados de um arquivo JSON
    def carregar_dados_arquivo(caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)

    def criar_mapa(latitude, longitude, zoom):
        return folium.Map(location=[latitude, longitude], zoom_start=zoom)

    def adicionar_linha_no_mapa(geom, construcao, linha, abertura, system, cores_linhas, mapa):
        cor = None
        for linha_info in cores_linhas:
            if linha_info['name'] == linha:
                cor = linha_info['color']
                break
        if cor is None:
            cor = 'black'
        
        peso = 5 if system == 'Metroferroviário' else 2 if system == 'Metrorrodoviário' else 3
        folium.PolyLine(
            locations=[(coord[1], coord[0]) for coord in geom.coords],
            color=cor,
            weight=peso,
            popup=folium.Popup(
                f"<b>Construção: </b>{construcao}<br>"
                f"<b>Linha: </b>{linha}<br>"
                f"<b>Abertura: </b>{abertura}",
                max_width=300
            )
        ).add_to(mapa)

    def iterate_geojson(geom, construcao, linha, abertura, system, cores_linhas, mapa, grupos):
        if geom.geom_type == 'LineString':
            adicionar_linha_no_mapa(geom, construcao, linha, abertura, system, cores_linhas, mapa)
        elif geom.geom_type == 'GeometryCollection':
            for geometry in geom.geoms:
                iterate_geojson(geometry, construcao, linha, abertura, system, cores_linhas, mapa, grupos)

    def adicionar_secoes_no_mapa(gdf_sections, cores_linhas, mapa_trilhos_group):
        for idx, row in gdf_sections.iterrows():
            lines = row.get('lines', '')
            construcao = row.get('buildstart', '')
            abertura = row.get('opening', '')

            lines_info = json.loads(lines) if lines else []
            if lines_info:
                linha_info = lines_info[0]['line']
                system = lines_info[0].get('system_name', '')
                geometry = row['geometry']
                adicionar_linha_no_mapa(geometry, construcao, linha_info, abertura, system, cores_linhas, mapa_trilhos_group)

    def adicionar_estacoes_no_mapa(gdf_stations, caminho_icones, mapa_trilhos_group):
        for idx, row in gdf_stations.iterrows():
            lines_info = json.loads(row.get('lines', '')) if 'lines' in row else []

            if lines_info:
                line_info = lines_info[0]['line']
                caminho_icone = caminho_icones.get(line_info, 'Mapa_dos_Trilhos\\Icons\\default.png')
            else:
                line_info = ''
                caminho_icone = 'Mapa_dos_Trilhos\\Icons\\default.png'

            abertura = row.get('opening', '')

            folium.Marker(
                location=(row['geometry'].y, row['geometry'].x),
                popup=folium.Popup(
                    f"<b>Estação: </b>{row['name']}<br><b>Construída em: </b>{row.get('buildstart', '')}<br><b>Linha: </b>{line_info}<br><b>Abertura: </b>{abertura}",
                    max_width=300
                ),
                icon=folium.CustomIcon(icon_image=caminho_icone, icon_size=(25, 25))
            ).add_to(mapa_trilhos_group)

    def adicionar_shapes_sptrans(mapa, grupo):
        shapes = {}
        caminho_arquivo_shapes = "Mapa_dos_Trilhos\\Gtfs_SPTRANS\\shapes.txt"

        with open(caminho_arquivo_shapes, 'r', encoding='utf-8') as arquivo_shapes:
            linhas = arquivo_shapes.readlines()
            for linha in linhas[1:]:
                dados = linha.strip().split(',')
                if len(dados) >= 4:
                    shape_id = dados[0]
                    lat = float(dados[1].strip('"'))
                    lon = float(dados[2].strip('"'))

                    if shape_id not in shapes:
                        shapes[shape_id] = []

                    shapes[shape_id].append((lat, lon))

        for shape_id, coordenadas in shapes.items():
            folium.PolyLine(coordenadas, color='red').add_to(grupo)

    def adicionar_shapes_emtu(mapa, grupo_emtu):
        shapes = {}
        caminho_arquivo_shapes = "Mapa_dos_Trilhos\\Gtfs_EMTU\\shapes.txt"

        with open(caminho_arquivo_shapes, 'r', encoding='utf-8') as arquivo_shapes:
            linhas = arquivo_shapes.readlines()
            for linha in linhas[1:]:
                dados = linha.strip().split(',')
                if len(dados) >= 4:
                    shape_id = dados[0]
                    lat = float(dados[1].strip('"'))
                    lon = float(dados[2].strip('"'))

                    if shape_id not in shapes:
                        shapes[shape_id] = []

                    shapes[shape_id].append((lat, lon))

        for shape_id, coordenadas in shapes.items():
            folium.PolyLine(coordenadas, color='blue').add_to(grupo_emtu)

    def adicionar_pontos_emtu(mapa, paradas_emtu_group):
        caminho_arquivo_stops = "Mapa_dos_Trilhos\\Gtfs_EMTU\\stops.txt"
        dados_paradas = []

        with open(caminho_arquivo_stops, 'r', encoding='utf-8') as arquivo_stops:
            leitor_csv = csv.reader(arquivo_stops)
            cabecalho = next(leitor_csv)

            for linha in leitor_csv:
                dados_paradas.append(linha)

            for dados in dados_paradas:
                stop_id, stop_name, stop_lat, stop_lon = dados
                stop_lat = float(stop_lat)
                stop_lon = float(stop_lon)

                # Define o caminho do ícone personalizado
                caminho_icone_personalizado = 'Mapa_dos_Trilhos\\Icons\\icone-terminais-pontos_emtu.png'

                # Cria um ícone personalizado
                icone_personalizado = folium.CustomIcon(
                    icon_image=caminho_icone_personalizado,  # Substitua pelo caminho do seu ícone
                    icon_size=(25, 25)  # Ajuste o tamanho do ícone conforme necessário
                )

                # Adiciona o marcador com o ícone personalizado
                folium.Marker(
                    location=[stop_lat, stop_lon],
                    popup=folium.Popup(f"<b>ID: </b>{stop_id}<br><b>Localização: </b>{stop_name}", max_width=300),
                    icon=icone_personalizado
                ).add_to(paradas_emtu_group)

    def adicionar_pontos_sptrans(mapa, paradas_sptrans_group):
        caminho_arquivo_stops = "Mapa_dos_Trilhos\\Gtfs_SPTRANS\\stops.txt"
        dados_paradas = []

        with open(caminho_arquivo_stops, 'r', encoding='utf-8') as arquivo_stops:
            leitor_csv = csv.reader(arquivo_stops)
            cabecalho = next(leitor_csv)

            for linha in leitor_csv:
                dados_paradas.append(linha)

            for dados in dados_paradas:
                stop_id, stop_name, stop_desc, stop_lat, stop_lon = dados
                stop_lat = float(stop_lat)
                stop_lon = float(stop_lon)

                # Define o caminho do ícone personalizado
                caminho_icone_personalizado = 'Mapa_dos_Trilhos\\Icons\\icone-terminais-pontos_sptrans.png'

                # Cria um ícone personalizado
                icone_personalizado = folium.CustomIcon(
                    icon_image=caminho_icone_personalizado,  # Substitua pelo caminho do seu ícone
                    icon_size=(25, 25)  # Ajuste o tamanho do ícone conforme necessário
                )

                # Adiciona o marcador com o ícone personalizado
                folium.Marker(
                    location=[stop_lat, stop_lon],
                    popup=folium.Popup(f"<b>ID: </b>{stop_id}<br><b>Localização: </b>{stop_name}<br><b>Descrição/Referência: </b>{stop_desc}", max_width=300),
                    icon=icone_personalizado
                ).add_to(paradas_sptrans_group)

    def adicionar_bicicletarios_no_mapa(mapa, bicicletarios_group):
        bicicletarios_geojson = 'Mapa_dos_Trilhos\\Data\\LL_WGS84_KMZ_bicicletarioparaciclo.geojson'
        with open(bicicletarios_geojson, 'r', encoding='utf-8') as f:
            bicicletarios_data = json.load(f)
            for feature in bicicletarios_data['features']:
                bcp_local = feature['properties']['bcp_local']
                bcp_orgao = feature['properties']['bcp_orgao']
                bcp_vaga = feature['properties']['bcp_vaga']
                coordinates = feature['geometry']['coordinates'][::-1]

                folium.Marker(
                    location=coordinates,
                    popup=folium.Popup(
                        f"<b>Órgão:</b> {bcp_orgao}<br><b>Local:</b> {bcp_local}<br><b>Vagas:</b> {bcp_vaga}<br>",
                        max_width=300
                    ),
                    icon=folium.CustomIcon(icon_image='Mapa_dos_Trilhos\\Icons\\Bicicleta.png', icon_size=(30, 30))
                ).add_to(bicicletarios_group)

    def adicionar_ciclovias_no_mapa(mapa, ciclovias_group):
        ciclovias_geojson = 'Mapa_dos_Trilhos\\Data\\LL_WGS84_KMZ_redecicloviaria.json'

        with open(ciclovias_geojson, 'r', encoding='utf-8') as f:
            ciclovias_data = json.load(f)
            for feature in ciclovias_data['features']:
                coordinates = feature['geometry']['coordinates']
                coordinates = [(coord[1], coord[0]) for coord in coordinates]

                inauguracao = datetime.strptime(feature['properties']['rc_inaugur'], '%Y%m%d').strftime('%d/%m/%Y')
                extensao_total_km = float(feature['properties']['rc_ext_t']) / 1000
                extensao_calculada_km = float(feature['properties']['rc_ext_c']) / 1000

                folium.PolyLine(
                    locations=coordinates,
                    color='green',
                    weight=3,
                    popup=folium.Popup(
                        f"<b>Nome:</b> {feature['properties']['rc_nome']}<br>"
                        f"<b>Inauguração:</b> {inauguracao}<br>"
                        f"<b>Extensão Total:</b> {extensao_total_km:.2f} km<br>"
                        f"<b>Extensão Calculada:</b> {extensao_calculada_km:.2f} km<br>",
                        max_width=300
                    )
                ).add_to(ciclovias_group)

    def adicionar_qualidade_ar(mapa, ar_group):
        # Mapeamento de ícones
        icone_mapping = {
            "N1": "Mapa_dos_Trilhos\\Icons\\N1 - Boa.png",
            "N2": "Mapa_dos_Trilhos\\Icons\\N2 - Moderada.png",
            "N3": "Mapa_dos_Trilhos\\Icons\\N3 - Ruim.png",
            "N4": "Mapa_dos_Trilhos\\Icons\\N4 - Muito Ruim.png",
            "N5": "Mapa_dos_Trilhos\\Icons\\N5 - Péssima.png",
        }

        # Mapeamento de classificações
        classificacao_mapping = {
            "N1": "Boa",
            "N2": "Moderada",
            "N3": "Ruim",
            "N4": "Muito Ruim",
            "N5": "Péssima",
        }

        # Carrega o arquivo JSON
        with open('Mapa_dos_Trilhos\\Data\\dados_estacoes_medicoes.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Cria um mapa
        m = folium.Map(location=[-23.5505205, -46.6333083], zoom_start=10)

        # Itera sobre os dados
        for local, info in data['base_medicoes'].items():
            lat, lon = info['latitude'], info['longitude']
            estacao = local
            endereco = info['endereco']

            # Obtém a qualidade do ar para a estação atual
            latitude, longitude = info['latitude'], info['longitude']

            # Utiliza o certifi para apontar para o caminho do certificado
            response = requests.get(f"https://api.waqi.info/feed/geo:{latitude};{longitude}/?token={API_TOKEN_QUALITY_AR}", 
                                    verify=certifi.where())
            air_quality_data = response.json()

            # Função para obter a classificação com base no índice
            def obter_classificacao(indice):
                if indice <= 40:
                    return "N1"
                elif 41 <= indice <= 80:
                    return "N2"
                elif 81 <= indice <= 120:
                    return "N3"
                elif 121 <= indice <= 200:
                    return "N4"
                else:
                    return "N5"

            # Obtém o índice de qualidade do ar
            indice = air_quality_data['data']['aqi']
        
            # Obtém a classificação correspondente
            classificacao = obter_classificacao(indice)

            # Obtém o ícone correspondente com base na classificação
            icone = icone_mapping[classificacao]

            # Adiciona marcador com o índice e classificação como popup
            folium.Marker([lat, lon], 
                icon=folium.CustomIcon(icon_image=icone, icon_size=(30,30)),
                popup=folium.Popup(
                    f"<b>Estação: </b>{estacao}<br>"
                    f"<b>Endereço: </b>{endereco}<br>"
                    f"<b>Índice: </b>{indice}<br>"
                    f"<b>Qualidade do Ar: </b>{classificacao_mapping[classificacao]}<br>",
                    max_width=300
                )
            ).add_to(ar_group)

    def od1987(mapa, od1987_group):
        # Carrega o arquivo JSON
        with open('Mapa_dos_Trilhos\\Data\\ZonasOD87_region.json', 'r', encoding='utf-8') as f:
            seus_dados = json.load(f)

        # Define o transformer para converter de UTM para WGS84
        transformer = Transformer.from_crs("epsg:31983", "epsg:4326")

        # Adiciona as features do JSON ao mapa
        for feature in seus_dados['features']:
            if feature['geometry']['type'] == 'Polygon':
                coordinates = feature['geometry']['coordinates'][0]

                # Transforma as coordenadas para o sistema WGS84
                coordinates_wgs84 = [transformer.transform(coord[0], coord[1]) for coord in coordinates]

                # Calcula o centro do polígono para definir o local do pop-up
                lat = sum(coord[1] for coord in coordinates_wgs84) / len(coordinates_wgs84)
                lon = sum(coord[0] for coord in coordinates_wgs84) / len(coordinates_wgs84)

                # Pega as propriedades do polígono
                properties = feature['properties']

                # Adiciona a linha ao mapa como um objeto PolyLine
                folium.PolyLine(
                    locations=coordinates_wgs84,
                    color='green',
                    fill=True,
                    fill_color='green',            
                    weight=1,
                    popup=folium.Popup(f"<b>Id:</b> {properties['ZONA']}<br>"
                        f"<b>Nome</b> {properties['NOME']}<br>"    
                        f"<b>Área</b> {properties['AREA']} km²<br>"           
                        f"<b>Ano:</b> {'1987'}<br>",
                    max_width=300),
                ).add_to(od1987_group)

    def od1997(mapa, od1997_group):
        # Carrega o arquivo JSON
        with open('Mapa_dos_Trilhos\\Data\\zonas97_region.json', 'r', encoding='utf-8') as f:
            seus_dados = json.load(f)

        # Define o transformer para converter de UTM para WGS84
        transformer = Transformer.from_crs("epsg:31983", "epsg:4326")

        # Adiciona as features do JSON ao mapa
        for feature in seus_dados['features']:
            if feature['geometry']['type'] == 'Polygon':
                coordinates = feature['geometry']['coordinates'][0]

                # Transforma as coordenadas para o sistema WGS84
                coordinates_wgs84 = [transformer.transform(coord[0], coord[1]) for coord in coordinates]

                # Calcula o centro do polígono para definir o local do pop-up
                lat = sum(coord[1] for coord in coordinates_wgs84) / len(coordinates_wgs84)
                lon = sum(coord[0] for coord in coordinates_wgs84) / len(coordinates_wgs84)

                # Pega as propriedades do polígono
                properties = feature['properties']

                # Calcula a área em quilômetros quadrados
                area_km2 = float(properties['TOTAL_HA']) / 1

                popup_info = f"<b>Id:</b> {properties['ZONASEQ']}<br>" \
                            f"<b>Nome:</b> {properties['NOME_ZONA']}<br>" \
                            f"<b>Área:</b> {area_km2:.2f} km²<br>" \
                            f"<b>Ano:</b> {'1997'}<br>" \
                            f"<b>Nº do Distrito:</b> {properties['DISTRITOS']}<br>" \
                            f"<b>Nº do Munícipio:</b> {properties['MUNICípIO']}<br>" \
                            f"<b>Nº de Domícílios:</b> {properties['DOMICILIOS']:,}<br>" \
                            f"<b>Nº de Famílias:</b> {properties['FAMILIAS']:,}<br>" \
                            f"<b>População:</b> {properties['POPULAçãO']:,}<br>" \
                            f"<b>Matrícula Escolares:</b> {properties['MATRICULAS']:,}<br>" \
                            f"<b>Total Empregos:</b> {properties['EMPREGOS']:,}<br>" \
                            f"<b>Viagens Diárias por ÔNIBUS:</b> {properties['ONIBUS']:,}<br>" \
                            f"<b>Viagens Diárias por FRETADO:</b> {properties['FRETADO']:,}<br>" \
                            f"<b>Viagens Diárias por ESCOLAR:</b> {properties['ESCOLAR']:,}<br>" \
                            f"<b>Viagens Diárias por DIRIGINDO AUTOMÓVEL:</b> {properties['DIRIG_AUTO']:,}<br>" \
                            f"<b>Viagens Diárias por PASSAGEIRO AUTOMÓVEL:</b> {properties['PASS_AUTO']:,}<br>" \
                            f"<b>Viagens Diárias por TÁXI:</b> {properties['TAXI']:,}<br>" \
                            f"<b>Viagens Diárias por LOTAÇÃO:</b> {properties['LOTAçãO']:,}<br>" \
                            f"<b>Viagens Diárias por METRÔ:</b> {properties['METRO']:,}<br>" \
                            f"<b>Viagens Diárias por TREM:</b> {properties['TREM']:,}<br>" \
                            f"<b>Viagens Diárias por MOTO:</b> {properties['MOTO']:,}<br>" \
                            f"<b>Viagens Diárias por BICICLETA:</b> {properties['BICICLETA']:,}<br>" \
                            f"<b>Viagens Diárias A PÉ:</b> {properties['A_PE']:,}<br>" \
                            f"<b>Viagens para COMPRAS:</b> {properties['COMPRAS']:,}<br>" \
                            f"<b>Viagens para SAÚDE:</b> {properties['SAúdE']:,}<br>" \
                            f"<b>Viagens para LAZER:</b> {properties['LAZER']:,}<br>" \
                            f"<b>Viagens para RESIDÊNCIA:</b> {properties['RESIDênCIA']:,}<br>" \
                            f"<b>Viagens para OUTROS:</b> {properties['OUTROS0']:,}<br>" \
                            f"<b>Renda Familiar:</b> R$ {properties['RENDA_FAM']:.2f}<br>" \
                            f"<b>Renda PerCapita:</b> R$ {properties['PER_CAPITA']:.2f}<br>" \
                            f"<b>Viagens Diárias Totais:</b> {properties['PRODUZIDAS']:,}<br>" 

                folium.PolyLine(
                    locations=coordinates_wgs84,
                    color='green',
                    fill=True,
                    fill_color='green',
                    weight=1,
                    popup=folium.Popup(popup_info, max_width=300),
                ).add_to(od1997_group)

    def od2007(mapa, od2007_group):
        # Carrega o arquivo JSON
        with open('Mapa_dos_Trilhos\\Data\\SIRGAS_SHP_origemdestino_2007.json', 'r', encoding='utf-8') as f:
            seus_dados = json.load(f)

        # Define o transformer para converter de UTM para WGS84
        transformer = Transformer.from_crs("epsg:31983", "epsg:4326")

        # Adiciona as features do JSON ao mapa
        for feature in seus_dados['features']:
            if feature['geometry']['type'] == 'Polygon':
                coordinates = feature['geometry']['coordinates'][0]

                # Transforma as coordenadas para o sistema WGS84
                coordinates_wgs84 = [transformer.transform(coord[0], coord[1]) for coord in coordinates]

                # Calcula o centro do polígono para definir o local do pop-up
                lat = sum(coord[1] for coord in coordinates_wgs84) / len(coordinates_wgs84)
                lon = sum(coord[0] for coord in coordinates_wgs84) / len(coordinates_wgs84)

                # Pega as propriedades do polígono
                properties = feature['properties']

                # Calcula a área em quilômetros quadrados
                area_km2 = float(properties['od_area']) / 1

                # Adiciona a linha ao mapa como um objeto PolyLine
                folium.PolyLine(
                    locations=coordinates_wgs84,
                    color='green',
                    fill=True,
                    fill_color='green',            
                    weight=1,
                    popup=folium.Popup(f"<b>Id:</b> {properties['od_id']}<br>"
                        f"<b>Nome</b> {properties['od_nome']}<br>"           
                        f"<b>Área:</b> {area_km2:.2f} km²<br>" 
                        f"<b>Ano</b> {properties['od_ano']}<br>"
                        f"<b>Munícipio</b> {properties['od_municip']}<br>",
                    max_width=300),
                ).add_to(od2007_group)

    def od2017(mapa, od2017_group):
        # Carrega o arquivo JSON
        with open('Mapa_dos_Trilhos\\Data\\SIRGAS_SHP_origemdestino_2017.json', 'r', encoding='utf-8') as f:
            seus_dados = json.load(f)

        # Define o transformer para converter de UTM para WGS84
        transformer = Transformer.from_crs("epsg:31983", "epsg:4326")

        # Adiciona as features do JSON ao mapa
        for feature in seus_dados['features']:
            if feature['geometry']['type'] == 'Polygon':
                coordinates = feature['geometry']['coordinates'][0]

                # Transforma as coordenadas para o sistema WGS84
                coordinates_wgs84 = [transformer.transform(coord[0], coord[1]) for coord in coordinates]

                # Calcula o centro do polígono para definir o local do pop-up
                lat = sum(coord[1] for coord in coordinates_wgs84) / len(coordinates_wgs84)
                lon = sum(coord[0] for coord in coordinates_wgs84) / len(coordinates_wgs84)

                # Pega as propriedades do polígono
                properties = feature['properties']

                # Calcula a área em quilômetros quadrados
                area_km2 = float(properties['od_area']) / 1

                # Adiciona a linha ao mapa como um objeto PolyLine
                folium.PolyLine(
                    locations=coordinates_wgs84,
                    color='green',
                    fill=True,
                    fill_color='green',            
                    weight=1,
                    popup=folium.Popup(f"<b>Id:</b> {properties['od_id']}<br>"
                        f"<b>Nome</b> {properties['od_nome']}<br>"           
                        f"<b>Área:</b> {area_km2:.2f} km²<br>" 
                        f"<b>Ano</b> {properties['od_ano']}<br>"
                        f"<b>Munícipio</b> {properties['od_municip']}<br>",
                    max_width=300),
                ).add_to(od2017_group)
                
    def salvar_mapa_como_html(mapa, nome_arquivo):
        mapa.save(nome_arquivo)

    def abrir_mapa_no_navegador(nome_arquivo):
        webbrowser.open(nome_arquivo)

    # Cria um mapa
    m = criar_mapa(latitude, longitude, zoom=13)

    # Cria grupos para as camadas
    paradas_sptrans_group = folium.FeatureGroup(name='Paradas de Ônibus - SPTrans', show=False)
    paradas_emtu_group = folium.FeatureGroup(name='Paradas de Ônibus - EMTU', show=False)
    area_atendida_sptrans = folium.FeatureGroup(name='Área Atendida - SPTrans', show=False)
    area_atendida_emtu = folium.FeatureGroup(name='Área Atendida - EMTU', show=False)
    mapa_trilhos_group = folium.FeatureGroup(name='Mapa_dos_Trilhos e Corredor Exclusivo SPTRANS/EMTU', show=False)
    bicicletarios_group = folium.FeatureGroup(name='Bicicletários', show=False)
    ciclovias_group = folium.FeatureGroup(name='Ciclovias', show=False)
    ar_group = folium.FeatureGroup(name='Qualidade do Ar', show=False)
    od1987_group = folium.FeatureGroup(name='Origem e Destino - 1987', show=False)
    od1997_group = folium.FeatureGroup(name='Origem e Destino - 1997', show=False)
    od2007_group = folium.FeatureGroup(name='Origem e Destino - 2007', show=False)
    od2017_group = folium.FeatureGroup(name='Origem e Destino - 2017', show=False)

    # Cria o grupo de marcadores
    paradas_sptrans_group = MarkerCluster(name='Paradas de Ônibus - SPTrans', show=False).add_to(m)
    paradas_emtu_group = MarkerCluster(name='Paradas de Ônibus - EMTU', show=False).add_to(m)

    # Carrega os dados necessários
    cores_linhas = carregar_dados_arquivo('Mapa_dos_Trilhos\\Data\\sao-paulo_lines_systems_and_modes.json')
    caminho_icones = carregar_dados_arquivo('Mapa_dos_Trilhos\\Data\\caminho_icones.json')

    # Carrega o arquivo GeoJSON com as seções
    geojson_file_sections = 'Mapa_dos_Trilhos\\Data\\sao-paulo_sections.geojson'
    gdf_sections = gpd.read_file(geojson_file_sections)

    # Carrega o arquivo GeoJSON com as estações
    geojson_file_stations = 'Mapa_dos_Trilhos\\Data\\sao-paulo_stations.geojson'
    gdf_stations = gpd.read_file(geojson_file_stations)

    # Adiciona as seções ao mapa
    adicionar_secoes_no_mapa(gdf_sections, cores_linhas, mapa_trilhos_group)

    # Adiciona as estações ao mapa
    adicionar_estacoes_no_mapa(gdf_stations, caminho_icones, mapa_trilhos_group)

    # Adiciona shapes ao mapa
    adicionar_shapes_sptrans(m, area_atendida_sptrans)
    adicionar_shapes_emtu(m, area_atendida_emtu)
    
    # Adiciona paradas ao mapa
    adicionar_pontos_sptrans(m, paradas_sptrans_group)
    adicionar_pontos_emtu(m, paradas_emtu_group)

    # Adiciona bicicletários ao mapa
    adicionar_bicicletarios_no_mapa(m, bicicletarios_group)

    # Adiciona ciclovias ao mapa
    adicionar_ciclovias_no_mapa(m, ciclovias_group)

    adicionar_qualidade_ar(m, ar_group)

    od1987(m, od1987_group)
    od1997(m, od1997_group)
    od2007(m, od2007_group)
    od2017(m, od2017_group)

    # Adiciona os grupos de camadas ao mapa
    paradas_sptrans_group.add_to(m)
    paradas_emtu_group.add_to(m)
    area_atendida_sptrans.add_to(m)
    area_atendida_emtu.add_to(m)
    mapa_trilhos_group.add_to(m)
    bicicletarios_group.add_to(m)
    ciclovias_group.add_to(m)
    ar_group.add_to(m)
    od1987_group.add_to(m)
    od1997_group.add_to(m)
    od2007_group.add_to(m)
    od2017_group.add_to(m)

    # Adiciona controle de camadas ao mapa
    folium.LayerControl().add_to(m)

    Draw(export=True).add_to(m)

    folium.plugins.Fullscreen(
        position="topright",
        title="Exibir em Tela Cheia",
        title_cancel="Fechar Tela Cheia",
        force_separate_button=True,
    ).add_to(m)

    folium.plugins.Geocoder().add_to(m)

    folium.plugins.LocateControl(auto_start=False).add_to(m)

    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' &deg; ';};"

    MousePosition(
        position="topright",
        separator=" | ",
        empty_string="NaN",
        lng_first=True,
        num_digits=20,
        prefix="Coordenadas:",
        lat_formatter=formatter,
        lng_formatter=formatter,
    ).add_to(m)

    # Define o caminho do arquivo HTML
    map_file = "Mapa_dos_Trilhos\\mapa_global.html"

    # Verifica se o arquivo já existe
    if os.path.exists(map_file):
        # Obtém as informações de tempo do arquivo
        tempo_modificacao = datetime.fromtimestamp(os.path.getmtime(map_file))
        tempo_atual = datetime.now()

        # Calcula a diferença de tempo
        diferenca_tempo = tempo_atual - tempo_modificacao

        # Se o arquivo foi criado a mais de 1 hora, gera um novo mapa
        if diferenca_tempo > timedelta(hours=1):
            # Salva o mapa como HTML
            salvar_mapa_como_html(m, map_file)
    else:
        # Salva o mapa como HTML
        salvar_mapa_como_html(m, map_file)

    # Abre o mapa no navegador padrão
    abrir_mapa_no_navegador(map_file)