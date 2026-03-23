async function buscarFilme(){

    const name = document.querySelector(".search-input").value;

    if (!name) return;

    const ress = await fetch(`http://localhost:5000/filme?name=${name}`)
    const date = await ress.json();

    const result = document.getElementById("resultado");
    result.innerHTML = date.map(filme => `
        <div class="filme-card">
            <img src="${filme.imagem}">
            <p class="filme-titulo">${filme.titulo}</p>
            <p class="filme-ano">${filme.ano}</p>
        </div>
    `).join("")

}