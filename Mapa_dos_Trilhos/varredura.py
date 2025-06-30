# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte pÃºblico Metropolitano do Estado de SÃ£o Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "28/06/2025 16:56"

DESCRITIVO:
MÃ³dulo de funcionalidades especÃ­ficas
ARQUITETURA:
    Mapa_dos_Trilhos/varredura.py
"""
import os
from pathlib import Path
import logging

def verificacao():
    resultados = {
        'pastas_nao_encontradas': [],
        'arquivos_encontrados': [],
        'arquivos_nao_encontrados': []
    }

    def verificar_arquivos(pastas, lista_arquivos):
        for pasta in pastas:
            pasta_path = Path(pasta.replace('\\', '/'))
            
            if not pasta_path.exists():
                resultados['pastas_nao_encontradas'].append(str(pasta_path))
                continue
                
            for arquivo in lista_arquivos:
                arquivo_nome = os.path.basename(arquivo)
                caminho_arquivo = pasta_path / arquivo_nome
                
                if caminho_arquivo.exists():
                    resultados['arquivos_encontrados'].append({
                        'arquivo': arquivo_nome,
                        'pasta': str(pasta_path)
                    })
                else:
                    resultados['arquivos_nao_encontrados'].append({
                        'arquivo': arquivo_nome,
                        'pasta': str(pasta_path)
                    })

    pastas_verificadas = [
        "Mapa_dos_Trilhos",
        "Mapa_dos_Trilhos/Sobre",
        "Mapa_dos_Trilhos/Data",
        "Mapa_dos_Trilhos/Gtfs_EMTU",  
        "Mapa_dos_Trilhos/Gtfs_SPTRANS", 
        "Mapa_dos_Trilhos/Linhas"
    ]

    lista_arquivos_verificados = [
        "caminho_icones.json", 
        "dados_estacoes_medicoes.json", 
        "Desktop_Guide_abr_2022_v2.pdf", 
        "Guia_do_passageiro_abr_2022.pdf",
        "LL_WGS84_KMZ_bicicletarioparaciclo.geojson",
        "LL_WGS84_KMZ_redecicloviaria.json",             
        "mapa-da-rede-metro.pdf",
        "Regulamento de Viagem Expresso Turístico.pdf",
        "Regulamento-Viagem.pdf",
        "sao-paulo_lines_systems_and_modes.json",
        "sao-paulo_sections.geojson", 
        "sao-paulo_stations.geojson",
        "SIRGAS_SHP_origemdestino_2007.json",
        "SIRGAS_SHP_origemdestino_2017.json",
        "zonas97_region.json",             
        "ZonasOD87_region.json",
        "agency.txt",
        "calendar.txt",
        "dataRef-10012024.txt",
        "fare_attributes.txt",
        "fare_rules.txt",
        "feed_info.txt",
        "routes.txt",
        "shapes.txt",
        "stops.txt",
        "trips.txt",
        "CPTM_SP_L7.py",
        "CPTM_SP_L8.py",
        "CPTM_SP_L9.py",
        "CPTM_SP_L10.py",
        "CPTM_SP_L11.py",  
        "CPTM_SP_L12.py",
        "CPTM_SP_L13.py",
        "Guararema.py",
        "Metrô_SP_L1.py",
        "Metrô_SP_L2.py",    
        "Metrô_SP_L3.py",
        "Metrô_SP_L4.py",
        "Metrô_SP_L5.py",
        "Metrô_SP_L15.py",
        "Pirapora.py",    
        "cet.py",
        "gtfs_emtu.py",
        "gtfs_sptrans.py",
        "guias.py",
        "log.txt",
        "mapa.py",
        "noticia.py",
        "temperatura.py",
        "web.py",
        "index.html",
        "linha_01.html",
        "linha_02.html",
        "linha_03.html",
        "linha_04.html",
        "linha_05.html",
        "linha_07.html",
        "linha_08.html",
        "linha_09.html",
        "linha_10.html",
        "linha_11.html",
        "linha_12.html",
        "linha_13.html",
        "linha_14.html",
        "linha_15.html",
        "script.js",
        "server.js",
        "styles.css"
    ]

    verificar_arquivos(pastas_verificadas, lista_arquivos_verificados)
    return resultados

def fazer_varredura():
    resultados = verificacao()
    
    # Log dos resultados
    logging.info("Resultado da varredura de arquivos:")
    logging.info(f"Pastas não encontradas: {len(resultados['pastas_nao_encontradas'])}")
    logging.info(f"Arquivos encontrados: {len(resultados['arquivos_encontrados'])}")
    logging.info(f"Arquivos não encontrados: {len(resultados['arquivos_nao_encontrados'])}")
    
    return resultados