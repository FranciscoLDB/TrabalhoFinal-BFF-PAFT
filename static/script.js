console.log('script works!');

function buscarGit(){
    console.log('Buscando git!');
    let usuario = document.getElementById('input_git').value;
    fetch('http://127.0.0.1:5000/github?usuario=' + usuario)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById('foto_git').setAttribute('src', data.foto);
            document.getElementById('nome_git').innerText = data.nome;
            document.getElementById('usuario_git').innerText = data.usuario;
            document.getElementById('bio_git').innerText = data.bio;
            document.getElementById('location_git').innerText = data.local;
        })
}

function buscarFilme(){
    console.log('Buscando filme!');
    let filme = document.getElementById('input_filme').value;
    fetch('http://127.0.0.1:5000/searchfilme?filme=' + filme)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById('foto_filme').setAttribute('src', data.foto);
            document.getElementById('nome_filme').innerText = data.titulo;
            document.getElementById('data_filme').innerText = data.data;
            document.getElementById('nota_filme').innerText = data.nota;
        })
}