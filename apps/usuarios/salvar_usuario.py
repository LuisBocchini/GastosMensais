from flask import Blueprint, request, jsonify, render_template
from apps.dbcontext.db_usuarios import valida_senha, verificar_senha, listar_usuarios, pesquisa_usuario_id, criar_usuario, atualizar_usuario, verificar_email


bp = Blueprint('cadastro_usuarios', __name__)

# Tela
@bp.route('/salva_usuario/<int:usuario_id>')
def salva_usuario(usuario_id):
      if usuario_id == 0:
            return render_template('usuarios/salvar_usuario.html', usuario_id=usuario_id)
      else:
            lst_usuario = pesquisa_usuario_id(usuario_id)
            usuario = lst_usuario[0]
            return render_template('usuarios/salvar_usuario.html', usuario=usuario, usuario_id=usuario_id)

# Cadastro no banco
@bp.route('/salvar_usuario/<string:nome>/<string:email>/<string:senha_atual>/<string:senha>/<int:usuario_id>',  methods=['GET'])
def salvar_usuario(nome, email,senha_atual,senha, usuario_id):
      usuarioSalvado = False
      if usuario_id == 0:
            verificacao_email = verificar_email(email)
            if len(verificacao_email) > 0:
                  return jsonify("Esse e-mail já existe")
            usuarioSalvado = criar_usuario(nome,email, senha)
      else:
            valida_senha_antiga = verificar_senha(senha_atual, usuario_id)
            if valida_senha_antiga == False:
                  return jsonify("Senha atual incorreta")
            usuarioSalvado = atualizar_usuario(nome, email, senha, usuario_id)     
      if usuarioSalvado == True:
            return jsonify("Operação realizada com sucesso")
      else:
            return jsonify("Ocorreu um erro")