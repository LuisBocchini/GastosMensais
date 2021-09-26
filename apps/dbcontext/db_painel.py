import pyodbc 
from apps.dbcontext.db_base import server, database, username, password
   
def cadastrar_ano_db(numero, usuario_id):
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # Abrindo conexão com o banco
        cursor = conn.cursor()             
        # Rodando o comando SQL
        cursor.execute("""
        INSERT INTO ANOS (NUMERO, USUARIO_ID)
        VALUES (?,?)
        """, (numero, usuario_id))
        conn.commit()
    except AttributeError:
        return AttributeError
    return True

def pesquisa_ano_db(numero_ano, id_usuario):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query = """
       select *from dbo.anos a
       inner join dbo.USUARIOS u
       on a.USUARIO_ID = u.ID 
       where numero = ? and usuario_id = ?
    """
    try:
      cursor = conn.cursor()
      execute_query = cursor.execute(query, numero_ano, id_usuario)
      columns = [column[0] for column in execute_query.description]
      ano = []
      for row in execute_query.fetchall():
          ano.append(dict(zip(columns, row)))
      if len(ano) > 0:
          return False
      else:
          return True
    except AttributeError:
          return 'Erro retornar dados'
      
def pesquisa_ano_id_db(ano_id, id_usuario):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query = """
       select a.numero, a.id from dbo.anos a
       inner join dbo.USUARIOS u
       on a.USUARIO_ID = u.ID 
       where a.id = ? and usuario_id = ?
    """
    try:
      cursor = conn.cursor()
      execute_query = cursor.execute(query, ano_id, id_usuario)
      columns = [column[0] for column in execute_query.description]
      ano = []
      for row in execute_query.fetchall():
          ano.append(dict(zip(columns, row)))
      return ano
    except AttributeError:
          return 'Erro retornar dados'
      
def excluir_ano_db(ano_id, id_usuario):
    try:
        
        despesas = pesquisa_despesa_ano(ano_id, id_usuario)
        if despesas == False:
            return "Esse ano possui despesas cadastradas. Exclua as despesas para poder excluir o ano"
        
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # Abrindo conexão com o banco
        cursor = conn.cursor()  
        # Rodando o comando SQL
        cursor.execute("""
        DELETE anos
        WHERE id = ? and usuario_id = ?
        """, (ano_id, id_usuario))
        conn.commit()
    except AttributeError:
        return False
    return True


def pesquisa_despesa_ano(id_ano, id_usuario):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query = """
       select * from dbo.DESPESAS
       where ANO_ID = ? and USUARIO_ID = ?
    """
    try:
      cursor = conn.cursor()
      execute_query = cursor.execute(query, id_ano, id_usuario)
      columns = [column[0] for column in execute_query.description]
      despesas = []
      for row in execute_query.fetchall():
          despesas.append(dict(zip(columns, row)))
      if len(despesas) > 0:
          return False
      else:
          return True
    except AttributeError:
          return 'Erro retornar dados'
      
      
def atualizar_ano_db(numero, ano_id, id_usuario):
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # Abrindo conexão com o banco
        cursor = conn.cursor()                  
        # Rodando o comando SQL
        cursor.execute("""
        UPDATE ANOS 
        SET NUMERO = ?
        WHERE ID = ? AND USUARIO_ID = ?
        """, (numero,ano_id,id_usuario))
        conn.commit()
    except AttributeError:
        return "Erro ao cadastrar"
    return True
  
      
def pesquisa_mes(id):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query = """
        select m.id, m.nome from dbo.meses m
        where m.id = ?
    """
    try:
        cursor = conn.cursor()
        execute_query = cursor.execute(query, id)
        columns = [column[0] for column in execute_query.description]
        mes = []
        for row in execute_query.fetchall():
            mes.append(dict(zip(columns, row)))
        return mes
    except AttributeError:
            return 'Erro retornar dados'

  