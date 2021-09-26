function SalvarDespesa(atualizar){
    let nome_despesa = document.querySelector('#nome').value 
    let valor_despesa = document.querySelector('#valor').value 
    let quitado = document.querySelector('#pago').value 
    let usuario_id = document.querySelector('h2').getAttribute("id_usuario")
    let mes_id = document.querySelector('.nome_mes').getAttribute('id_mes')
    let ano_id = document.querySelector('.nome_mes').getAttribute('id_ano')
    let nome_mes = document.querySelector('.p_nome_mes').innerText;
    let url = ""

    validacao_campos = ValidarCampos()
    if(validacao_campos.erro == true){
      return ModalErro(validacao_campos.mensagem)
    }

    if(atualizar == false){
       url = window.location.origin + "/cadastrar_despesa/" + nome_despesa + "/" + valor_despesa + "/" + quitado + "/" + usuario_id + "/" + mes_id + "/" + nome_mes + "/" + ano_id
    }else{
      var id_despesa = document.querySelector('#nome').getAttribute('id_despesa')
       url = window.location.origin + "/atualizar_despesa/" + nome_despesa + "/" + valor_despesa + "/" + quitado + "/" + usuario_id + "/" + mes_id + "/" + nome_mes + "/" + ano_id + "/" + id_despesa
    }

    fetch(
        url,
      )
        .then(function (response) {
          return RedirecionarDespesas()
        })
        .then(function (data) {
        });
}

function RedirecionarDespesas(){
    let usuario_id = document.querySelector('h2').getAttribute("id_usuario")
    let mes_id = document.querySelector('.nome_mes').getAttribute('id_mes')
    let ano_id = document.querySelector('.nome_mes').getAttribute('id_ano')
    let nome_mes = document.querySelector('.p_nome_mes').innerText;
    let url = window.location.origin + "/despesas/" + usuario_id + "/" + mes_id + "/" + ano_id + "/" + nome_mes
    window.location.href = url
}

function SomenteNumero(e){
  var tecla=(window.event)?event.keyCode:e.which;   
  if((tecla>47 && tecla<58)) return true;
  else{
    if (tecla==8 || tecla==0) return true;
  else  return false;
  }
}

function ValidarCampos(){
  let nome_despesa = document.querySelector('#nome').value 
  let valor_despesa = document.querySelector('#valor').value 

  if(nome_despesa == "" || valor_despesa == ""){
    response.erro = true
    response.mensagem = "Informe todos os campos..."
    return response
  }
  response.erro = false
  return response
}