[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
function Get-Header {
    param (
        [string]$filePath,
        [string]$description,
        [datetime]$lastModified
    )
    
    $relativePath = $filePath.Replace((Get-Location).Path + "\", "").Replace("\", "/")
    $formattedDate = $lastModified.ToString("dd/MM/yyyy HH:mm")
    
    return @"
# -*- coding: utf-8 -*-

"""
SAMPA 4U - Projeto simples de dados abertos sobre transporte público Metropolitano do Estado de São Paulo.

METADADOS:
__author__      = "Rafael Barbosa"
__copyright__   = "Desenvolvimento independente"
__license__     = "MIT"
__version__     = "1.1.4"
__maintainer__  = "https://github.com/Rafabs"
__modified__    = "$formattedDate"

DESCRITIVO:
    $description

ARQUITETURA:
    $relativePath
"""

"@
}

# Configurações
$descriptions = @{
    "main.py" = @"
Ponto de entrada principal do sistema SAMPA 4U - Aplicação Qt que consolida:
- Monitoramento em tempo real das linhas de metrô/trem de SP
- Visualização de mapas e rotas interativas
- Notícias atualizadas sobre transporte
- Pesquisas de origem-destino (OD)
- Qualidade do ar e condições climáticas
- Console de logs integrado
- Interface responsiva para múltiplos monitores
- Confirmação de encerramento de janela GUI
"@

    "linhas/*.py" = @"
Módulo de visualização das linhas de metrô/trem de São Paulo:
- Interface gráfica com Tkinter
- Exibe mapas interativos das estações
- Mostra conexões entre linhas
- Inclui informações em tempo real
- Design responsivo (1920x1080)
- Ícones personalizados para cada linha
- Código de cores padrão do metrô
- Indica estações em construção
"@

    "gtfs_*.py" = @"
Módulo de processamento de dados GTFS (General Transit Feed Specification):
- Implementa parser completo do formato GTFS
- Carrega e processa arquivos: routes.txt, trips.txt, stop_times.txt, stops.txt
- Calcula itinerários e conexões entre linhas
- Interface gráfica com Tkinter para consulta
- Visualização de mapas com Folium
- Integração com API Olho Vivo (tempo real)
- Exportação para CSV/Excel/JSON
- Algoritmo de roteamento (Dijkstra)
- Suporte a múltiplos encodings (UTF-8, Latin-1)
"@

    "pesquisa_*.py" = @"
Módulo de análise de demanda de passageiros do metrô:
- Visualização interativa de dados de origem-destino (OD)
- Interface gráfica com PyQt5 e matplotlib
- Gráficos dinâmicos com tooltips informativos
- Filtros por linha e estação
- Análise temporal (séries históricas)
- Tratamento robusto de dados faltantes
- Exportação de resultados
- Integração com dados GTFS
"@

    "config*.py" = @"
Módulo de configuração e variáveis de ambiente:
- Armazenamento seguro de credenciais de API
- URLs base de serviços externos
- Chaves de acesso para integrações
- Parâmetros globais do sistema
- Configurações de ambiente (dev/prod)
- Variáveis de conexão com bancos de dados
- Constantes compartilhadas entre módulos
"@

    "temperatura*.py" = @"
Módulo de monitoramento climático em tempo real:
- Integração com API OpenWeatherMap
- Consulta automática de temperatura atual
- Formatação de dados meteorológicos
- Tratamento robusto de erros e exceções
- Atualização periódica (10 minutos)
- Suporte a fuso horário local (America/Sao_Paulo)
- Exibição formatada (°C)
- Logs detalhados para diagnóstico
"@
}


$excludedFiles = @("__init__.py", "pycache.py")
$headerPattern = '(?sm)^# -\*- coding: utf-8 -\*-\s+"""[\s\S]*?^ARQUITETURA:.*?"""'

# Processar arquivos Python
Get-ChildItem -Path "." -Filter "*.py" -Recurse | Where-Object {
    $_.Name -notin $excludedFiles -and $_.Name -notmatch "^__pycache__"
} | ForEach-Object {
    try {
        $filePath = $_.FullName

        if (-not (Test-Path $filePath -PathType Leaf)) {
            Write-Host "[AVISO] Arquivo não encontrado ou sem permissão: $($_.Name)" -ForegroundColor Yellow
            return
        }

        $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
        $content = [System.IO.File]::ReadAllText($filePath, $utf8NoBom)

        $description = $null
        foreach ($pattern in $descriptions.Keys) {
            if ($_.Name -like $pattern) {
                $description = $descriptions[$pattern]
                break
            }
        }
        if (-not $description) {
            $description = "Módulo de funcionalidades específicas"
        }

        if ($content -match $headerPattern) {
            $currentHeader = $matches[0]
            $dataFormatada = $_.LastWriteTime.ToString("dd/MM/yyyy HH:mm")

            $newHeader = $currentHeader `
                -replace '(?m)(__modified__\s*=\s*")[^"\r\n]*"', "`${1}$dataFormatada`"" `
                -replace '(?s)(DESCRITIVO:\s*\n)(\s*).*?(?=\nARQUITETURA:)', "`$1$2$description"

            if ($newHeader -ne $currentHeader) {
                $newContent = $content.Replace($currentHeader, $newHeader)
                [System.IO.File]::WriteAllText($filePath, $newContent, $utf8NoBom)
                Write-Host "[ATUALIZADO] $($_.Name)" -ForegroundColor Green
            }
        }
        else {
            $header = Get-Header -filePath $_.FullName -description $description -lastModified $_.LastWriteTime

            $shebang = ""
            if ($content -match '^#!.*') {
                $shebang = $matches[0] + "`n`n"
                $content = $content.Substring($matches[0].Length).TrimStart()
            }

            $newContent = $shebang + $header + $content
            [System.IO.File]::WriteAllText($filePath, $newContent, $utf8NoBom)
            Write-Host "[NOVO CABEÇALHO] $($_.Name)" -ForegroundColor Cyan
        }
    }
    catch [System.UnauthorizedAccessException] {
        Write-Host "[ERRO] Acesso negado ao arquivo: $($_.Name)" -ForegroundColor Red
    }
    catch [System.IO.IOException] {
        Write-Host "[ERRO] Problema de E/S no arquivo: $($_.Name) - $($_.Exception.Message)" -ForegroundColor Red
    }
    catch {
        Write-Host "[ERRO INESPERADO] $($_.Name): $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "Stack Trace: $($_.ScriptStackTrace)" -ForegroundColor DarkGray
    }
}

Write-Host "`nProcesso concluído! Arquivos processados com segurança." -ForegroundColor Green