from flask import Flask, render_template
from apps.usuarios.api import bp as bp_login
from apps.usuarios.salvar_usuario import bp as bp_usuario
from apps.despesas.api import bp as bp_despesas
from apps.painel.api import bp as bp_painel

app = Flask('app')

@app.route('/')
def index():
  return render_template('login/login.html')

# login
app.register_blueprint(bp_login)
app.register_blueprint(bp_login, url_prefix='/json_home' )

# usuários
app.register_blueprint(bp_usuario)
app.register_blueprint(bp_usuario, url_prefix='/json_home' )

# despesas
app.register_blueprint(bp_despesas)
app.register_blueprint(bp_despesas, url_prefix='/json_home' )

# painel
app.register_blueprint(bp_painel)
app.register_blueprint(bp_painel, url_prefix='/json_home' )

if __name__== '__main__':
    app.run(host='localhost', port='8080', debug=True)
