# Mapas dos Trilhos/Ônibus/Ciclovias de São Paulo
![Version](https://img.shields.io/badge/Vers%C3%A3o-1.1.0-blue.svg)
![Atualização](https://img.shields.io/badge/Atualiza%C3%A7%C3%A3o-18/07/2024-green.svg)

<img align="right" src="https://github.com/Rafabs/SP-4-u/blob/main/Mapa_dos_Trilhos/Icons/SP4U.gif" alt="Logo" width="150" height="150" />

Bem-vindo ao repositório de Sampa 4u! Neste repositório, você encontrará uma coleção de códigos que geram mapas das linhas de Metrô, CPTM, Via Quatro e Via Mobilidade, além de corredores da SPTrans/EMTU e informações sobre ciclovias e bicicletários usando Python, HTML5, CSS3, JS e NODE.JS.

## Sobre

Este repositório foi criado com o objetivo de demonstrar como criar visualizações simples de mapas de linhas de metrô, trens e ônibus usando a biblioteca Tkinter. Cada script contido neste repositório representa uma linha diferente e usa elementos gráficos para criar um mapa que mostra as estações, as conexões e os trajetos possíveis, além de verificar o trânsito no sentido Centro-Bairro ou Bairro-Centro, a hora e a temperatura na cidade de São Paulo, as linhas que estão em construção não constam no mapa de trajetos, porém consta no mapa global.

Saiba mais sobre este projeto acessando o arquivo html em [SOBRE](https://github.com/Rafabs/SP-4-u/blob/main/Mapa_dos_Trilhos/Sobre/index.html)

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

Cada arquivo `.py` na pasta `Mapa_dos_Trilhos` corresponde a um mapa de uma linha específica. Você pode explorar cada arquivo para ver como os mapas estão sendo criados e personalizados usando o Tkinter.

Cada arquivo `.json` e `.geojson` na pasta `Mapa_dos_Trilhos/Data` corresponde a dados de toda a malha ferroviária e rodoviária EMTU/METRA/SPTRANS. 

Cada arquivo `.png` na pasta `Mapa_dos_Trilhos/Icons` foram extraídos do [Flaticon](https://www.flaticon.com/), exceto os logotipos, que foram extraídos dos sites oficiais.

Os arquivos de Fontes usados no CSS3 foram extraídos do GitHub do [Google](https://github.com/google/fonts/?tab=readme-ov-file)


## Última Atualização - METRÔ/CPTM/ViaMobilidade

Inclusão da(s) linha(s):
Nada para mostrar aqui.

Modificação da(s) linha(s):
Nada para mostrar aqui.

Remoção da(s) linha(s):
Nada para mostrar aqui.

Alteração Tarifária:
Nada para mostrar aqui.

## Última Atualização - SPTrans

Inclusão da(s) linha(s):
Nada para mostrar aqui.

Modificação da(s) linha(s):
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/514T/10-006341.svg) Term. Sacomã - Jd. Itápolis
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/514T/10-006341.svg) Term. Sacomã - Conj. Hab. Teotônio Vilela

Remoção da(s) linha(s):
Nada para mostrar aqui.

Alteração Tarifária:
Nada para mostrar aqui.

## Última Atualização - EMTU

Inclusão da(s) linha(s):
- ![Linha](https://img.shields.io/badge/VLT--Binário-0455A1.svg) SANTOS (ESTACAO VLT CONSELHEIRO NEBIAS) - SANTOS (ESTACAO VALONGO)
- ![Linha](https://img.shields.io/badge/5113PR1-0455A1.svg) SANTA BRANCA (JARDIM ALBUQUERQUE) - JACAREI (TERMINAL RODOVIARIO DE JACAREI)
- ![Linha](https://img.shields.io/badge/5311EX1-0455A1.svg) GUARATINGUETA (TERMINAL RODOVIARIO DE GUARATINGUETA) - PINDAMONHANGABA (CENTRO)
- 
Modificação da(s) linha(s):
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/042VP1-0455A1.svg) MAIRIPORA (ESPACO PAULO AMAURY SERRALVO) - SAO PAULO (TERMINAL RODOVIARIO TIETE)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/042VP1-0455A1.svg) MAIRIPORA (TERMINAL RODOVIARIO CIDADE BONITA SIGUEMI AIACYDA) - SAO PAULO (TERMINAL RODOVIARIO TIETE)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/049-0455A1.svg) MAIRIPORA (ESPACO PAULO AMAURY SERRALVO) - FRANCO DA ROCHA (CENTRO)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/049-0455A1.svg) MAIRIPORA (TERMINAL RODOVIARIO CIDADE BONITA SIGUEMI AIACYDA) - FRANCO DA ROCHA (CENTRO)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/064-0455A1.svg) MAUA (JARDIM GUAPITUBA) - SAO CAETANO DO SUL (BAIRRO SANTO ANTONIO)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/064-0455A1.svg) MAUA (JARDIM GUAPITUBA) - SAO CAETANO DO SUL (TERMINAL RODOVIARIO NICOLAU DELIC)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/158BI1-0455A1.svg) MAUA (JARDIM ZAIRA) - SAO CAETANO DO SUL (BAIRRO SANTO ANTONIO)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/158BI1-0455A1.svg) MAUA (JARDIM ZAIRA) - SAO CAETANO DO SUL (TERMINAL RODOVIARIO NICOLAU DELIC)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/160EX1-0455A1.svg) MAUA  (JARDIM ITAPEVA) - SAO CAETANO DO SUL (BAIRRO SANTO ANTONIO)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/160EX1-0455A1.svg) MAUA  (JARDIM ITAPEVA) - SAO CAETANO DO SUL (TERMINAL RODOVIARIO NICOLAU DELIC)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/240-0455A1.svg) MAIRIPORA (ESPACO PAULO AMAURY SERRALVO) - SAO PAULO (TERMINAL RODOVIARIO DO TIETE)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/240-0455A1.svg) MAIRIPORA (TERMINAL RODOVIARIO CIDADE BONITA SIGUEMI AIACYDA) - SAO PAULO (TERMINAL RODOVIARIO DO TIETE)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/271-0455A1.svg) MAIRIPORA (ESPACO PAULO AMAURY SERRALVO) - SAO PAULO (PEDRA BRANCA)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/271-0455A1.svg) MAIRIPORA (TERMINAL RODOVIARIO CIDADE BONITA SIGUEMI AIACYDA) - SAO PAULO (PEDRA BRANCA)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/382-0455A1.svg) MAUA (BAIRRO FEITAL) - SAO CAETANO DO SUL ( BAIRRO SANTO ANTONIO)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/382-0455A1.svg) MAUA (BAIRRO FEITAL) - SAO CAETANO DO SUL (TERMINAL RODOVIARIO NICOLAU DELIC)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/382EX1-0455A1.svg) MAUA (JARDIM ITAPEVA) - SAO CAETANO DO SUL (BAIRRO SANTO ANTONIO)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/382EX1-0455A1.svg) MAUA (JARDIM ITAPEVA) - SAO CAETANO DO SUL (TERMINAL RODOVIARIO NICOLAU DELIC)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/403-0455A1.svg) MAUA (VILA NOVA MAUA) - SAO CAETANO DO SUL (SANTO ANTONIO)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/403-0455A1.svg) MAUA (VILA NOVA MAUA) - SAO CAETANO DO SUL (TERMINAL RODOVIARIO NICOLAU DELIC)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/454-0455A1.svg) JANDIRA (CONDOMINIO RESERVA DE SANTA MARIA) - BARUERI (TERMINAL RODOFERROVIARIO GUALBERTO TOLAINE)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/454-0455A1.svg) JANDIRA (CONDOMINIO RESERVA DE SANTA MARIA) - BARUERI (CENTRO)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/455-0455A1.svg) BARUERI (ALPHAVILLE) - CARAPICUIBA (ALDEIA)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/455-0455A1.svg) CARAPICUIBA (ALDEIA) - BARUERI (ALPHAVILLE)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/566-0455A1.svg) MAIRIPORA (ESPACO PAULO AMAURY SERRALVO) - SAO PAULO (TERMINAL RODOVIARIO TIETE)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/566-0455A1.svg) MAIRIPORA (TERMINAL RODOVIARIO CIDADE BONITA SIGUEMI AIACYDA) - SAO PAULO (TERMINAL RODOVIARIO TIETE)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/612-0455A1.svg) JAGUARIUNA (JOAO NASSIF) - CAMPINAS (TERMINAL METROPOLITANO PREFEITO MAGALHAES TEIXEIRA)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/612-0455A1.svg) JAGUARIUNA (VARGEAO) - CAMPINAS (TERMINAL METROPOLITANO PREFEITO MAGALHAES TEIXEIRA)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/612DV1-0455A1.svg) JAGUARIUNA (JOAO NASSIF) - CAMPINAS (TERMINAL METROPOLITANO PREFEITO MAGALHAES TEIXEIRA)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/612DV1-0455A1.svg) JAGUARIUNA (VARGEAO) - CAMPINAS (TERMINAL METROPOLITANO PREFEITO MAGALHAES TEIXEIRA)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/6320BI1-0455A1.svg) ARACOIABA DA SERRA (BAIRRO FARIAS) - SOROCABA (CENTRO)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/6320BI1-0455A1.svg) ARACOIABA DA SERRA (MARIA PAULA ESPOSITO) - SOROCABA (TERMINAL SAO PAULO)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/736-0455A1.svg) ARTUR NOGUEIRA (CORACAO CRIANCA) - HOLAMBRA (PORTAL TURISTICO DE HOLAMBRA)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/736-0455A1.svg) ARTUR NOGUEIRA (CORACAO CRIANCA) - HOLAMBRA (TREVO DA POSSE)
- ![Linha](https://img.shields.io/badge/ANTES-red.svg) ![Linha](https://img.shields.io/badge/822-0455A1.svg) MAIRIPORA (ESPACO PAULO AMAURY SERRALVO) - SAO PAULO (METRO PARADA INGLESA)
- ![Linha](https://img.shields.io/badge/AGORA-green.svg) ![Linha](https://img.shields.io/badge/822-0455A1.svg) MAIRIPORA (TERMINAL RODOVIARIO CIDADE BONITA SIGUEMI AIACYDA) - SAO PAULO (METRO PARADA INGLESA)
  
Remoção da(s) linha(s):
- ![Linha](https://img.shields.io/badge/911DV1-0455A1.svg) PRAIA GRANDE (TERMINAL RODOVIARIO E URBANO TATICO FRANCISCO GOMES DA SILVA) - CUBATAO (USIMINAS)
- ![Linha](https://img.shields.io/badge/059-0455A1.svg) OSASCO (CONJUNTO DOS METALURGICOS) - SAO PAULO (METRO BUTANTA) 
- ![Linha](https://img.shields.io/badge/059PR1-0455A1.svg) CARAPICUIBA (JARDIM NOVO HORIZONTE) - SAO PAULO (METRO BUTANTA)
- ![Linha](https://img.shields.io/badge/060BI1-0455A1.svg) OSASCO (JARDIM SANTA MARIA) - SAO PAULO (METRO BUTANTA)
- ![Linha](https://img.shields.io/badge/076-0455A1.svg) ITAQUAQUECETUBA (TERMINAL URBANO ENGENHEIRO MANOEL FEIO) - SAO PAULO (METRO BRAS)
- ![Linha](https://img.shields.io/badge/093-0455A1.svg) GUARULHOS (TERMINAL METROPOLITANO VILA GALVAO) - SAO PAULO (METRO CARRAO)
- ![Linha](https://img.shields.io/badge/116-0455A1.svg) BARUERI (CENTRO) - SAO PAULO (METRO ARMENIA)
- ![Linha](https://img.shields.io/badge/121-0455A1.svg) GUARULHOS (TERMINAL METROPOLITANO TABOAO) - SAO PAULO (PENHA)
- ![Linha](https://img.shields.io/badge/148EX1-0455A1.svg) SAO BERNARDO DO CAMPO (UFABC) - SAO BERNARDO DO CAMPO (AVENIDA KENNEDY)
- ![Linha](https://img.shields.io/badge/165BI1-0455A1.svg) SANTO ANDRE (PARQUE REPRESA BILLINGS) - SAO BERNARDO DO CAMPO (TERMINAL PACO - SAO BERNARDO)
- ![Linha](https://img.shields.io/badge/187-0455A1.svg) MAIRIPORA (ESPACO PAULO AMAURY SERRALVO) - SAO PAULO (CAMPOS ELISEOS)
- ![Linha](https://img.shields.io/badge/210-0455A1.svg) BIRITIBA MIRIM (CASA GRANDE) - MOGI DAS CRUZES (CENTRO)
- ![Linha](https://img.shields.io/badge/214VP1-0455A1.svg) ITAQUAQUECETUBA (RANCHO GRANDE) - SAO PAULO (TERMINAL RODOVIARIO TIETE)
- ![Linha](https://img.shields.io/badge/227DV1-0455A1.svg) GUARULHOS (JARDIM LEBLON) - SAO PAULO (METRO ARMENIA)
- ![Linha](https://img.shields.io/badge/278-0455A1.svg) OSASCO (CENTRO) - GUARULHOS (TERMINAL URBANO GUARULHOS)
- ![Linha](https://img.shields.io/badge/302-0455A1.svg) ITAQUAQUECETUBA (TERMINAL URBANO ENGENHEIRO MANOEL FEIO) - ITAQUAQUECETUBA (JARDIM PINHEIRINHO)
- ![Linha](https://img.shields.io/badge/337BI1-0455A1.svg) GUARULHOS (RECREIO SAO JORGE) - SAO PAULO (TERMINAL RODOVIARIO TIETE)
- ![Linha](https://img.shields.io/badge/470-0455A1.svg) SANTO ANDRE (TERMINAL METROPOLITANO SANTO ANDRE LESTE) - SAO PAULO (AEROPORTO DE CONGONHAS)
- ![Linha](https://img.shields.io/badge/337478BI1BI1-0455A1.svg) GUARULHOS (JARDIM DAS NACOES) - SAO PAULO (METRO ARMENIA)
- ![Linha](https://img.shields.io/badge/512-0455A1.svg) ITAQUAQUECETUBA (PARQUE PIRATININGA) - SAO PAULO (METRO ARMENIA)
- ![Linha](https://img.shields.io/badge/5210-0455A1.svg) CAMPOS DO JORDAO (TERMINAL RODOVIARIO DE CAMPOS DO JORDAO) - SAO JOSE DOS CAMPOS (TERMINAL RODOVIARIO FREDERICO OZANAM)
- ![Linha](https://img.shields.io/badge/5213-0455A1.svg) SAO BENTO DO SAPUCAI (TERMINAL RODOVIARIO DE SAO BENTO DO SAPUCAI) - SAO JOSE DOS CAMPOS (TERMINAL RODOVIARIO FREDERICO OZANAM)
- ![Linha](https://img.shields.io/badge/5320-0455A1.svg) CANAS (CENTRO) - LORENA (TERMINAL RODOVIARIO DE LORENA)
- ![Linha](https://img.shields.io/badge/540-0455A1.svg) BARUERI (ALDEIA DA SERRA) - COTIA (TERMINAL METROPOLITANO DE COTIA)
- ![Linha](https://img.shields.io/badge/574-0455A1.svg) GUARULHOS (JARDIM CUMBICA) - SAO PAULO (METRO CARRAO)
- ![Linha](https://img.shields.io/badge/605-0455A1.svg) PAULINIA (PAULINIA RODOVIARIA SHOPPING) - CAMPINAS (TERMINAL METROPOLITANO PREFEITO MAGALHAES TEIXEIRA)
- ![Linha](https://img.shields.io/badge/6104-0455A1.svg) CAPELA DO ALTO (JARDIM NOVA CAPELA) - IPERO (CENTRO)
- ![Linha](https://img.shields.io/badge/6108VP2-0455A1.svg) TATUI (CENTRO) - ARACOIABA DA SERRA (CENTRO)
- ![Linha](https://img.shields.io/badge/6213EX2-0455A1.svg) TATUI (CENTRO) - BOITUVA (FACULDADE IFSP)
- ![Linha](https://img.shields.io/badge/6216-0455A1.svg) MAIRINQUE (JARDIM CRUZEIRO) - SAO ROQUE (CATARINA FASHION OUTLET)
- ![Linha](https://img.shields.io/badge/6225EX1-0455A1.svg) ARACARIGUAMA (CENTRO) - ITU (TERMINAL CIDADE NOVA - PIRAPITINGUI)
- ![Linha](https://img.shields.io/badge/6301-0455A1.svg) PILAR DO SUL (BAIRRO CAMPO GRANDE) - PIEDADE (CENTRO)
- ![Linha](https://img.shields.io/badge/6303-0455A1.svg) PIEDADE (CENTRO) - SOROCABA (CENTRO)
- ![Linha](https://img.shields.io/badge/6330PR1-0455A1.svg) IPERO (G. OETTERER - INDUSTRIA DE ARTEFATOS) - SOROCABA (CENTRO)
- ![Linha](https://img.shields.io/badge/6334EX1-0455A1.svg) PILAR DO SUL (TERMINAL RODOVIARIO ANTONIO JOSE DA SILVA) - SOROCABA (TERMINAL RODOVIARIO DE SOROCABA)
- ![Linha](https://img.shields.io/badge/655DV1-0455A1.svg) SUMARE (TERMINAL RODOVIARIO DE SUMARE) - CAMPINAS (SHOPPING IGUATEMI)
- ![Linha](https://img.shields.io/badge/689-0455A1.svg) VALINHOS (TERMINAL RODOVIARIO MARIO ROLIM TELLES) - VINHEDO (TERMINAL RODOVIARIO DE VINHEDO)
- ![Linha](https://img.shields.io/badge/744-0455A1.svg) COSMOPOLIS (TERMINAL RODOVIARIO DE COSMOPOLIS) - CAMPINAS (TERMINAL METROPOLITANO PREFEITO MAGALHAES TEIXEIRA)
- ![Linha](https://img.shields.io/badge/800-0455A1.svg) MOGI DAS CRUZES (TERMINAL RODOVIARIO GERALDO SCAVONE) - GUARULHOS (AEROPORTO INTERNACIONAL DE SAO PAULO)
- ![Linha](https://img.shields.io/badge/828-0455A1.svg) JANDIRA (JARDIM NOSSA SENHORA DE FATIMA) - SANTANA DE PARNAIBA (TERMINAL RODOVIARIO ALPHAVILLE)
- ![Linha](https://img.shields.io/badge/829-0455A1.svg) ITAPECERICA DA SERRA (PARQUE PARAISO) - TABOAO DA SERRA (CENTRO)
- ![Linha](https://img.shields.io/badge/911DV1-0455A1.svg) PRAIA GRANDE (TERMINAL RODOVIARIO E URBANO TATICO FRANCISCO GOMES DA SILVA) - CUBATAO (USIMINAS)

Alteração Tarifária:
Nada para mostrar aqui.

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

Em ambos os sistemas operacionais, a tela que deverá ser exibida é parecida com o exemplo abaixo `main.py`:

<div style="display:flex; flex-direction:row;">
        <img src="https://github.com/Rafabs/SP-4-u/blob/e604f14d346b45c89f9bb0ef83f894d7f71efe63/Exibi%C3%A7%C3%A3o/PY_Imagens_projeto_v1.0.9%20(7).png" alt="Imagem 1" style="width:50%;">
        <img src="https://github.com/Rafabs/SP-4-u/blob/21c85e8f6c6a4d3466f9e92edb99bb4a4657c848/Exibi%C3%A7%C3%A3o/PY_Imagens_projeto_v1.0.9%20(10).png" alt="Imagem 2" style="width:50%;" >
</div>
<div style="display:flex; flex-direction:row;">
    <img src="https://github.com/Rafabs/SP-4-u/blob/21c85e8f6c6a4d3466f9e92edb99bb4a4657c848/Exibi%C3%A7%C3%A3o/PY_Imagens_projeto_v1.0.9%20(8).png" alt="Imagem 3" style="width:50%;">
    <img src="https://github.com/Rafabs/SP-4-u/blob/21c85e8f6c6a4d3466f9e92edb99bb4a4657c848/Exibi%C3%A7%C3%A3o/PY_Imagens_projeto_v1.0.9%20(9).png" alt="Imagem 4" style="width:50%;">
</div>

## Exibição (Web)

Em ambos os sistemas operacionais, a tela que deverá ser exibida é parecida com o exemplo abaixo `index.html`:

<div style="display:flex; flex-direction:row;">
        <img src="https://github.com/Rafabs/SP-4-u/blob/e604f14d346b45c89f9bb0ef83f894d7f71efe63/Exibi%C3%A7%C3%A3o/WEB_%20(3).png" alt="Imagem 1" style="width:50%;">
        <img src="https://github.com/Rafabs/SP-4-u/blob/8a92f6e914bf0c9be75ef931ae443d67f6134441/Exibi%C3%A7%C3%A3o/WEB_%20(1).png" alt="Imagem 2" style="width:50%;">
        <img src="https://github.com/Rafabs/SP-4-u/blob/8a92f6e914bf0c9be75ef931ae443d67f6134441/Exibi%C3%A7%C3%A3o/WEB_%20(2).png" alt="Imagem 3" style="width:50%;">
</div>

## Diagrama da versão atual v1.1.0
![Diagrama da versão atual v1.1.0](https://github.com/Rafabs/SP-4-u/blob/main/Diagrama/Diagrama_v1.1.0.png)

## To Do 
- [ ] Tornar o projeto responsível 
- [x] Desenvolver L6 em .py
- [x] Desenvolver L6 em .html
- [x] Desenvolver L17 em .py
- [x] Desenvolver L17 em .html 
- [x] Desenvolver as linhas 6 e 17 no mapa global em html
- [x] Atualizar Área de desenvolvimento 
- [ ] Atualizar diagrama
- [ ] Incluir Ortofoto 2004, 2017 ou 2020
- [ ] Atualizar diagrama
- [ ] Ajustar Config com todas as API's
- [ ] Inserir detlhes de algumas ações no diagrama
- [ ] Atualizar siglas das estações da L6

## Contribuição

Se você deseja contribuir para este repositório, sinta-se à vontade para fazer um fork, criar um branch com suas alterações e, em seguida, enviar um pull request. Você pode adicionar novos mapas de linhas, melhorar as existentes ou fazer correções.

## Agradecimentos

Obrigado por visitar este repositório! Espero que os mapas de linhas de metrô criados com Tkinter sejam úteis e informativos. Sinta-se à vontade para explorar, aprender e contribuir. Se tiver alguma dúvida ou sugestão, não hesite em abrir uma issue neste repositório.

Divirta-se explorando os mapas do transporte metropolitano de São Paulo!

> [!NOTE]
> Esse projeto foi construído apenas para fins de aprendizado, sem qualquer vínculo.

## Versões e Fases

O projeto está em constante evolução e passa por diferentes fases de desenvolvimento. Para mais informações, consulte [Versões](https://github.com/Rafabs/SP-4-u/blob/88acfd9d030c56f44776496af6f647b1a140efa0/Vers%C3%B5es/versao.md)

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE)
