import pyodbc 
import bcrypt
import sqlite3
from apps.dbcontext.db_base import server, database, username, password

def valida_senha(senha_digitada, hash_senha):
    return bcrypt.checkpw(senha_digitada, hash_senha) == hash_senha

def verificar_usuario(email, senha):
      senha = senha 
      conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
      query ="""
      SELECT * FROM USUARIOS WITH (NOLOCK) WHERE EMAIL = ?
      """
      try:
        cursor = conn.cursor()
        execute_query = cursor.execute(query,email)
        columns = [column[0] for column in execute_query.description]
        usuario = []
        for row in execute_query.fetchall():
            usuario.append(dict(zip(columns, row)))
                 
        validar_senha = False
        if senha != '' and len(usuario) > 0: 
            validar_senha = bcrypt.checkpw(senha.encode('utf-8'), usuario[0]['SENHA'].encode('utf-8'))
        
        if validar_senha == True:
              return usuario
        else:
              usuario = []
              return usuario
      except Exception as erro:
          return erro.__cause__
    
def listar_usuarios():
      conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
      query = """
          SELECT * FROM USUARIOS
      """
      try:
        cursor = conn.cursor()
        ret = cursor.execute(query)
        columns = [column[0] for column in ret.description]
        usuarios = []
        for row in ret.fetchall():
            usuarios.append(dict(zip(columns, row)))
        return usuarios

      except Exception as erro:
        return erro.__cause__
      
def listar_anos_usuarios(id_usuario):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query = """
        SELECT * FROM ANOS where USUARIO_ID = ?
    """
    try:
      cursor = conn.cursor()
      execute_query = cursor.execute(query, id_usuario)
      columns = [column[0] for column in execute_query.description]
      anos = []
      for row in execute_query.fetchall():
          anos.append(dict(zip(columns, row)))
      return anos
    except Exception as erro:
      return erro.__cause__
    
def pesquisa_usuario_id(id_usuario):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query = """
        SELECT ID, NOME, EMAIL FROM USUARIOS where ID = ?
    """
    try:
      cursor = conn.cursor()
      execute_query = cursor.execute(query, id_usuario)
      columns = [column[0] for column in execute_query.description]
      usuario = []
      for row in execute_query.fetchall():
          usuario.append(dict(zip(columns, row)))
      return usuario

    except AttributeError:
      return 'Erro retornar dados'
     
def criar_usuario(nome, email, senha):
    try:
      conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
      cursor = conn.cursor()
      nome = str(nome)
      email = str(email)
      senha = bcrypt.hashpw(str(senha).encode('utf-8'), bcrypt.gensalt())
      cursor.execute(
      """
      INSERT INTO USUARIOS (NOME, EMAIL, SENHA)
      VALUES(?,?,?)
      """, (nome,email,senha))
      conn.commit()
    except AttributeError:
        return False
    return True

def atualizar_usuario(nome, email, senha, usuario_id):
    try:
      conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
      cursor = conn.cursor()
      nome = str(nome)
      email = str(email)
      if senha != '0':
          senha = bcrypt.hashpw(str(senha).encode('utf-8'), bcrypt.gensalt())    
      if senha == '0':
            cursor.execute(
            """
            UPDATE USUARIOS 
            SET NOME = ?, EMAIL = ?
            WHERE id = ?
            """, (nome,email, usuario_id))
            conn.commit()
      else:
            cursor.execute(
            """
            UPDATE USUARIOS 
            SET NOME = ?, EMAIL = ?, SENHA = ?
            WHERE id = ?
            """, (nome,email,senha, usuario_id))
            conn.commit() 
    except AttributeError:
        return False
    return True
  
def verificar_senha(senha, usuario_id):
    senha = senha 
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query ="""
    SELECT * FROM USUARIOS  WHERE id = ?
    """
    try:
      cursor = conn.cursor()
      execute_query = cursor.execute(query, usuario_id)
      columns = [column[0] for column in execute_query.description]
      usuario = []
      for row in execute_query.fetchall():
          usuario.append(dict(zip(columns, row)))  
      validar_senha = False
      
      if len(usuario) > 0:          
         validar_senha = bcrypt.checkpw(senha.encode('utf-8'), usuario[0]['SENHA'].encode('utf-8'))   
          
      return validar_senha
    except Exception as erro:
      return erro.__cause__

def verificar_email(email):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query ="""
    SELECT * FROM USUARIOS  WHERE email = ?
    """
    try:
      cursor = conn.cursor()
      execute_query = cursor.execute(query, email)
      columns = [column[0] for column in execute_query.description]
      emails = []
      for row in execute_query.fetchall():
          emails.append(dict(zip(columns, row)))  
      return emails
    except Exception as erro:
      return erro.__cause__

  