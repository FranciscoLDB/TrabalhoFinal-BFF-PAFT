console.log('script works!');

function buscarGit(){
    console.log('Buscando git!');
    let usuario = document.getElementById('input_git').value;
    fetch('http://127.0.0.1:5000/github?usuario=' + usuario)
        .then(response => response.json()).then(data => console.log(data))
}