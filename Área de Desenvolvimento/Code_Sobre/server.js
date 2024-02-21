const express = require('express');
const axios = require('axios');
const jsdom = require('jsdom');
const cors = require('cors'); // Importando o pacote cors
const { JSDOM } = jsdom;

const app = express();

app.use(cors()); // Usando o middleware cors

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

function getLineStatus(lineNumber, res) {
    axios.get('https://www.viamobilidade.com.br')
        .then(response => {
            const dom = new JSDOM(response.data);
            const status = dom.window.document.querySelector(`.line-${lineNumber} .status`).textContent;
            res.json({ linha: lineNumber, status: status });
        })
        .catch(err => res.status(500).json({ error: err.toString() }));
}

app.listen(3000, () => console.log('Servidor funcionando normalmente na porta 3000'));
