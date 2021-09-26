function AbrirMeses(elemento){
    // div ano mais próxima ao elemento clicado
    let acoes = elemento.closest('.acoes')
    let ano = acoes.closest('.ano')
    let numero_ano = parseInt(ano.innerText);
    // div meses referente ao ano
    let meses = document.getElementById(numero_ano)
    ano.style.marginBottom = "0px"
    //Lógica para abrir ou fechar o ano
    if(meses.classList.contains('show')){
        meses.classList.remove('show')
        ano.style.marginBottom = "30px"
    }else{
      meses.classList.add('show')
    }
}

function DespesasMes(elemento){
    let usuario_id = document.querySelector('.container').id
    let div_meses = elemento.closest('.meses')
    let ano_id = div_meses.getAttribute('ano_id')
    let mes = elemento.id;
    let nome_mes = elemento.innerText

    let url = window.location.origin + "/despesas/" + usuario_id + "/" + mes + "/" + ano_id + "/" + nome_mes
    fetch(
        window.location.href = url,
      )
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
     
        });
}

function CadastroAnosFormulario(id_ano){
  let id_usuario = document.querySelector('h2').getAttribute('id_usuario')
  let nome_usuario = document.querySelector('h2').getAttribute('nome_usuario')

  if(id_ano != 0){
    // div ano mais próxima ao elemento clicado
    let acoes = id_ano.closest('.acoes')
    let ano = acoes.closest('.ano')
    id_ano = ano.getAttribute("id")
  }


  let url = window.location.origin + "/cadastro_ano/" + id_usuario + "/" + nome_usuario + "/" + id_ano
    fetch(
        window.location.href = url,
      )
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
     
        });
}

function SalvarAno(){
  let numero_ano = document.querySelector('.placeholder-text').value 
  let id_usuario = document.querySelector('h2').getAttribute('id_usuario') 
  let ano_id = document.querySelector('input').getAttribute('id')
  let url = window.location.origin + "/salvar_ano/" + numero_ano + "/" + id_usuario + "/" + ano_id
  validacao_campos = ValidarCampos()
  if(validacao_campos.erro == true){
    return ModalErro(validacao_campos.mensagem)
  }

    fetch(
         url,
      )
        .then(function (response) {
         console.log(response.body)
         return response.json();
        })
        .then(function (data) {
          if(data == "OK"){
            RedirecionarPainel(id_usuario)
          }else{
            ModalErro(data)
          }
        });
}

function ModalErroExcluirAno(mensagem){
  let modal_container = document.querySelector('.modal-container')
  modal_container.style.display = "flex";
  document.querySelector('.mensagem').innerText = mensagem

  let modal = document.querySelector('.modal')
  modal.style.height = "135px"

  //Escondendo o botão Sim
  document.querySelector("#btnSim").style.display = "none";

  //Configurando  estilo do botão de fechar
  document.querySelector("#btnFechar").innerText = "Fechar";
  document.querySelector("#btnFechar").style.fontSize = "12px";
  document.querySelector("#btnFechar").style.width = "70px";
  document.querySelector("#btnFechar").style.float = "right";
  modal.style.color = "red";

}

function FecharModalPergunta(){
  let modal = document.querySelector('#modal-pergunta')
  modal.style.display = "none";
}

function AbrirModal(ano){
  let ano_id = ano.closest('.ano').id
  let modal = document.querySelector('#modal-pergunta')
  modal.style.display = "flex";
  modal.setAttribute('ano', ano_id)
}

//Excluir ano
function ExcluirAno(){
  let modal = document.querySelector('#modal-pergunta')
  modal.style.display = "none";
  //lógica para excluir
  let id_usuario = document.querySelector('h2').getAttribute('id_usuario')
  let ano_id = document.querySelector('#modal-pergunta').getAttribute('ano')
  let url = window.location.origin + "/excluir_ano/" + ano_id + "/" + id_usuario
  fetch(
     url,
  )
    .then(function (response) {
      console.log(response.body)
      return response.json();
    })
    .then(function (data) {
      //Se excluir a despesa corretamente, redireciona pro painel
       if(data == "OK"){
        RedirecionarPainel(id_usuario)
       }else{
         //Ajustando espaçamento do botão
         let button = document.querySelector('#btnFechar')
         button.style.marginTop = "-27px"
        ModalErro(data)
       }
    });

}
  
function ValidarCampos(){
    let numero_ano = document.querySelector('.placeholder-text').value 

    if(numero_ano == 0 || numero_ano == ""){
      response.erro = true
      response.mensagem = "Ano incorreto"
      return response
    } 
    response.erro = false 
    return response
} 



