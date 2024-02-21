fetch('http://localhost:3000/linha1-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha01-info');
        card.textContent = data.status;

        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));

fetch('http://localhost:3000/linha2-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha02-info');
        card.textContent = data.status;

        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));        

fetch('http://localhost:3000/linha3-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha03-info');
        card.textContent = data.status;

        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));        

    fetch('http://localhost:3000/linha4-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha04-info');
        card.textContent = data.status;
        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));       
    fetch('http://localhost:3000/linha5-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha05-info');
        card.textContent = data.status;
        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));       
    fetch('http://localhost:3000/linha7-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha07-info');
        card.textContent = data.status;
        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));       
    fetch('http://localhost:3000/linha8-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha08-info');
        card.textContent = data.status;
        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));       
    fetch('http://localhost:3000/linha9-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha09-info');
        card.textContent = data.status;
        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));       
    fetch('http://localhost:3000/linha10-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha10-info');
        card.textContent = data.status;
        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));       
    fetch('http://localhost:3000/linha11-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha11-info');
        card.textContent = data.status;
        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));       
    fetch('http://localhost:3000/linha12-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha12-info');
        card.textContent = data.status;
        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));       
    fetch('http://localhost:3000/linha13-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha13-info');
        card.textContent = data.status;
        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));       
    fetch('http://localhost:3000/linha15-status')
    .then(response => response.json())
    .then(data => {
        let card = document.getElementById('linha15-info');
        card.textContent = data.status;
        // Adicionar a classe de status apropriada
        switch (data.status) {
            case 'Operação Normal':
                card.classList.add('verde_operacao_normal');
                break;
            case 'Circulação de Trens':
            case 'Operação Parcial':
            case 'Velocidade Reduzida':
                card.classList.add('amarelo_velocidade_reduzida');
                break;
            case 'Dados Indisponíveis':
                card.classList.add('branco_dados_indisponiveis');
                break;
            case 'Paralisada':
            case 'Operação Encerrada':
                card.classList.add('vermelho_paralisada');
                break;
        }
    })
    .catch(err => console.log(err));       