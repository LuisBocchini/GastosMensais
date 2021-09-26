from flask import Blueprint, request, jsonify, render_template
from apps.dbcontext.db_usuarios import verificar_usuario, listar_usuarios, listar_anos_usuarios, criar_usuario


bp = Blueprint('login', __name__)

@bp.route('/efetuar_login/<string:email>/<string:senha>',  methods=['GET'])
def efetuar_login(email, senha):
      lst_usuario = verificar_usuario(email, senha)
      if len(lst_usuario) > 0:
           return jsonify(lst_usuario[0])
      else:
            return jsonify("Usuário incorreto")
      # anos = listar_anos_usuarios(usuario['ID'])
      # return render_template('painel/painel.html', usuario=usuario, anos=anos)




