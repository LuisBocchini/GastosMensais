function SalvarUsuario(atualizar){
    let usuario_id = 0
    let url = ""
    let email = document.querySelector('#email').value 
    let nome = document.querySelector('#nome').value 
    //Editar
    if(atualizar == true){

        validarCampos = ValidarCampos(atualizar)
        if(validarCampos.erro == true){
            return ModalErro(validarCampos.mensagem)
        }

        let senhaAtual = document.querySelector("#senhaAtual").value
        let novaSenha = document.querySelector('#novaSenha').value
        usuario_id =  document.querySelector('h2').getAttribute("id_usuario")

        if(novaSenha == ""){
            novaSenha = 0
        }

        url = window.location.origin + "/salvar_usuario/" + nome + "/" + email + "/" + senhaAtual + "/" + novaSenha + "/" + usuario_id
    } else {
        validarCampos = ValidarCampos(atualizar)
        if(validarCampos.erro == true){
            return ModalErro(validarCampos.mensagem)
        }
        let senha = document.querySelector('#senha').value
        url = window.location.origin + "/salvar_usuario/" + nome + "/" + email + "/" + 0 + "/" + senha + "/" + 0   
    }
   
    fetch(
        url,
     )
       .then(function (response) {
        console.log(response.body)
        return response.json();
       })
       .then(function (data) {
        if(data == "Operação realizada com sucesso"){
            ModalSucesso(data)
        }
        else if(data == "Senha atual incorreta"){
            document.querySelector('#senhaAtual').style.border = "2px solid red"
            ModalErro(data)
        } else{
            ModalErro(data)
        }
        
       });
}

function ValidarCampos(atualizar){
    let form = document.querySelector('.itens_form')
    for(var i = 1; i <= 5; i++){
        form.children[i].style.removeProperty('border')
    }
    if(atualizar == true){
        let emailValue = document.querySelector('#email').value 
        let nome = document.querySelector('#nome').value 
        let senhaAtual = document.querySelector("#senhaAtual").value
        let inputEmail = document.querySelector('#email')
        //Nova senha
        let novaSenha = document.querySelector("#novaSenha").value
        let ConfirmeNovaSenha = document.querySelector("#ConfirmeNovaSenha").value

        if(emailValue == ""){
            document.querySelector('#email').style.border = "2px solid red"
        }
        if(nome == ""){
            document.querySelector('#nome').style.border = "2px solid red"
        }
        if(senhaAtual == ""){
            document.querySelector('#senhaAtual').style.border = "2px solid red"
        }

        //Validação de email
        let validarEmail = validacaoEmail(inputEmail)
        if(validarEmail.erro == true){
            return validarEmail
        }

        //Validação de senhas
        validarSenhas = ValidarSenhas(novaSenha, ConfirmeNovaSenha)
        if(validarSenhas.erro == true){
            document.querySelector('#novaSenha').style.border = "2px solid red"
            document.querySelector('#ConfirmeNovaSenha').style.border = "2px solid red"
            return validarSenhas
        }

        if(emailValue == "" || nome == "" || senhaAtual == ""){
            response.erro = true 
            response.mensagem = "Preencha todos os campos"
            return response
        }   

        return response

    } else {
        let email = document.querySelector('#email').value 
        let nome = document.querySelector('#nome').value 
        let senha = document.querySelector('#senha').value 
        let confirmeSenha = document.querySelector("#ConfirmeSenha").value
        let inputEmail = document.querySelector('#email')

        if(email == ""){
            document.querySelector('#email').style.border = "2px solid red"
        }
        if(nome == ""){
            document.querySelector('#nome').style.border = "2px solid red"
        }
        if(senha == ""){
            document.querySelector('#senha').style.border = "2px solid red"
        }
        if(confirmeSenha == ""){
            document.querySelector('#ConfirmeSenha').style.border = "2px solid red"
        }

        //Validação de email
        let validarEmail = validacaoEmail(inputEmail)
        if(validarEmail.erro == true){
            return validarEmail
        }

        //validação de senhas
        validarSenhas = ValidarSenhas(senha, confirmeSenha)
        if(validarSenhas.erro == true){
            document.querySelector('#senha').style.border = "2px solid red"
            document.querySelector('#ConfirmeSenha').style.border = "2px solid red"
            return validarSenhas
        }

        if(email == "" || nome == "" || senha == "" || confirmeSenha == ""){
            response.erro = true
            response.mensagem = "Preencha todos os campos"
            return response
        }  
        return response
    }
}

function ValidarSenhas(senha1, senha2){
        if(senha1 != senha2){
            response.erro = true 
            response.mensagem = "As senhas estão incorretas";
            return response
        }else{
            response.erro = false
            return response
        }
}



