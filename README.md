# Mapas dos Trilhos/Ônibus/Ciclovias de São Paulo
![Version](https://img.shields.io/badge/Vers%C3%A3o-1.0.8-blue.svg)
![Atualização](https://img.shields.io/badge/Atualiza%C3%A7%C3%A3o-05/03/2024-green.svg)

<img align="right" src="https://github.com/Rafabs/SP-4-u/blob/main/Mapa%20dos%20Trilhos/Icons/SP4U.gif" alt="Logo" width="150" height="150" />

Bem-vindo ao repositório de Sampa 4u! Neste repositório, você encontrará uma coleção de códigos que geram mapas das linhas de Metrô, CPTM, Via Quatro e Via Mobilidade, além de corredores da SPTrans/EMTU e informações sobre ciclovias e bicicletários usando Python, HTML5, CSS3, JS e NODE.JS.

## Sobre

Este repositório foi criado com o objetivo de demonstrar como criar visualizações simples de mapas de linhas de metrô, trens e ônibus usando a biblioteca Tkinter. Cada script contido neste repositório representa uma linha diferente e usa elementos gráficos para criar um mapa que mostra as estações, as conexões e os trajetos possíveis, além de verificar o trânsito no sentido Centro-Bairro ou Bairro-Centro, a hora e a temperatura na cidade de São Paulo, as linhas que estão em construção não constam no mapa de trajetos, porém consta no mapa global.

Saiba mais sobre este projeto acessando o arquivo html em [SOBRE](https://github.com/Rafabs/SP-4-u/blob/main/Mapa%20dos%20Trilhos/Sobre/index.html)

Cada linha recebeu uma cor em hexadecimal, de acordo com o GFTS da [SPTRANS](https://www.sptrans.com.br/desenvolvedores/login-desenvolvedores/), em ordem numérica:
- ![#0455A1](https://via.placeholder.com/15/0455A1/000000?text=+) `#0455A1` Linha 01 - Azul 
- ![#007E5E](https://via.placeholder.com/15/007E5E/000000?text=+) `#007E5E` Linha 02 - Verde  
- ![#EE372F](https://via.placeholder.com/15/EE372F/000000?text=+) `#EE372F` Linha 03 - Vermelha 
- ![#FFF000](https://via.placeholder.com/15/FFF000/000000?text=+) `#FFF000` Linha 04 - Amarela   
- ![#9B3894](https://via.placeholder.com/15/9B3894/000000?text=+) `#9B3894` Linha 05 - Lilás 
- ![#CA016B](https://via.placeholder.com/15/CA016B/000000?text=+) `#CA016B` Linha 07 - Rubi 
- ![#97A098](https://via.placeholder.com/15/97A098/000000?text=+) `#97A098` Linha 08 - Diamante 
- ![#01A9A7](https://via.placeholder.com/15/01A9A7/000000?text=+) `#01A9A7` Linha 09 - Esmeralda 
- ![#049FC3](https://via.placeholder.com/15/049FC3/000000?text=+) `#049FC3` Linha 10 - Turquesa 
- ![#F68368](https://via.placeholder.com/15/F68368/000000?text=+) `#F68368` Linha 11 - Coral 
- ![#133C8D](https://via.placeholder.com/15/133C8D/000000?text=+) `#133C8D` Linha 12 - Safira 
- ![#00B352](https://via.placeholder.com/15/00B352/000000?text=+) `#00B352` Linha 13 - Jade 
- ![#C0C0C0](https://via.placeholder.com/15/C0C0C0/000000?text=+) `#C0C0C0` Linha 15 - Prata 

Cada arquivo `.py` na pasta `Mapa dos Trilhos` corresponde a um mapa de uma linha específica. Você pode explorar cada arquivo para ver como os mapas estão sendo criados e personalizados usando o Tkinter.

Cada arquivo `.json` e `.geojson` na pasta `Mapa dos Trilhos/Data` corresponde a dados de toda a malha ferroviária e rodoviária EMTU/METRA/SPTRANS. 

Cada arquivo `.png` na pasta `Mapa dos Trilhos/Icons` foram extraídos do [Flaticon](https://www.flaticon.com/), exceto os logotipos, que foram extraídos dos sites oficiais.

Os arquivos de Fontes usados no CSS3 foram extraídos do GitHub do [Google](https://github.com/google/fonts/?tab=readme-ov-file)
## Bibliotecas Utilizadas

Para executar os scripts, você precisará das seguintes bibliotecas Python:
(No windows, copie e cole no terminal CMD para instalar as bibliotecas)
```python
pip install tk
pip install requests
pip install beautifulsoup4
pip install pillow
pip install folium
pip install geopandas
pip install json
pip install webbrowser
pip install datetime
pip install threading
pip install pyproj
pip install pymupdf
pip install selenium
pip install colorama
pip install logging
pip install atexit
pip install googlenews
pip install re
```

(No windows, copie e cole no terminal Node.js command prompt para instalar as bibliotecas)
```node.js
npm install express 
npm install axios 
npm install jsdom 
npm install cors
```
## Linguagens e IDE Utilizadas

![VSCode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Node](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)

## Fonte de dados

Todos os dados utilizados nesse projeto são em sua maioria abertos e alimentados pela comunidade, são eles:
- ![Download](https://img.shields.io/badge/Último_Download-23/10/2023-white.svg) [Citylines](https://www.citylines.co/data?city=sao-paulo#city) - Dados utilizados para plotagem do mapa.
- ![Download](https://img.shields.io/badge/Último_Download-03/01/2024-white.svg) [SPTrans](https://www.sptrans.com.br/desenvolvedores/perfil-desenvolvedor/) - Dados utilizados para buscar linhas.
- ![Download](https://img.shields.io/badge/Último_Download-11/01/2024-white.svg) [EMTU](https://www.emtu.sp.gov.br/emtu/dados-abertos/dados-abertos-principal/acesse-os-dados-abertos.fss) - Dados utilizados para buscar linhas.
- ![Download](https://img.shields.io/badge/Último_Download-20/10/2023-white.svg) [GEOSampa](https://geosampa.prefeitura.sp.gov.br/PaginasPublicas/_SBC.aspx) - Dados utilizados para buscar traçados e pontos de bicicletários e ciclovias. 
- ![Download](https://img.shields.io/badge/Último_Download-11/01/2024-white.svg) [METRÔ](https://www.metro.sp.gov.br/) - Extração do Mapa da Rede e do Guia do Usuário (em .PDF)
- ![Download](https://img.shields.io/badge/Último_Download-20/10/2023-white.svg) [METRÔ](http://catalogo.governoaberto.sp.gov.br/dataset/869-pesquisa-origem-e-destino) - Acesso às bases de dados da Pesquisa Origem e Destino dos anos de 1977, 1987, 1997 e 2007
- ![Download](https://img.shields.io/badge/Último_Download-20/10/2023-white.svg) [CPTM](https://www.cptm.sp.gov.br/Pages/Home.aspx) - Extração do Guia do Usuário (em .PDF)
- ![Download](https://img.shields.io/badge/Último_Download-Não_Aplicável-white.svg) [ViaMobilidade](https://www.viamobilidade.com.br/) - Extração de informações da operação e ocorrências (web scraping)
- ![Download](https://img.shields.io/badge/Último_Download-Não_Aplicável-white.svg) [World's Air Pollution](https://waqi.info/) - APi para amostragem da qualidade do ar
- ![Download](https://img.shields.io/badge/Último_Download-Não_Aplicável-white.svg) [News API](https://newsapi.org/) - APi para exibição de notícias na versão Web

## Como Executar (Projeto Python)

#### No Windows:

1. Abra o prompt de comando.

2. Navegue até o diretório onde está localizado o arquivo main.py usando o comando cd (por exemplo, cd C:\Caminho\Para\O\Projeto).

3. Execute o arquivo main.py usando o comando python main.py.

#### Linux e Mac:

1. Abra o terminal.

2. Navegue até o diretório onde está localizado o arquivo main.py usando o comando cd (por exemplo, cd /Caminho/Para/O/Projeto).

3. Execute o arquivo main.py usando o comando python3 main.py.

O projeto será iniciado e a interface gráfica será exibida.

Observação: Certifique-se de que você possui o Python instalado no seu sistema. Caso contrário, faça o download e a instalação a partir do site oficial do Python (https://www.python.org/).

## Como Executar (Projeto Web)

#### No Windows:

1. Abra o Node.js command prompt

2. digite node "caminho/para/o/aquivo/server.js"

3. Deverá ser exibido no terminal a mensagem ```Servidor funcionando normalmente na porta 3000```

4. Abre o arquivo html e navegue

#### Linux e Mac:

1. Abra o Node.js command prompt

2. digite node "caminho/para/o/aquivo/server.js"

3. Deverá ser exibido no terminal a mensagem ```Servidor funcionando normalmente na porta 3000```

4. Abre o arquivo html e navegue

Observação: Certifique-se de que você possui o Node.js instalado no seu sistema. Caso contrário, faça o download e a instalação a partir do site oficial (https://nodejs.org/en).

## Exibição (Python)

Em ambos os sistemas operacionais, a tela que deverá ser exibida é parecida com o exemplo abaixo ```main.py```:
![PÁGINA EM DESENVOLVIMENTO](https://github.com/Rafabs/SP-4-u/blob/main/Diagrama/Hist%C3%B3rico/app_v1.0.8.jpg)

## Exibição (Web)

Em ambos os sistemas operacionais, a tela que deverá ser exibida é parecida com o exemplo abaixo ```index.html```:
![PÁGINA EM DESENVOLVIMENTO](https://github.com/Rafabs/SP-4-u/blob/main/Diagrama/Hist%C3%B3rico/app_v1.0.8.jpg)

## Diagrama da versão atual v1.0.8
![Diagrama da versão atual v1.0.8](https://github.com/Rafabs/SP-4-u/blob/main/Diagrama/Diagrama_v1.0.8.png)

## To Do 
- [ ] ```EMERGENCIAL``` CORRIGIR TRECHO DA CET DE MAIN.PY.
- [ ] Criar mapa no HTML via js pelos dados json existente ```v1.0.9``` ```EM ANDAMENTO```.
- [ ] Atualizar o diagrama v1.0.9
- [ ] Python: Verificar possibilidade ao inicializar o programa, fazer uma varredura automática dos documentos disponíveis, exemplo: MAPA DAS LINHAS: OK.
- [ ] Web: Verificar possibilidade ao inicializar o programa, fazer uma varredura automática dos documentos disponíveis, exemplo: MAPA DAS LINHAS: OK.
- [ ] Corrigir erros e alertas de main.py
- [ ] Informar no status linha a última atualização do mesmo em index.html
- [ ] Ajustar favicon de index.html
- [ ] Renomear as pastas com espaços no nome por (_)
- [ ] Inserir imagens da execução no readme.md 

## Contribuição

Se você deseja contribuir para este repositório, sinta-se à vontade para fazer um fork, criar um branch com suas alterações e, em seguida, enviar um pull request. Você pode adicionar novos mapas de linhas, melhorar as existentes ou fazer correções.

## Agradecimentos

Obrigado por visitar este repositório! Espero que os mapas de linhas de metrô criados com Tkinter sejam úteis e informativos. Sinta-se à vontade para explorar, aprender e contribuir. Se tiver alguma dúvida ou sugestão, não hesite em abrir uma issue neste repositório.

Divirta-se explorando os mapas do transporte metropolitano de São Paulo!

> [!NOTE]
> Esse projeto foi construído apenas para fins de aprendizado, sem qualquer vínculo.

## Versões e Fases

O projeto está em constante evolução e passa por diferentes fases de desenvolvimento. Abaixo estão listadas as versões principais e as fases atuais

## Histórico das versões

### Versão ![Version](https://img.shields.io/badge/1.0.7-yellow.svg)

- Incrementação do Figma ao escopo do projeto e dados na versão web.
  
### Versão ![Version](https://img.shields.io/badge/1.0.6-yellow.svg)

- Incrementação das notícias na página principal do Projeto Python e do Projeto Web, além de informação de status das linhas na versão web.

### Versão ![Version](https://img.shields.io/badge/1.0.5-yellow.svg)

- Incrementação do mapa global, sendo um único mapa com todas as informações, câmadas e demais ferramentas.

### Versão ![Version](https://img.shields.io/badge/1.0.4-yellow.svg)

- Incrementação da malha de ciclovias, bicicletários públicos e dados de Origem e Destino 2007 e 2017.
  
### Versão ![Version](https://img.shields.io/badge/1.0.3-yellow.svg)

- Melhorias no design da tela inicial.

### Versão ![Version](https://img.shields.io/badge/1.0.2-yellow.svg)

- Incrementação do sistema de GFTS dos ônibus da SPTrans com o restante do projeto.

### Versão ![Version](https://img.shields.io/badge/1.0.1-yellow.svg)

- Incrementação do botão para acesso ao mapa da rede ferroviária e corredores de ônibus.
 
### Versão ![Version](https://img.shields.io/badge/1.0.0-yellow.svg)

- Descrição das linhas existentes ao lado em todos os mapas.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
