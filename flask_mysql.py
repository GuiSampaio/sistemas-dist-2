import mysql.connector
from flask import Flask
import json
from flask_jsonpify import jsonify

app = Flask(__name__) # __name__ variável do sistema que indica o nome do módulo ou 'main'

@app.route("/cliente/<nome>")
def imprime_cliente (nome=None):
    conn = mysql.connector.connect (host=' ', user=' ', passwd=' ', port=' ', database='chinook')
    cursor = conn.cursor()
    qstr = "select * from customers where FirstName=\'"+nome+"\'"
    print (qstr)
    query = cursor.execute(qstr)
    row_headers=[x[0] for x in cursor.description]
    print(row_headers)
    records = cursor.fetchall()
    print (records)
    result = [dict(zip(tuple (row_headers) ,i)) for i in records]
    print (result)
    jret = jsonify(result)
    print (jret)
    conn.close()
    return jret

@app.route("/clientes/")
def imprime_clientes():
   conn = conn = mysql.connector.connect (host=' ', user=' ', passwd=' ', port=' ', database='chinook')
   cursor = conn.cursor()
   qstr = "select * from customers"
   print (qstr)
   query = cursor.execute(qstr)
   row_headers=[x[0] for x in cursor.description]
   print(row_headers)
   records = cursor.fetchall()
   print(records)
   results = [dict(zip(tuple(row_headers), i)) for i in records]
   print (results)
   jret = jsonify(results)
   print(jret)
   conn.close()
   return jret

@app.route("/clientesbypais/<pais>")
def imprime_clientes_por_pais(pais=None):
   conn = conn = mysql.connector.connect (host=' ', user=' ', passwd=' ', port=' ', database='chinook')
   cursor = conn.cursor()
   qstr = "select * from customers where country = \'"+pais+"\' "
   print (qstr)
   query = cursor.execute(qstr)
   row_headers=[x[0] for x in cursor.description]
   print(row_headers)
   records = cursor.fetchall()
   print(records)
   results = [dict(zip(tuple(row_headers), i)) for i in records]
   print (results)
   jret = jsonify(results)
   print(jret)
   conn.close()
   return jret




app.run(host='0.0.0.0', port='80')
