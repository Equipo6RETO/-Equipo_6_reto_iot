import mysql.connector
import random

def insertar(param, valor, fecha, estado):
  try:
      cnx = mysql.connector.connect(user='root', password='3.14164510', host='127.0.0.1', database='oximetro')

      cursor = cnx.cursor()

      query_data = (valor, fecha, estado)

      if param == 1:
          query = f"INSERT INTO pulso(valor_pulso, fecha, estado) values(%s, %s, %s);"

      elif param == 2:
          query = f"INSERT INTO oxigenacion(valor_oxigenacion, fecha, estado) values(%s, %s, %s);"
 
      cursor.execute(query, query_data)
      cnx.commit()


  except mysql.connector.Error as err:

    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
      
  finally:
    if 'cnx' in locals() or 'cnx' in globals():
      cnx.close()

def insertarExp(idExpediente, valorPulso, valorOxigenacion, fecha):
  try:
      cnx = mysql.connector.connect(user='root', password='3.14164510', host='127.0.0.1', database='oximetro')

      cursor = cnx.cursor()

      query_data = (idExpediente, valorPulso, valorOxigenacion, fecha)

      query = f"INSERT INTO expediente(id_expediente, valor_pulso, valor_oxigenacion, fecha) values(%s, %s, %s, %s);"
      
      cursor.execute(query, query_data)

      cnx.commit()

  except mysql.connector.Error as err:

    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
      
  finally:
    if 'cnx' in locals() or 'cnx' in globals():
      cnx.close()

for i in range(1000):
  valor_Pul = random.randint(60, 120)
  valor_Ox = random.randint(70, 100)

  insertar(1, valor_Pul, "25/01/2020", True)
  insertar(2,valor_Ox,"25/01/2020",True)
  insertarExp(9012, valor_Pul, valor_Ox, "25/01/2020")





