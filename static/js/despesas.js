function CadastroDespesas(atualizar){
    let usuario_id = document.querySelector('h2').getAttribute('id_usuario')
    let nome_usuario = document.querySelector('h2').getAttribute('nome_usuario');
    let mes_id = document.querySelector('.nome_mes').getAttribute('id_mes');
    let ano_id = document.querySelector('.nome_mes').getAttribute('id_ano');
    let nome_mes = document.querySelector('.p_nome_mes').innerText;
    let url = "";

    //Se for uma nova despesa
    if(atualizar == false){
      url = window.location.origin + "/cadastro_despesas/" + usuario_id + "/" + mes_id + "/" + ano_id + "/" + nome_mes + "/" + nome_usuario + "/" + 0
    } else{
      let id_despesa = atualizar.closest("tr").id
      url = window.location.origin + "/cadastro_despesas/" + usuario_id + "/" + mes_id + "/" + ano_id + "/" + nome_mes + "/" + nome_usuario + "/" + id_despesa
    }
 
    fetch(
        window.location.href = url,
      )
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
     
        });
}

function AbrirModal(despesa){
   let id_despesa = despesa.closest('tr').id
   let modal = document.querySelector('.modal-container')
   modal.style.display = "flex";
   modal.setAttribute('id_despesa', id_despesa)
}

//Excluir despesa
document.getElementById('btnSim').addEventListener('click', function(){
  let modal = document.querySelector('.modal-container')
  modal.style.display = "none";
  //lógica para excluir
  let id_despesa = modal.getAttribute('id_despesa')
  let url = window.location.origin + "/excluir_despesa/" + id_despesa
  fetch(
     url,
  )
    .then(function (response) {
      console.log(response.body)
      return response.json();
    })
    .then(function (data) {
      //Se excluir a despesa corretamente, redireciona pro painel
       if(data == 1){
        RedirecionarDespesas()
       }else{
        alert("Erro ao excluir")
       }
    });
})

//Fechar modal
document.getElementById('btnNao').addEventListener('click', function(){
  let modal = document.querySelector('.modal-container')
  modal.style.display = "none";
})

function RedirecionarDespesas(){
    let usuario_id = document.querySelector('h2').getAttribute('id_usuario')
    let mes_id = document.querySelector('.nome_mes').getAttribute('id_mes')
    let ano_id = document.querySelector('.nome_mes').getAttribute('id_ano')
    let nome_mes = document.querySelector('.nome_mes').innerText;
    let url = window.location.origin + "/despesas/" + usuario_id + "/" + mes_id + "/" + ano_id + "/" + nome_mes
    window.location.href = url
}

