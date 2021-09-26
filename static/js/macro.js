function AbrirOpcoesUsuario(){
    let divOpcoesUsuario = document.querySelector(".opcoes_usuarios")
    if(divOpcoesUsuario.classList.contains('show2')){
        divOpcoesUsuario.classList.remove('show2')
    }else{
        divOpcoesUsuario.classList.add('show2')
    }
}

function EditarUsuario(){
    let usuario_id = document.querySelector('h2').getAttribute('id_usuario')
    let url = window.location.origin + "/salva_usuario/" + usuario_id
    fetch(
        window.location.href = url
      )
        .then(function (response) {
        //   return RedirecionarDespesas()
        })
        .then(function (data) {
        });
}

function ModalErro(mensagem){
    let modal_container = document.querySelector('.modal-container')
    modal_container.style.display = "flex";
    let p_mensagem = document.querySelector('.mensagem').innerText = mensagem
    document.querySelector('.mensagem').style.color = "red"
}

function ModalSucesso(mensagem){
    let modal_container = document.querySelector('.modal-container')
    modal_container.style.display = "flex";
    let p_mensagem = document.querySelector('.mensagem').innerText = mensagem
    document.querySelector('.mensagem').style.color = "#3F66CC"
}

function FecharModal(){
    let modal = document.querySelector('.modal-container')
    modal.style.display = "none";
}

  