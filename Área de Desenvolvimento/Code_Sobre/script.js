// Busca o status da linha 1
fetch('http://localhost:3000/linha1-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 1
        let card = document.getElementById('linha01-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
     
// Busca o status da linha 2
fetch('http://localhost:3000/linha2-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 2
        let card = document.getElementById('linha02-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
     
// Busca o status da linha 3
fetch('http://localhost:3000/linha3-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 3
        let card = document.getElementById('linha03-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
     
// Busca o status da linha 4
fetch('http://localhost:3000/linha4-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 4
        let card = document.getElementById('linha04-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
     
// Busca o status da linha 5
fetch('http://localhost:3000/linha5-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 5
        let card = document.getElementById('linha05-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
     
// Busca o status da linha 7
fetch('http://localhost:3000/linha7-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 7
        let card = document.getElementById('linha07-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
     
// Busca o status da linha 8
fetch('http://localhost:3000/linha8-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 8
        let card = document.getElementById('linha08-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
     
// Busca o status da linha 9
fetch('http://localhost:3000/linha9-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 9
        let card = document.getElementById('linha09-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
     
// Busca o status da linha 10
fetch('http://localhost:3000/linha10-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 10
        let card = document.getElementById('linha10-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
     
// Busca o status da linha 11
fetch('http://localhost:3000/linha11-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 11
        let card = document.getElementById('linha11-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
     
// Busca o status da linha 12
fetch('http://localhost:3000/linha12-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 12
        let card = document.getElementById('linha12-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
     
// Busca o status da linha 13
fetch('http://localhost:3000/linha13-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 13
        let card = document.getElementById('linha13-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
     
// Busca o status da linha 15
fetch('http://localhost:3000/linha15-status')
    // Converte a resposta para JSON
    .then(response => response.json())
    // Manipula os dados retornados
    .then(data => {
        // Obtém o elemento HTML correspondente ao status da linha 15
        let card = document.getElementById('linha15-info');
        // Define o texto do elemento como o status retornado dos dados
        card.textContent = data.status;

        // Adiciona uma classe CSS com base no status para estilização visual
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

        // Adiciona um evento de mouseover para exibir uma mensagem de tooltip com mais informações
        card.addEventListener('mouseover', () => {
            card.setAttribute('title', data.msg); // Exibe a mensagem como um tooltip ao passar o mouse sobre a linha
        });

    })
    // Captura erros, caso ocorram
    .catch(err => console.log(err));
    