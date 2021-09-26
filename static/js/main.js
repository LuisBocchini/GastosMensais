function RedirecionarPainel(id_usuario){
    let url = ""
    if(id_usuario == null){
        let usuario_id = document.querySelector('h2').getAttribute('id_usuario')
        url = window.location.origin + "/redirecionar_painel/" + usuario_id
    }else{
        url = window.location.origin + "/redirecionar_painel/" + id_usuario
    }  
    window.location.href = url
  }

function RedirecionarLogin(){
    window.location.href = window.location.origin + "/"
}

function validacaoEmail(field) {
    usuario = field.value.substring(0, field.value.indexOf("@"));
    dominio = field.value.substring(field.value.indexOf("@")+ 1, field.value.length);  
    if ((usuario.length >=1) &&
        (dominio.length >=3) &&
        (usuario.search("@")==-1) &&
        (dominio.search("@")==-1) &&
        (usuario.search(" ")==-1) &&
        (dominio.search(" ")==-1) &&
        (dominio.search(".")!=-1) &&
        (dominio.indexOf(".") >=1)&&
        (dominio.lastIndexOf(".") < dominio.length - 1)) {
        return true
    }
    else{
        response.erro = true
        response.mensagem = "Email inválido"
        return response
    }
}

var response = {
    erro: false,
    mensagem: ""
}