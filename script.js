async function buscarFilme(){

    const name = document.querySelector(".search-input").value;

    if (!name) return;

    const ress = await fetch(`http://localhost:5000/filme?name=${name}`)
    const date = await ress.json();

    const result = document.getElementById("resultado");
    result.innerHTML = `
        <p>${date.titulo}</p>
        <p>${date.genero}</p>
        <img src="${date.Imagem}">
        <p>${date.avaliacao}</p>
    `;

}