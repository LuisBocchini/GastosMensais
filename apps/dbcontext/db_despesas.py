import pyodbc 
from apps.dbcontext.db_base import server, database, username, password
    
def listar_despesas(id_usuario, mes_id, ano_id):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query = """
        SELECT D.ID, D.NOME, D.VALOR, D.PAGO, D.USUARIO_ID, D.MES_ID, D.ANO_ID, U.NOME NOME_USUARIO FROM DESPESAS D
        INNER JOIN DBO.USUARIOS U
         ON D.USUARIO_ID = U.ID
        where USUARIO_ID = ? AND MES_ID = ? AND ANO_ID = ?
    """
    try:
      cursor = conn.cursor()
      execute_query = cursor.execute(query, id_usuario, mes_id, ano_id)
      columns = [column[0] for column in execute_query.description]
      despesas = []
      for row in execute_query.fetchall():
          despesas.append(dict(zip(columns, row)))
      return despesas

    except AttributeError:
      return 'Erro retornar dados'
  
  
def listar_despesa_id(id_despesa):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query = """
        SELECT D.ID, D.NOME, D.VALOR, D.PAGO, D.USUARIO_ID, D.MES_ID, D.ANO_ID, U.NOME NOME_USUARIO FROM DESPESAS D
        INNER JOIN DBO.USUARIOS U
            ON D.USUARIO_ID = U.ID
        where D.ID = ?
    """
    try:
        cursor = conn.cursor()
        execute_query = cursor.execute(query, id_despesa)
        columns = [column[0] for column in execute_query.description]
        despesas = []
        for row in execute_query.fetchall():
            despesas.append(dict(zip(columns, row)))
        if len(despesas) != 0:
            return despesas[0]
        else:
            return despesas
    except AttributeError:
        return 'Erro retornar dados'
  
    
def cadastrar_despesa_db(nome, valor, pago, usuario_id, mes_id, ano_id):
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # Abrindo conexão com o banco
        cursor = conn.cursor()  
        # Parâmetros para o cadastro de despesa              
        nome_despesa = str(nome)
        valor_despesa = int(valor)
        pago_despesa = int(pago)
        id_usuario = int(usuario_id)
        mes = int(mes_id)
        ano = int(ano_id)
        # Rodando o comando SQL
        cursor.execute("""
        INSERT INTO DESPESAS (NOME, VALOR, PAGO, USUARIO_ID, MES_ID, ANO_ID)
        VALUES (?,?,?,?,?, ?)
        """, (nome_despesa, valor_despesa,pago_despesa,id_usuario, mes, ano))
        conn.commit()
    except AttributeError:
        return "Erro ao cadastrar"
    return True
  
def atualizar_despesa_db(nome, valor, pago, usuario_id, mes_id, ano_id, id_despesa):
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # Abrindo conexão com o banco
        cursor = conn.cursor()  
        # Parâmetros para o cadastro de despesa              
        nome_despesa = str(nome)
        valor_despesa = int(valor)
        pago_despesa = int(pago)
        # Rodando o comando SQL
        cursor.execute("""
        UPDATE DESPESAS 
        SET NOME = ?, VALOR = ?, PAGO = ?
        WHERE ID = ?
        """, (nome_despesa, valor_despesa,pago_despesa,id_despesa))
        conn.commit()
    except AttributeError:
        return "Erro ao cadastrar"
    return True


def excluir_despesa_db(id_despesa):
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # Abrindo conexão com o banco
        cursor = conn.cursor()  
        # Rodando o comando SQL
        cursor.execute("""
        DELETE DESPESAS 
        WHERE ID = ?
        """, (id_despesa))
        conn.commit()
    except AttributeError:
        return False
    return True
      
      

  