from flask import Blueprint, request, jsonify, render_template
from apps.dbcontext.db_painel import cadastrar_ano_db, pesquisa_ano_db, excluir_ano_db, pesquisa_ano_id_db, atualizar_ano_db
from apps.dbcontext.db_usuarios import pesquisa_usuario_id, listar_anos_usuarios

bp = Blueprint('painel', __name__)

@bp.route('/salvar_ano/<int:numero>/<int:id_usuario>/<int:ano_id>',methods=['GET'])
def salvar_ano(numero, id_usuario, ano_id): 
      # Se for editar um ano
      if ano_id > 0:
            atualizar_ano = atualizar_ano_db(numero, ano_id, id_usuario)
            if atualizar_ano == True:
                  return jsonify("OK")
      adicionar = False
      validandoAno = pesquisa_ano_db(numero, id_usuario)
      if validandoAno == True:
         adicionar = cadastrar_ano_db(numero, id_usuario)  
      if adicionar == True:
          return jsonify("OK")
      else:
          return jsonify("Esse ano já esta cadastrado em seu painel")
    
      
# Tela de cadastro 
@bp.route('/cadastro_ano/<int:usuario_id>/<string:nome_usuario>/<int:ano_id>',methods=['GET'])
def cadastro_ano(usuario_id, nome_usuario, ano_id):
      ano = 0
      lst_usuario = pesquisa_usuario_id(usuario_id)
      usuario = lst_usuario[0]
      if ano_id > 0:
         lst_ano = pesquisa_ano_id_db(ano_id, usuario_id)
         ano = lst_ano[0] 
      return render_template("painel/cadastro_ano.html", usuario=usuario, ano_id=ano_id, ano=ano)


@bp.route('/excluir_ano/<int:ano_id>/<int:id_usuario>',methods=['GET'])
def excluir_ano(ano_id, id_usuario):
      excluir = excluir_ano_db(ano_id, id_usuario)
      if excluir == True:
            return jsonify("OK")
      return jsonify(str(excluir))
  
  
@bp.route('/redirecionar_painel/<int:usuario_id>',  methods=['GET'])
def redirecionar_painel(usuario_id):
      # Valores digitados pelo usuário
      lst_usuario = pesquisa_usuario_id(usuario_id)
      usuario = lst_usuario[0]
      anos = listar_anos_usuarios(usuario['ID'])
      return render_template('painel/painel.html', usuario=usuario, anos=anos)