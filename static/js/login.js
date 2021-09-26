function efetuar_login(){
    let email = document.querySelector('#email').value
    let senha = document.querySelector('#senha').value
    let url = window.location.origin + "/efetuar_login/" + email + '/' + senha
    fetch(
         url
   )
     .then(function (response) {
      return response.json();
     })
     .then(function (usuario) {
       if(usuario != "Usuário incorreto"){
        RedirecionarPainel(usuario.ID)
       }else{
         ModalErro(usuario)
       }
       
     });
}

function Cadastro(){
    let url = window.location.origin + "/salva_usuario/" + 0
    fetch(
      window.location.href = url
     )
     .then(function (response) {
       return response.json();
     })
}




