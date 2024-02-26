const express = require('express'); // Importa o Express
const axios = require('axios'); // Importa o Axios para fazer requisições HTTP
const jsdom = require('jsdom'); // Importa o JSDOM para manipulação do DOM em Node.js
const cors = require('cors'); // Importa o pacote cors para lidar com requisições CORS
const fs = require('fs'); // Importa o módulo fs para manipulação de arquivos
const { JSDOM } = jsdom; // Extrai JSDOM da biblioteca jsdom

const app = express(); // Cria uma instância do Express

app.use(cors()); // Utiliza o middleware cors para permitir solicitações de origens diferentes

const logFileName = 'Área de Desenvolvimento\\server_logs.txt'; // Define o nome do arquivo de log

// Função para adicionar logs ao arquivo
function addToLog(logData) {
    fs.appendFile(logFileName, logData + '\n', (err) => {
        if (err) {
            console.error('Erro ao adicionar ao log:', err);
        }
    });
}

// Define rotas para obter o status de cada linha de transporte público
// Cada rota chama a função getLineStatus com o número da linha e a resposta (res) como parâmetros
app.get('/linha1-status', (req, res) => {
    getLineStatus(1, res);
});

app.get('/linha2-status', (req, res) => {
    getLineStatus(2, res);
});

app.get('/linha3-status', (req, res) => {
    getLineStatus(3, res);
});

app.get('/linha4-status', (req, res) => {
    getLineStatus(4, res);
});

app.get('/linha5-status', (req, res) => {
    getLineStatus(5, res);
});

app.get('/linha7-status', (req, res) => {
    getLineStatus(7, res);
});

app.get('/linha8-status', (req, res) => {
    getLineStatus(8, res);
});

app.get('/linha9-status', (req, res) => {
    getLineStatus(9, res);
});

app.get('/linha10-status', (req, res) => {
    getLineStatus(10, res);
});

app.get('/linha11-status', (req, res) => {
    getLineStatus(11, res);
});

app.get('/linha12-status', (req, res) => {
    getLineStatus(12, res);
});

app.get('/linha13-status', (req, res) => {
    getLineStatus(13, res);
});

app.get('/linha15-status', (req, res) => {
    getLineStatus(15, res);
});

// Função para obter o status de uma linha específica
function getLineStatus(lineNumber, res) {
    // Faz uma requisição GET para o site da ViaMobilidade
    axios.get('https://www.viamobilidade.com.br')
        .then(response => {
            // Cria uma instância do JSDOM para manipular o HTML retornado
            const dom = new JSDOM(response.data);
            // Seleciona o elemento que contém o status da linha especificada
            const statusElement = dom.window.document.querySelector(`.line-${lineNumber} .status`);
            // Obtém o texto do status
            const status = statusElement.textContent;
            // Seleciona o elemento que contém a mensagem relacionada à linha (se houver)
            const msgElement = dom.window.document.querySelector(`.line-${lineNumber} .msg p`);
            // Obtém o texto da mensagem (ou uma string vazia se não houver mensagem)
            const msg = msgElement ? msgElement.textContent : '';
            // Log das informações com data e hora
            const logData = `${new Date().toISOString()} - Linha ${lineNumber}: Status - ${status}, Mensagem - ${msg}`;
            console.log(logData); // Exibe no terminal
            addToLog(logData); // Adiciona ao arquivo de log
            // Retorna os dados como um objeto JSON
            res.json({ linha: lineNumber, status: status, msg: msg });
        })
        // Trata erros, se ocorrerem
        .catch(err => {
            const logData = `Erro ao obter status da Linha ${lineNumber}: ${err}`;
            console.error(logData);
            addToLog(logData);
            res.status(500).json({ error: err.toString() });
        });
}
// Define a porta na qual o servidor irá ouvir as requisições
app.listen(3000, () => console.log('Servidor funcionando normalmente na porta \x1b[33m3000\x1b[0m\nPressione Ctrl + C para sair'));