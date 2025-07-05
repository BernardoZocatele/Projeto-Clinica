function paginaEstoque() {
    window.location.href = 'estoque.html';
}
// Função para consultar todo o estoque da empresa
function consultar_estoque() {
    const empresaId = userInfos.empresa_id;

    // Chama a função Python para obter todos os itens do estoque da empresa
    eel.consultar_estoque(empresaId, '')(function(result) {
        const estoqueLista = document.getElementById('estoque-lista');
        estoqueLista.innerHTML = '';  // Limpar resultados anteriores

        if(result.length > 0) {
            result.forEach(item => {
                const itemDiv = document.createElement('div');
                itemDiv.classList.add('item-estoque');  // Adicionando uma classe para estilo
                itemDiv.innerHTML = `
                    <p><strong>Nome:</strong> ${item[0]}</p>
                    <p><strong>Quantidade:</strong> ${item[1]}</p>
                    <p><strong>Empresa ID:</strong> ${item[2]}</p>
                    <hr>
                `;
                estoqueLista.appendChild(itemDiv);
            });
        } else {
            estoqueLista.innerHTML = 'Nenhum item encontrado.';
        }
    });
}
document.addEventListener('DOMContentLoaded', function () {
  const numeroWhatsApp = "5524993134184"; // <-- substituir pelo numero
  document.getElementById('whatsapp-btn').addEventListener('click', function () {
    const url = `https://wa.me/${numeroWhatsApp}`;
    window.open(url, '_blank');
  });
});
