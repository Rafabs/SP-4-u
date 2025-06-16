import os
from pathlib import Path

def verificacao():
    def verificar_arquivos(pastas, lista_arquivos):
        for pasta in pastas:
            # Normaliza o caminho da pasta
            pasta_path = Path(pasta.replace('\\', '/'))
            print(f"\nVerificando arquivos em {pasta_path}:")
            
            if not pasta_path.exists():
                print(f"- PASTA NÃO ENCONTRADA: {pasta_path}")
                continue
                
            for arquivo in lista_arquivos:
                # Remove duplicação de caminho se existir
                arquivo_nome = os.path.basename(arquivo)
                caminho_arquivo = pasta_path / arquivo_nome
                
                if caminho_arquivo.exists():
                    print(f"- {arquivo_nome} encontrado")
                else:
                    print(f"- {arquivo_nome} não encontrado")

    # Lista de pastas a serem verificadas (usando Path)
    pastas_verificadas = [
        "Mapa_dos_Trilhos",
        "Mapa_dos_Trilhos/Sobre",
        "Mapa_dos_Trilhos/Data",
        "Mapa_dos_Trilhos/Gtfs_EMTU",  
        "Mapa_dos_Trilhos/Gtfs_SPTRANS", 
        "Mapa_dos_Trilhos/Linhas"
    ]

    # Lista de arquivos a serem verificados (apenas nomes, sem caminho)
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

    # Chama a função para verificar os arquivos
    verificar_arquivos(pastas_verificadas, lista_arquivos_verificados)

    # Retorna um dicionário com os resultados (opcional)
    return {"status": "Verificação concluída", "pastas": pastas_verificadas}