document.addEventListener('DOMContentLoaded', function() {
    let copyButtons = document.querySelectorAll('.copy-code');

    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            let codeText = this.innerText.trim();
            navigator.clipboard.writeText(codeText).then(function() {
                alert('Código copiado para a área de transferência!');
            }, function() {
                alert('Erro ao copiar o código.');
            });
        });
    });
});