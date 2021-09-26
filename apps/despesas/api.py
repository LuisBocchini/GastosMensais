from flask import Blueprint, request, jsonify, render_template
from apps.dbcontext.db_despesas import listar_despesas, listar_despesa_id, cadastrar_despesa_db, atualizar_despesa_db, excluir_despesa_db
from apps.dbcontext.db_usuarios import pesquisa_usuario_id
from apps.dbcontext.db_painel import  pesquisa_ano_id_db, pesquisa_mes

bp = Blueprint('despesas', __name__)

@bp.route('/despesas/<int:usuario_id>/<int:mes_id>/<int:ano_id>/<string:nome_mes>',methods=['GET'])
def despesas(usuario_id, mes_id, ano_id, nome_mes):
      despesas = listar_despesas(usuario_id, mes_id, ano_id)
      ano = pesquisa_ano_id_db(ano_id, usuario_id)
      numero_ano = ano[0]['numero']
      total = 0
      lst_usuario = pesquisa_usuario_id(usuario_id)
      usuario = lst_usuario[0]
      mes = pesquisa_mes(mes_id)
      nome_mes = mes[0]['nome']
      for despesa in despesas:
            total += despesa['VALOR']
      return render_template('despesas/despesas.html', despesas=despesas, nome_mes=nome_mes,mes_id=mes_id, total=total, usuario=usuario, ano_id=ano_id, numero_ano=numero_ano)


@bp.route('/cadastro_despesas/<int:usuario_id>/<int:mes_id>/<int:ano_id>/<string:nome_mes>/<string:nome_usuario>/<int:id_despesa>',methods=['GET'])
def cadastro_despesas(usuario_id, mes_id, ano_id, nome_mes, nome_usuario, id_despesa):
      despesa = ""
      ano = pesquisa_ano_id_db(ano_id, usuario_id) 
      lst_usuario = pesquisa_usuario_id(usuario_id)
      usuario = lst_usuario[0]         
      if id_despesa != 0:
         despesa = listar_despesa_id(id_despesa)  
      return render_template('despesas/cadastro_despesas.html', nome_mes=nome_mes, usuario=usuario, usuario_id=usuario_id, mes_id=mes_id, ano_id=ano_id, despesa=despesa, id_despesa=id_despesa, ano=ano[0]['numero'])


@bp.route('/cadastrar_despesa/<string:nome>/<int:valor>/<int:pago>/<int:usuario_id>/<int:mes_id>/<string:nome_mes>/<int:ano_id>',methods=['GET'])
def cadastrar_despesa(nome, valor, pago, usuario_id, mes_id, nome_mes, ano_id):
      cadastro = cadastrar_despesa_db(nome, valor, pago, usuario_id, mes_id, ano_id)
      if cadastro == True:
            return "Despesa cadastrada com sucesso"
      return "Falha ao cadastrar empresa"


@bp.route('/atualizar_despesa/<string:nome>/<int:valor>/<int:pago>/<int:usuario_id>/<int:mes_id>/<string:nome_mes>/<int:ano_id>/<int:id_despesa>',methods=['GET'])
def atualizar_despesa(nome, valor, pago, usuario_id, mes_id, nome_mes, ano_id, id_despesa):
      editar = atualizar_despesa_db(nome, valor, pago, usuario_id, mes_id, ano_id, id_despesa)
      if editar == True:
            return "Despesa atualizada com sucesso"
      return "Falha ao atualizar despesa"

@bp.route('/excluir_despesa/<int:id_despesa>',methods=['GET'])
def excluir_despesa(id_despesa):
      excluir = excluir_despesa_db(id_despesa)
      if excluir == True:
            return "1"
      return "0"


