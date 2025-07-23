# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte pÃºblico Metropolitano do Estado de SÃ£o Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.2"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "16/07/2025 02:00"

DESCRITIVO:
MÃ³dulo de processamento de dados GTFS (General Transit Feed Specification):
- Implementa parser completo do formato GTFS
- Carrega e processa arquivos: routes.txt, trips.txt, stop_times.txt, stops.txt
- Calcula itinerÃ¡rios e conexÃµes entre linhas
- Interface grÃ¡fica com Tkinter para consulta
- VisualizaÃ§Ã£o de mapas com Folium
- IntegraÃ§Ã£o com API Olho Vivo (tempo real)
- ExportaÃ§Ã£o para CSV/Excel/JSON
- Algoritmo de roteamento (Dijkstra)
- Suporte a mÃºltiplos encodings (UTF-8, Latin-1)
ARQUITETURA:
    Mapa_dos_Trilhos/gtfs_sptrans.py
"""
import csv
import webbrowser
import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from tkinter.scrolledtext import ScrolledText
import folium
from folium.plugins import MarkerCluster
from PIL import Image, ImageTk
from colorama import Fore, Back, Style, init
from datetime import datetime, timedelta
import logging
from typing import List, Dict, Optional, Set, Tuple
import requests
import json
from threading import Thread
import os
from pathlib import Path
import sys

BASE_DIR = Path(__file__).parent.parent
GTFS_DIR = BASE_DIR / "Mapa_dos_Trilhos" / "Gtfs_SPTRANS"

if not GTFS_DIR.exists():
    raise FileNotFoundError(
        f"Diretório GTFS não encontrado em: {GTFS_DIR}\n"
        f"Por favor, verifique se a pasta 'Gtfs_SPTRANS' está em 'Mapa_dos_Trilhos'"
    )

# Get the absolute path to the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
    
from Mapa_dos_Trilhos.utils.logger_config import configurar_logger
configurar_logger()

# Obtém a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")

class DadosGTFS:
    """Classe para carregar e gerenciar dados GTFS"""
    
    def __init__(self):
        self.routes = self.carregar_routes()
        self.trips = self.carregar_trips()
        self.stop_times = self.carregar_stop_times()
        self.stops = self.carregar_stops()
        self.frequencies = self.carregar_frequencies()
        self.calendar = self.carregar_calendar()
        self.fare_attributes = self.carregar_fare_attributes()
        
        # Mapeamentos úteis
        self.stop_map = {stop['stop_id']: stop for stop in self.stops}
        self.trip_map = {trip['trip_id']: trip for trip in self.trips}
        self.frequencies_map = self.criar_frequencies_map()
    
    def carregar_arquivo(self, caminho: str) -> List[Dict]:
        """Carrega um arquivo CSV do GTFS com tratamento robusto de erros"""
        try:
            caminho = str(Path(caminho))  # Garante que é um caminho válido
            
            if not os.path.exists(caminho):
                raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
                
            with open(caminho, newline='', encoding='utf-8') as arquivo:
                leitor = csv.DictReader(arquivo)
                return list(leitor)
                
        except UnicodeDecodeError:
            # Tentar com outro encoding se UTF-8 falhar
            try:
                with open(caminho, newline='', encoding='latin-1') as arquivo:
                    leitor = csv.DictReader(arquivo)
                    return list(leitor)
            except Exception as e:
                logging.error(f"Erro ao carregar {caminho} com latin-1: {str(e)}")
                return []
                
        except Exception as e:
            logging.error(f"Erro ao carregar {caminho}: {str(e)}", exc_info=True)
            return []
    
    def carregar_routes(self) -> List[Dict]:
        return self.carregar_arquivo(str(GTFS_DIR /'routes.txt'))
    
    def carregar_trips(self) -> List[Dict]:
        return self.carregar_arquivo(str(GTFS_DIR /'trips.txt'))
    
    def carregar_stop_times(self) -> List[Dict]:
        return self.carregar_arquivo(str(GTFS_DIR / 'stop_times.txt'))
    
    def carregar_stops(self) -> List[Dict]:
        return self.carregar_arquivo(str(GTFS_DIR / 'stops.txt'))
    
    def carregar_frequencies(self) -> List[Dict]:
        return self.carregar_arquivo(str(GTFS_DIR / 'frequencies.txt'))
    
    def carregar_calendar(self) -> List[Dict]:
        return self.carregar_arquivo(str(GTFS_DIR / 'calendar.txt'))
    
    def carregar_fare_attributes(self) -> List[Dict]:
        return self.carregar_arquivo(str(GTFS_DIR / 'fare_attributes.txt'))
    
    def criar_frequencies_map(self) -> Dict:
        """Cria mapeamento de trip_id para frequências"""
        freq_map = {}
        for freq in self.frequencies:
            trip_id = freq.get('trip_id')
            if trip_id:
                freq_map.setdefault(trip_id, []).append(freq)
        return freq_map

def sptrans():
    """Função principal da aplicação"""
    print(f"{Style.BRIGHT}{Fore.WHITE}GTFS da SPTRANS iniciado às {Fore.GREEN}{hora_atual}{Style.RESET_ALL}")
    
    # Carregar dados GTFS
    dados = DadosGTFS()
    
    # Criar janela principal
    root = tk.Tk()
    root.title("Consulta de Rotas SPTrans")
    root.geometry("1200x800")
    
    # Configurar ícone
    try:
        icon_path = str(BASE_DIR / 'Mapa_dos_Trilhos' / 'Favicon' / 'onibus_sptrans.ico')
        image = Image.open(icon_path)
        photo = ImageTk.PhotoImage(image)
        root.iconphoto(False, photo)
    except Exception as e:
        logging.error(f"Erro ao carregar ícone: {str(e)}")
    
    # Variáveis globais
    rotas = []
    
    # Funções auxiliares
    def exibir_rotas() -> List[str]:
        """Exibe todas as rotas disponíveis"""
        nonlocal rotas
        try:
            rotas = [
                f"{route['route_id']} - {route['route_long_name']}\n"
                for route in dados.routes
            ]
            resultado_text.delete(1.0, tk.END)
            resultado_text.insert(tk.END, "".join(rotas))
            return rotas
        except Exception as e:
            resultado_text.insert(tk.END, f"Erro ao carregar rotas: {str(e)}")
            return []
    
    def filtrar_linhas():
        """Filtra as linhas com base no termo de pesquisa"""
        termo = campo_pesquisa.get().lower()
        linhas_filtradas = [linha for linha in rotas if termo in linha.lower()]
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, "".join(linhas_filtradas))
    
    def exibir_tarifas():
        """Exibe a tabela de tarifas"""
        try:
            tabela_tarifas.delete(*tabela_tarifas.get_children())
            for tarifa in dados.fare_attributes:
                nome = tarifa.get('fare_id', '')
                valor = f"R$ {float(tarifa.get('price', '0')):.2f}"
                tabela_tarifas.insert("", "end", values=(nome, valor))
        except Exception as e:
            tabela_tarifas.insert("", "end", values=(f"Erro: {str(e)}", ""))
    
    def exibir_frequencias():
        """Exibe a tabela de frequências"""
        try:
            frequencias_tree.delete(*frequencias_tree.get_children())
            for freq in dados.frequencies:
                trip_id = freq.get('trip_id', '')
                trip = dados.trip_map.get(trip_id, {})
                route_id = trip.get('route_id', '?')
                headsign = trip.get('trip_headsign', '')
                direction = trip.get('direction_id', '')
                descricao = f"{route_id} • {headsign} ({direction})"
                intervalo = f"{int(freq.get('headway_secs', '0')) // 60} min"
                frequencias_tree.insert("", "end", values=(
                    descricao,
                    freq.get('start_time', ''),
                    freq.get('end_time', ''),
                    intervalo
                ))
        except Exception as e:
            frequencias_tree.insert("", "end", values=(f"Erro: {str(e)}", "", "", ""))
    
    def gerar_horarios_interpolados(start_time: str, end_time: str, headway_secs: str) -> List[str]:
        """Gera horários baseados na frequência (headway)"""
        try:
            start = datetime.strptime(start_time, "%H:%M:%S")
            end = datetime.strptime(end_time, "%H:%M:%S")
            headway = timedelta(seconds=int(headway_secs))
            horarios = []
            
            atual = start
            while atual <= end:
                horarios.append(atual.strftime("%H:%M:%S"))
                atual += headway
            
            return horarios
        except Exception as e:
            logging.error(f"Erro ao gerar horários: {str(e)}")
            return []
    
    def mostrar_itinerario(route_id: str):
        """Exibe o itinerário completo para uma rota específica"""
        print(f"Exibindo itinerário da linha: {route_id}")
        
        try:
            # Filtrar trips para a rota selecionada
            trips_rota = [
                trip for trip in dados.trips
                if trip.get('route_id') == route_id
            ]
            
            if not trips_rota:
                messagebox.showwarning("Aviso", f"Nenhuma viagem encontrada para a linha {route_id}")
                return
            
            # Criar janela de seleção
            janela_selecao = tk.Toplevel(root)
            janela_selecao.title(f"Seleção de Horário - Linha {route_id}")
            
            # Variável para armazenar a seleção
            var_periodo = tk.StringVar(value="todos")
            
            # Frame para opções
            frame_opcoes = ttk.Frame(janela_selecao)
            frame_opcoes.pack(pady=10)
            
            ttk.Label(frame_opcoes, text="Selecione o período:").pack()
            
            opcoes = [
                ("Todos os horários", "todos"),
                ("Manhã (06:00-12:00)", "manha"),
                ("Tarde (12:00-18:00)", "tarde"),
                ("Noite (18:00-23:59)", "noite"),
                ("Madrugada (00:00-06:00)", "madrugada")
            ]
            
            for texto, valor in opcoes:
                ttk.Radiobutton(frame_opcoes, text=texto, variable=var_periodo, value=valor).pack(anchor='w')
            
            def exibir_horarios_selecionados():
                """Exibe os horários conforme a seleção do usuário"""
                periodo = var_periodo.get()
                filtrar_por_hora = periodo != "todos"
                
                janela = tk.Toplevel(janela_selecao)
                janela.title(f"Itinerário: {route_id}")
                janela.geometry("1200x800")
                
                # Paleta de cores pastel (16 cores distintas)
                cores_viagens = [
                    "#FFCDD2", "#F8BBD0", "#E1BEE7", "#D1C4E9", 
                    "#C5CAE9", "#BBDEFB", "#B3E5FC", "#B2EBF2",
                    "#B2DFDB", "#C8E6C9", "#DCEDC8", "#F0F4C3",
                    "#FFF9C4", "#FFECB3", "#FFE0B2", "#FFCCBC"
                ]
                
                notebook = ttk.Notebook(janela)
                notebook.pack(fill=tk.BOTH, expand=True)
                
                for direcao in ['0', '1']:
                    trips_direcao = [
                        t for t in trips_rota 
                        if t.get('direction_id') == direcao
                    ]
                    
                    if not trips_direcao:
                        continue
                    
                    # Frame externo com canvas e scrollbar
                    frame_sentido_externo = ttk.Frame(notebook)
                    
                    # Canvas + Scrollbar vertical
                    canvas = tk.Canvas(frame_sentido_externo)
                    scrollbar_vertical = ttk.Scrollbar(frame_sentido_externo, orient="vertical", command=canvas.yview)
                    canvas.configure(yscrollcommand=scrollbar_vertical.set)
                    
                    scrollbar_vertical.pack(side="right", fill="y")
                    canvas.pack(side="left", fill="both", expand=True)
                    
                    frame_sentido = ttk.Frame(canvas)
                    canvas.create_window((0, 0), window=frame_sentido, anchor="nw", tags="frame")
                    
                    def on_frame_configure(event):
                        canvas.configure(scrollregion=canvas.bbox("all"))
                    
                    def on_canvas_configure(event):
                        canvas.itemconfig("frame", width=event.width)
                    
                    canvas.bind("<Configure>", on_canvas_configure)
                    frame_sentido.bind("<Configure>", on_frame_configure)
                    
                    # Configurar scroll do mouse
                    def bind_scroll(event):
                        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
                    
                    def unbind_scroll(event):
                        canvas.unbind_all("<MouseWheel>")
                    
                    frame_sentido.bind("<Enter>", bind_scroll)
                    frame_sentido.bind("<Leave>", unbind_scroll)
                    
                    # Adicionar aba ao notebook
                    headsign = trips_direcao[0].get('trip_headsign', f"Direção {direcao}")
                    notebook.add(frame_sentido_externo, text=f"Direção: {headsign}")
                    
                    # Processar cada viagem
                    viagens_por_hora = {}
                    
                    for viagem_idx, trip in enumerate(trips_direcao):
                        trip_id = trip.get('trip_id', '')
                        cor = cores_viagens[viagem_idx % len(cores_viagens)]
                        
                        # Obter paradas desta viagem
                        modelo_paradas = [
                            st for st in dados.stop_times
                            if st.get('trip_id') == trip_id
                        ]
                        
                        if not modelo_paradas:
                            continue
                        
                        def adicionar_viagem(horario_base_str: str):
                            """Adiciona uma viagem ao agrupamento por horário"""
                            try:
                                horario_base = datetime.strptime(horario_base_str, "%H:%M:%S")
                                tempo_ref = datetime.strptime(modelo_paradas[0].get('arrival_time', '00:00:00'), "%H:%M:%S")
                                delta_ref = horario_base - tempo_ref
                                
                                paradas_info = {}
                                hora_chave = horario_base.strftime("%H:%M")
                                
                                for parada in modelo_paradas:
                                    seq = int(parada.get('stop_sequence', 0))
                                    nome = dados.stop_map.get(parada.get('stop_id', ''), {}).get('stop_name', 'Desconhecido')
                                    tempo_parada = datetime.strptime(parada.get('arrival_time', '00:00:00'), "%H:%M:%S")
                                    hora = (tempo_parada + delta_ref).strftime("%H:%M")
                                    
                                    # Filtrar por período
                                    if filtrar_por_hora:
                                        hora_num = int(hora.split(':')[0])
                                        if (periodo == "manha" and not 6 <= hora_num < 12) or \
                                           (periodo == "tarde" and not 12 <= hora_num < 18) or \
                                           (periodo == "noite" and not 18 <= hora_num <= 23) or \
                                           (periodo == "madrugada" and not (0 <= hora_num < 6)):
                                            continue
                                    
                                    paradas_info.setdefault(seq, {'nome': nome})[hora] = hora
                                
                                viagens_por_hora.setdefault(hora_chave, []).append({
                                    'paradas': paradas_info,
                                    'cor': cor,
                                    'trip_id': trip_id
                                })
                            
                            except Exception as e:
                                logging.error(f"Erro ao adicionar viagem: {str(e)}")
                        
                        # Adicionar horário real
                        if modelo_paradas[0].get('arrival_time'):
                            adicionar_viagem(modelo_paradas[0]['arrival_time'])
                        
                        # Adicionar horários de frequência
                        for freq in dados.frequencies_map.get(trip_id, []):
                            horarios = gerar_horarios_interpolados(
                                freq.get('start_time', '00:00:00'),
                                freq.get('end_time', '23:59:59'),
                                freq.get('headway_secs', '3600')
                            )
                            for h in horarios:
                                adicionar_viagem(h)
                    
                    # Exibir viagens agrupadas por horário
                    for hora_chave, viagens in sorted(viagens_por_hora.items()):
                        frame_hora = ttk.LabelFrame(
                            frame_sentido,
                            text=f"Saída às {hora_chave} • {len(viagens)} viagens"
                        )
                        frame_hora.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
                        
                        # Treeview para exibir as paradas
                        tree = ttk.Treeview(frame_hora, show="headings")
                        
                        # Determinar todas as colunas necessárias
                        horarios = set()
                        for viagem in viagens:
                            for seq, info in viagem['paradas'].items():
                                for h in info:
                                    if h != 'nome':
                                        horarios.add(h)
                        
                        colunas = ["seq", "parada"] + sorted(horarios)
                        tree["columns"] = colunas
                        
                        # Configurar cabeçalhos
                        tree.heading("seq", text="Ordem")
                        tree.column("seq", width=50, anchor="center")
                        
                        tree.heading("parada", text="Parada")
                        tree.column("parada", width=250, anchor="w")
                        
                        for hora in sorted(horarios):
                            tree.heading(hora, text=hora)
                            tree.column(hora, width=80, anchor="center")
                        
                        # Adicionar tags de cor para cada viagem
                        for viagem_idx, viagem in enumerate(viagens):
                            tree.tag_configure(f'viagem_{viagem_idx}', background=viagem['cor'])
                        
                        # Adicionar dados
                        for viagem_idx, viagem in enumerate(viagens):
                            for seq in sorted(viagem['paradas'].keys()):
                                valores = [seq, viagem['paradas'][seq]['nome']]
                                for hora in sorted(horarios):
                                    valores.append(viagem['paradas'][seq].get(hora, ""))
                                
                                tree.insert("", "end", values=valores, tags=(f'viagem_{viagem_idx}',))
                        
                        # Configurar scrollbars
                        vsb = ttk.Scrollbar(frame_hora, orient="vertical", command=tree.yview)
                        hsb = ttk.Scrollbar(frame_hora, orient="horizontal", command=tree.xview)
                        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
                        
                        tree.grid(row=0, column=0, sticky="nsew")
                        vsb.grid(row=0, column=1, sticky="ns")
                        hsb.grid(row=1, column=0, sticky="ew")
                        
                        frame_hora.grid_rowconfigure(0, weight=1)
                        frame_hora.grid_columnconfigure(0, weight=1)
                
                # Adicionar legenda de cores
                if viagens_por_hora:
                    legenda_frame = ttk.Frame(janela)
                    legenda_frame.pack(fill=tk.X, padx=10, pady=5)
                    
                    ttk.Label(legenda_frame, text="Legenda de Veículos:").pack(side=tk.LEFT)
                    
                    # Mostrar até 8 viagens na legenda
                    viagens_unicas = {
                        v['trip_id']: v['cor']
                        for grupo in viagens_por_hora.values()
                        for v in grupo
                    }
                    
                    for trip_id, cor in list(viagens_unicas.items())[:8]:
                        frame_cor = tk.Frame(legenda_frame, width=20, height=20, bg=cor)
                        frame_cor.pack(side=tk.LEFT, padx=5)
                        ttk.Label(legenda_frame, text=trip_id[-3:]).pack(side=tk.LEFT)
            
            # Botão para confirmar
            ttk.Button(
                janela_selecao,
                text="Exibir Horários",
                command=exibir_horarios_selecionados
            ).pack(pady=10)
        
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao exibir itinerário: {str(e)}")
            logging.exception("Erro em mostrar_itinerario")
    
    def ao_clicar_na_linha(event):
        """Handler para clique em uma linha na lista de rotas"""
        try:
            indice = resultado_text.index(f"@{event.x},{event.y}")
            linha = resultado_text.get(
                f"{indice} linestart",
                f"{indice} lineend"
            ).strip()
            
            if '-' not in linha:
                return
            
            # Extrair route_id corretamente (ex: "1012-10" de "1012-10 - Term. Jd. Britania...")
            partes = linha.split('-', 1)
            if len(partes) < 2:
                return
                
            route_id = f"{partes[0].strip()}-{partes[1].split()[0].strip()}"
            print(f"Route ID extraído: {route_id}")
            mostrar_itinerario(route_id)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível exibir o itinerário: {str(e)}")
            logging.error(f"Erro ao processar clique: {str(e)}")
    
    # Interface principal
    frame_principal = ttk.Frame(root)
    frame_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Frame de pesquisa
    frame_pesquisa = ttk.Frame(frame_principal)
    frame_pesquisa.pack(fill=tk.X, pady=5)
    
    ttk.Label(frame_pesquisa, text="Pesquisar linha:").pack(side=tk.LEFT)
    campo_pesquisa = ttk.Entry(frame_pesquisa)
    campo_pesquisa.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
    campo_pesquisa.bind('<KeyRelease>', lambda e: filtrar_linhas())
    
    # Frame de conteúdo
    frame_conteudo = ttk.Frame(frame_principal)
    frame_conteudo.pack(fill=tk.BOTH, expand=True)
    
    # Frame esquerdo (rotas)
    frame_esquerdo = ttk.Frame(frame_conteudo)
    frame_esquerdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Área de exibição de rotas
    resultado_text = ScrolledText(frame_esquerdo, width=40, height=20, wrap=tk.WORD)
    resultado_text.pack(fill=tk.BOTH, expand=True)
    resultado_text.bind("<Button-1>", ao_clicar_na_linha)
    
    # Frame para botões
    frame_botoes = ttk.Frame(frame_esquerdo)
    frame_botoes.pack(fill=tk.X, pady=5)
    
    # Botões de ação
    botao_shapes = ttk.Button(
        frame_botoes,
        text="Mapa de Ruas",
        command=lambda: carregar_mapa(dados)
    )
    botao_shapes.pack(side=tk.LEFT, padx=5)
    
    botao_stops = ttk.Button(
        frame_botoes,
        text="Mapa de Paradas",
        command=lambda: mostrar_pontos(dados)
    )
    botao_stops.pack(side=tk.LEFT, padx=5)
    
    # Frame direito (tabelas)
    frame_direito = ttk.Frame(frame_conteudo)
    frame_direito.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Notebook para abas de tarifas e frequências
    notebook_tabelas = ttk.Notebook(frame_direito)
    notebook_tabelas.pack(fill=tk.BOTH, expand=True)
    
    # Aba de tarifas
    frame_tarifas = ttk.Frame(notebook_tabelas)
    notebook_tabelas.add(frame_tarifas, text="Tarifas")
    
    tabela_tarifas = ttk.Treeview(frame_tarifas, columns=("Modalidade", "Tarifa"), show="headings")
    tabela_tarifas.heading("Modalidade", text="Modalidade")
    tabela_tarifas.heading("Tarifa", text="Tarifa")
    tabela_tarifas.column("Modalidade", width=150, anchor="w")
    tabela_tarifas.column("Tarifa", width=80, anchor="center")
    
    vsb_tarifas = ttk.Scrollbar(frame_tarifas, orient="vertical", command=tabela_tarifas.yview)
    hsb_tarifas = ttk.Scrollbar(frame_tarifas, orient="horizontal", command=tabela_tarifas.xview)
    tabela_tarifas.configure(yscrollcommand=vsb_tarifas.set, xscrollcommand=hsb_tarifas.set)
    
    tabela_tarifas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    vsb_tarifas.pack(side=tk.RIGHT, fill=tk.Y)
    hsb_tarifas.pack(side=tk.BOTTOM, fill=tk.X)
    
    # Aba de frequências
    frame_frequencias = ttk.Frame(notebook_tabelas)
    notebook_tabelas.add(frame_frequencias, text="Frequências")
    
    frequencias_tree = ttk.Treeview(
        frame_frequencias,
        columns=("Viagem", "Início", "Fim", "Intervalo"),
        show="headings"
    )
    frequencias_tree.heading("Viagem", text="Viagem")
    frequencias_tree.heading("Início", text="Início")
    frequencias_tree.heading("Fim", text="Fim")
    frequencias_tree.heading("Intervalo", text="Intervalo (min)")
    frequencias_tree.column("Viagem", width=200, anchor="w")
    frequencias_tree.column("Início", width=100, anchor="center")
    frequencias_tree.column("Fim", width=100, anchor="center")
    frequencias_tree.column("Intervalo", width=100, anchor="center")
    
    adicionar_aba_tempo_real(notebook_tabelas, dados)
    adicionar_aba_calculo_rotas(notebook_tabelas, dados)

    adicionar_menu_exportacao(root, dados)

    vsb_freq = ttk.Scrollbar(frame_frequencias, orient="vertical", command=frequencias_tree.yview)
    hsb_freq = ttk.Scrollbar(frame_frequencias, orient="horizontal", command=frequencias_tree.xview)
    frequencias_tree.configure(yscrollcommand=vsb_freq.set, xscrollcommand=hsb_freq.set)
    
    frequencias_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    vsb_freq.pack(side=tk.RIGHT, fill=tk.Y)
    hsb_freq.pack(side=tk.BOTTOM, fill=tk.X)
    
    # Carregar dados iniciais
    rotas = exibir_rotas()
    exibir_tarifas()
    exibir_frequencias()
    
    # Iniciar loop principal
    root.mainloop()

def carregar_mapa(dados: DadosGTFS):
    """Carrega o mapa com os shapes das rotas"""
    try:
        m = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)
        shapes = {}
        
        for shape in dados.carregar_arquivo('Mapa_dos_Trilhos\\Gtfs_SPTRANS\\shapes.txt'):
            shape_id = shape.get('shape_id')
            if shape_id not in shapes:
                shapes[shape_id] = []
            
            try:
                lat = float(shape.get('shape_pt_lat', 0))
                lon = float(shape.get('shape_pt_lon', 0))
                shapes[shape_id].append((lat, lon))
            except (ValueError, TypeError):
                continue
        
        for shape_id, coordenadas in shapes.items():
            folium.PolyLine(coordenadas, color='red').add_to(m)
        
        m.save("Mapa_dos_Trilhos\\mapa_shapes.html")
        webbrowser.open("Mapa_dos_Trilhos\\mapa_shapes.html")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao carregar mapa: {str(e)}")
        logging.error(f"Erro em carregar_mapa: {str(e)}")

def mostrar_pontos(dados: DadosGTFS):
    """Mostra mapa com pontos de parada"""
    try:
        m = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)
        marker_cluster = MarkerCluster().add_to(m)
        
        for stop in dados.stops:
            try:
                stop_id = stop.get('stop_id', '')
                stop_name = stop.get('stop_name', 'Desconhecido')
                stop_desc = stop.get('stop_desc', '')
                stop_lat = float(stop.get('stop_lat', 0))
                stop_lon = float(stop.get('stop_lon', 0))
                
                folium.Marker(
                    location=[stop_lat, stop_lon],
                    popup=folium.Popup(
                        f"<b>{stop_name}</b><br>ID: {stop_id}<br>Descrição: {stop_desc}",
                        max_width=300
                    )
                ).add_to(marker_cluster)
            except (ValueError, TypeError):
                continue
        
        m.save("Mapa_dos_Trilhos\\mapa_paradas_cluster.html")
        webbrowser.open("Mapa_dos_Trilhos\\mapa_paradas_cluster.html")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao carregar paradas: {str(e)}")
        logging.error(f"Erro em mostrar_pontos: {str(e)}")

class APITempoReal:
    """Classe para integração com API de tempo real da SPTrans"""
    
    def __init__(self, token: str):
        self.token = token
        self.base_url = "http://api.olhovivo.sptrans.com.br/v2.1"
        self.session = requests.Session()
        self.authenticated = False
        
    def autenticar(self) -> bool:
        """Autentica na API Olho Vivo"""
        try:
            response = self.session.post(
                f"{self.base_url}/Login/Autenticar",
                data={'token': self.token}
            )
            self.authenticated = response.json()
            return self.authenticated
        except Exception as e:
            logging.error(f"Erro na autenticação: {str(e)}")
            return False
    
    def buscar_posicoes_veiculos(self, linha: str = None) -> List[Dict]:
        """Busca posições dos veículos em tempo real"""
        if not self.authenticated:
            if not self.autenticar():
                return []
        
        try:
            url = f"{self.base_url}/Posicao"
            if linha:
                url = f"{self.base_url}/Posicao/Linha?codigoLinha={linha}"
            
            response = self.session.get(url)
            return response.json()
        except Exception as e:
            logging.error(f"Erro ao buscar posições: {str(e)}")
            return []
    
    def buscar_previsao_chegada(self, stop_id: str) -> List[Dict]:
        """Busca previsão de chegada em um ponto específico"""
        if not self.authenticated:
            if not self.autenticar():
                return []
        
        try:
            response = self.session.get(
                f"{self.base_url}/Previsao/Parada?codigoParada={stop_id}"
            )
            return response.json()
        except Exception as e:
            logging.error(f"Erro ao buscar previsões: {str(e)}")
            return []

def adicionar_aba_tempo_real(notebook_tabelas: ttk.Notebook, dados: DadosGTFS):
    """Adiciona aba de tempo real à interface"""
    frame_tempo_real = ttk.Frame(notebook_tabelas)
    notebook_tabelas.add(frame_tempo_real, text="Tempo Real")
    
    # Configuração da API
    frame_config = ttk.LabelFrame(frame_tempo_real, text="Configuração API")
    frame_config.pack(fill=tk.X, padx=5, pady=5)
    
    ttk.Label(frame_config, text="Token API:").pack(side=tk.LEFT)
    token_var = tk.StringVar()
    entry_token = ttk.Entry(frame_config, textvariable=token_var, width=40)
    entry_token.pack(side=tk.LEFT, padx=5)
    
    api = None
    
    def conectar_api():
        nonlocal api
        token = token_var.get()
        if not token:
            messagebox.showerror("Erro", "Por favor, insira um token válido")
            return
        
        api = APITempoReal(token)
        if api.autenticar():
            messagebox.showinfo("Sucesso", "Conexão com API estabelecida!")
            btn_atualizar.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Erro", "Falha na autenticação com a API")
    
    btn_conectar = ttk.Button(frame_config, text="Conectar", command=conectar_api)
    btn_conectar.pack(side=tk.LEFT, padx=5)
    
    # Controles de busca
    frame_controles = ttk.Frame(frame_tempo_real)
    frame_controles.pack(fill=tk.X, padx=5, pady=5)
    
    ttk.Label(frame_controles, text="Buscar por:").pack(side=tk.LEFT)
    
    tipo_busca = tk.StringVar(value="linha")
    ttk.Radiobutton(frame_controles, text="Linha", variable=tipo_busca, value="linha").pack(side=tk.LEFT, padx=5)
    ttk.Radiobutton(frame_controles, text="Parada", variable=tipo_busca, value="parada").pack(side=tk.LEFT, padx=5)
    
    ttk.Label(frame_controles, text="Código:").pack(side=tk.LEFT, padx=5)
    codigo_var = tk.StringVar()
    entry_codigo = ttk.Entry(frame_controles, textvariable=codigo_var, width=10)
    entry_codigo.pack(side=tk.LEFT)
    
    # Área de resultados
    frame_resultados = ttk.Frame(frame_tempo_real)
    frame_resultados.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    tree_resultados = ttk.Treeview(frame_resultados, columns=("Tipo", "Detalhes"), show="headings")
    tree_resultados.heading("Tipo", text="Tipo")
    tree_resultados.heading("Detalhes", text="Detalhes")
    tree_resultados.column("Tipo", width=150, anchor="w")
    tree_resultados.column("Detalhes", width=400, anchor="w")
    
    vsb = ttk.Scrollbar(frame_resultados, orient="vertical", command=tree_resultados.yview)
    hsb = ttk.Scrollbar(frame_resultados, orient="horizontal", command=tree_resultados.xview)
    tree_resultados.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    tree_resultados.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    vsb.pack(side=tk.RIGHT, fill=tk.Y)
    hsb.pack(side=tk.BOTTOM, fill=tk.X)
    
    def atualizar_dados():
        if not api or not api.authenticated:
            messagebox.showerror("Erro", "Conecte-se à API primeiro")
            return
        
        tree_resultados.delete(*tree_resultados.get_children())
        codigo = codigo_var.get()
        tipo = tipo_busca.get()
        
        if not codigo:
            messagebox.showerror("Erro", "Informe um código para busca")
            return
        
        def buscar_e_exibir():
            try:
                if tipo == "linha":
                    dados = api.buscar_posicoes_veiculos(codigo)
                    if dados and 'vs' in dados:
                        for veiculo in dados['vs']:
                            tree_resultados.insert("", "end", values=(
                                "Veículo",
                                f"Prefixo: {veiculo.get('p')} | Lat: {veiculo.get('py')}, Lon: {veiculo.get('px')}"
                            ))
                elif tipo == "parada":
                    dados = api.buscar_previsao_chegada(codigo)
                    if dados and 'p' in dados:
                        parada = dados['p']
                        tree_resultados.insert("", "end", values=(
                            "Parada",
                            f"{parada.get('np')} - {parada.get('ed')}"
                        ))
                        if 'vs' in parada:
                            for previsao in parada['vs']:
                                tree_resultados.insert("", "end", values=(
                                    "Previsão",
                                    f"Linha: {previsao.get('c')} | Chega em: {previsao.get('t')} min | Destino: {previsao.get('lt1')}"
                                ))
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao buscar dados: {str(e)}")
        
        # Executar em thread para não travar a interface
        Thread(target=buscar_e_exibir, daemon=True).start()
    
    btn_atualizar = ttk.Button(
        frame_controles,
        text="Atualizar",
        command=atualizar_dados,
        state=tk.DISABLED
    )
    btn_atualizar.pack(side=tk.LEFT, padx=5)
    
    # Botão para mostrar no mapa
    def mostrar_no_mapa():
        selecao = tree_resultados.selection()
        if not selecao:
            return
        
        item = tree_resultados.item(selecao[0])
        valores = item['values']
        
        if valores and valores[0] == "Veículo":
            # Extrair coordenadas do veículo
            partes = valores[1].split('|')
            lat = partes[1].split(':')[1].strip().split(',')[0]
            lon = partes[2].split(':')[1].strip()
            
            m = folium.Map(location=[float(lat), float(lon)], zoom_start=16)
            folium.Marker(
                location=[float(lat), float(lon)],
                popup=f"Veículo {partes[0].split(':')[1].strip()}",
                icon=folium.Icon(color='green')
            ).add_to(m)
            
            m.save("Mapa_dos_Trilhos\\mapa_tempo_real.html")
            webbrowser.open("Mapa_dos_Trilhos\\mapa_tempo_real.html")
    
    btn_mapa = ttk.Button(
        frame_controles,
        text="Mostrar no Mapa",
        command=mostrar_no_mapa
    )
    btn_mapa.pack(side=tk.LEFT, padx=5)

class CalculadorRotas:
    """Classe para cálculo de rotas e conexões"""
    
    def __init__(self, dados: DadosGTFS):
        self.dados = dados
        self.grafo = self.construir_grafo()
    
    def construir_grafo(self) -> Dict[str, Dict[str, Dict]]:
        """Constrói grafo de conexões entre paradas"""
        grafo = {}
        
        # Mapear todas as paradas
        for stop in self.dados.stops:
            grafo[stop['stop_id']] = {}
        
        # Adicionar conexões baseadas nas viagens
        for trip in self.dados.trips:
            route_id = trip['route_id']
            stop_times = [st for st in self.dados.stop_times if st['trip_id'] == trip['trip_id']]
            
            # Ordenar por sequence
            stop_times.sort(key=lambda x: int(x['stop_sequence']))
            
            # Adicionar arestas ao grafo
            for i in range(len(stop_times) - 1):
                origem = stop_times[i]['stop_id']
                destino = stop_times[i+1]['stop_id']
                tempo = self.calcular_tempo_viagem(
                    stop_times[i]['departure_time'],
                    stop_times[i+1]['arrival_time']
                )
                
                # Criar informação da conexão
                conexao = {
                    'tempo': tempo,
                    'rota': route_id,
                    'trip_id': trip['trip_id']
                }
                
                # Adicionar conexão se não existir ou se for mais rápida
                if destino not in grafo[origem] or grafo[origem][destino]['tempo'] > tempo:
                    grafo[origem][destino] = conexao
        
        return grafo
    
    def calcular_tempo_viagem(self, partida: str, chegada: str) -> int:
        """Calcula tempo de viagem em minutos entre duas paradas"""
        try:
            fmt = "%H:%M:%S"
            t1 = datetime.strptime(partida, fmt)
            t2 = datetime.strptime(chegada, fmt)
            
            # Lidar com horários que passam da meia-noite
            if t2 < t1:
                t2 += timedelta(days=1)
            
            return int((t2 - t1).total_seconds() / 60)
        except:
            return float('inf')  # Retornar infinito em caso de erro
    
    def encontrar_melhor_rota(self, origem_id: str, destino_id: str) -> Dict:
        """Encontra a melhor rota usando algoritmo Dijkstra"""
        if origem_id not in self.grafo or destino_id not in self.grafo:
            return None
        
        # Inicialização
        distancias = {stop: float('inf') for stop in self.grafo}
        distancias[origem_id] = 0
        predecessores = {stop: None for stop in self.grafo}
        visitados = set()
        
        while True:
            # Encontrar nó não visitado com menor distância
            nao_visitados = {stop: dist for stop, dist in distancias.items() if stop not in visitados}
            if not nao_visitados:
                break
                
            atual = min(nao_visitados, key=nao_visitados.get)
            if atual == destino_id:
                break
                
            visitados.add(atual)
            
            # Atualizar distâncias dos vizinhos
            for vizinho, info in self.grafo[atual].items():
                nova_dist = distancias[atual] + info['tempo']
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    predecessores[vizinho] = {
                        'de': atual,
                        'rota': info['rota'],
                        'trip_id': info['trip_id']
                    }
        
        # Reconstruir caminho
        if distancias[destino_id] == float('inf'):
            return None
            
        caminho = []
        atual = destino_id
        
        while predecessores[atual]:
            anterior = predecessores[atual]
            caminho.insert(0, {
                'de': anterior['de'],
                'para': atual,
                'rota': anterior['rota'],
                'trip_id': anterior['trip_id'],
                'tempo': self.grafo[anterior['de']][atual]['tempo']
            })
            atual = anterior['de']
        
        return {
            'paradas': caminho,
            'tempo_total': distancias[destino_id],
            'transfers': len({step['rota'] for step in caminho}) - 1
        }

def adicionar_aba_calculo_rotas(notebook_tabelas: ttk.Notebook, dados: DadosGTFS):
    """Adiciona aba para cálculo de rotas"""
    frame_rotas = ttk.Frame(notebook_tabelas)
    notebook_tabelas.add(frame_rotas, text="Calcular Rotas")
    
    calculador = CalculadorRotas(dados)
    
    # Frame de entrada
    frame_entrada = ttk.Frame(frame_rotas)
    frame_entrada.pack(fill=tk.X, padx=5, pady=5)
    
    # Origem
    ttk.Label(frame_entrada, text="Origem:").grid(row=0, column=0, padx=5, sticky='e')
    origem_var = tk.StringVar()
    combo_origem = ttk.Combobox(frame_entrada, textvariable=origem_var, width=50)
    combo_origem.grid(row=0, column=1, padx=5, sticky='we')
    
    # Destino
    ttk.Label(frame_entrada, text="Destino:").grid(row=1, column=0, padx=5, sticky='e')
    destino_var = tk.StringVar()
    combo_destino = ttk.Combobox(frame_entrada, textvariable=destino_var, width=50)
    combo_destino.grid(row=1, column=1, padx=5, sticky='we')
    
    # Preencher combobox com paradas
    paradas = [(stop['stop_id'], stop['stop_name']) for stop in dados.stops]
    paradas.sort(key=lambda x: x[1])
    combo_origem['values'] = [f"{nome} ({id})" for id, nome in paradas]
    combo_destino['values'] = [f"{nome} ({id})" for id, nome in paradas]
    
    # Frame de resultados
    frame_resultados = ttk.Frame(frame_rotas)
    frame_resultados.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    texto_resultado = ScrolledText(frame_resultados, wrap=tk.WORD)
    texto_resultado.pack(fill=tk.BOTH, expand=True)
    
    def extrair_id_parada(texto: str) -> str:
        """Extrai o ID da parada do texto do combobox"""
        if '(' in texto and ')' in texto:
            return texto.split('(')[-1].rstrip(')')
        return texto
    
    def calcular_rota():
        origem_id = extrair_id_parada(origem_var.get())
        destino_id = extrair_id_parada(destino_var.get())
        
        if not origem_id or not destino_id:
            messagebox.showerror("Erro", "Selecione origem e destino")
            return
        
        rota = calculador.encontrar_melhor_rota(origem_id, destino_id)
        
        texto_resultado.delete(1.0, tk.END)
        
        if not rota:
            texto_resultado.insert(tk.END, "Nenhuma rota encontrada entre os pontos selecionados.")
            return
        
        texto_resultado.insert(tk.END, f"ROTA ENCONTRADA\n{'='*40}\n")
        texto_resultado.insert(tk.END, f"Tempo total: {rota['tempo_total']} minutos\n")
        texto_resultado.insert(tk.END, f"Transferências: {rota['transfers']}\n\n")
        
        for i, passo in enumerate(rota['paradas'], 1):
            parada_origem = dados.stop_map.get(passo['de'], {}).get('stop_name', passo['de'])
            parada_destino = dados.stop_map.get(passo['para'], {}).get('stop_name', passo['para'])
            rota_nome = next(
                (r['route_long_name'] for r in dados.routes if r['route_id'] == passo['rota']),
                passo['rota']
            )
            
            texto_resultado.insert(tk.END, f"{i}. Pegar {rota_nome}:\n")
            texto_resultado.insert(tk.END, f"   - Embarque: {parada_origem}\n")
            texto_resultado.insert(tk.END, f"   - Desembarque: {parada_destino}\n")
            texto_resultado.insert(tk.END, f"   - Tempo de viagem: {passo['tempo']} minutos\n\n")
    
    btn_calcular = ttk.Button(
        frame_entrada,
        text="Calcular Rota",
        command=calcular_rota
    )
    btn_calcular.grid(row=2, column=0, columnspan=2, pady=10)
    
    def mostrar_mapa_rota():
        origem_id = extrair_id_parada(origem_var.get())
        destino_id = extrair_id_parada(destino_var.get())
        
        if not origem_id or not destino_id:
            messagebox.showerror("Erro", "Selecione origem e destino")
            return
        
        rota = calculador.encontrar_melhor_rota(origem_id, destino_id)
        
        if not rota:
            messagebox.showerror("Erro", "Nenhuma rota encontrada para mostrar no mapa")
            return
        
        m = folium.Map(
            location=[-23.5505, -46.6333],
            zoom_start=12
        )
        
        # Adicionar marcadores para origem e destino
        origem = dados.stop_map.get(origem_id)
        destino = dados.stop_map.get(destino_id)
        
        if origem:
            folium.Marker(
                location=[float(origem['stop_lat']), float(origem['stop_lon'])],
                popup=f"ORIGEM: {origem['stop_name']}",
                icon=folium.Icon(color='green', icon='home')
            ).add_to(m)
        
        if destino:
            folium.Marker(
                location=[float(destino['stop_lat']), float(destino['stop_lon'])],
                popup=f"DESTINO: {destino['stop_name']}",
                icon=folium.Icon(color='red', icon='flag')
            ).add_to(m)
        
        # Adicionar trajetos das rotas
        cores = ['blue', 'purple', 'orange', 'darkred', 'lightblue']
        
        for i, passo in enumerate(rota['paradas']):
            # Encontrar shape_id para esta trip
            trip = dados.trip_map.get(passo['trip_id'], {})
            shape_id = trip.get('shape_id')
            
            if shape_id:
                # Carregar shape do arquivo shapes.txt
                shape_points = []
                with open('Mapa_dos_Trilhos\\Gtfs_SPTRANS\\shapes.txt', 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row['shape_id'] == shape_id:
                            shape_points.append((
                                float(row['shape_pt_lat']),
                                float(row['shape_pt_lon'])
                            ))
                
                if shape_points:
                    folium.PolyLine(
                        shape_points,
                        weight=3,
                        opacity=0.7,
                        popup=f"Linha: {passo['rota']}"
                    ).add_to(m)
        
        m.save("Mapa_dos_Trilhos\\mapa_rota.html")
        webbrowser.open("Mapa_dos_Trilhos\\mapa_rota.html")
    
    btn_mapa = ttk.Button(
        frame_entrada,
        text="Mostrar no Mapa",
        command=mostrar_mapa_rota
    )
    btn_mapa.grid(row=3, column=0, columnspan=2, pady=5)

import pandas as pd
from tkinter import filedialog

def adicionar_menu_exportacao(root: tk.Tk, dados: DadosGTFS):
    """Adiciona menu de exportação à janela principal"""
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    menu_exportar = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Exportar", menu=menu_exportar)
    
    # Exportar rotas
    menu_exportar.add_command(
        label="Rotas (CSV)",
        command=lambda: exportar_dados(
            dados.routes,
            "routes",
            ["route_id", "route_short_name", "route_long_name", "route_type"]
        )
    )
    
    # Exportar paradas
    menu_exportar.add_command(
        label="Paradas (CSV)",
        command=lambda: exportar_dados(
            dados.stops,
            "stops",
            ["stop_id", "stop_name", "stop_lat", "stop_lon", "stop_desc"]
        )
    )
    
    # Exportar horários
    menu_exportar.add_command(
        label="Horários (Excel)",
        command=lambda: exportar_horarios_excel(dados)
    )
    
    # Exportar tudo em JSON
    menu_exportar.add_command(
        label="Todos dados (JSON)",
        command=lambda: exportar_todos_json(dados)
    )

def exportar_dados(dados: List[Dict], nome_base: str, campos: List[str]):
    """Exporta dados para CSV"""
    try:
        filepath = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")],
            initialfile=f"{nome_base}.csv"
        )
        
        if not filepath:
            return
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(
                {k: v for k, v in item.items() if k in campos}
                for item in dados
            )
        
        messagebox.showinfo("Sucesso", f"Dados exportados para {filepath}")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao exportar: {str(e)}")
        logging.error(f"Erro ao exportar {nome_base}: {str(e)}")

def exportar_horarios_excel(dados: DadosGTFS):
    """Exporta horários para arquivo Excel"""
    try:
        filepath = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel Files", "*.xlsx")],
            initialfile="horarios.xlsx"
        )
        
        if not filepath:
            return
        
        # Criar um Excel writer
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            # Exportar stop_times
            df_stop_times = pd.DataFrame(dados.stop_times)
            df_stop_times.to_excel(writer, sheet_name='stop_times', index=False)
            
            # Exportar trips
            df_trips = pd.DataFrame(dados.trips)
            df_trips.to_excel(writer, sheet_name='trips', index=False)
            
            # Exportar frequencies
            df_freq = pd.DataFrame(dados.frequencies)
            df_freq.to_excel(writer, sheet_name='frequencies', index=False)
        
        messagebox.showinfo("Sucesso", f"Horários exportados para {filepath}")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao exportar horários: {str(e)}")
        logging.error(f"Erro ao exportar horários: {str(e)}")

def exportar_todos_json(dados: DadosGTFS):
    """Exporta todos os dados para um arquivo JSON"""
    try:
        filepath = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json")],
            initialfile="sptrans_data.json"
        )
        
        if not filepath:
            return
        
        todos_dados = {
            'routes': dados.routes,
            'trips': dados.trips,
            'stop_times': dados.stop_times,
            'stops': dados.stops,
            'frequencies': dados.frequencies,
            'calendar': dados.calendar,
            'fare_attributes': dados.fare_attributes
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(todos_dados, f, ensure_ascii=False, indent=2)
        
        messagebox.showinfo("Sucesso", f"Todos dados exportados para {filepath}")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao exportar dados: {str(e)}")
        logging.error(f"Erro ao exportar todos dados: {str(e)}")
        
if __name__ == "__main__":
    sptrans()