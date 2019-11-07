from socket import *
from threading import Thread

def atende (conn, cliente):
        conn.settimeout(10.00)
        while True:
                try:
                    	data = conn.recv (4096)
                except:
                       	print ("Erro na conexão com o cliente "+str(cliente))
                        break

                if data == b'':
                        continue

                print (str(cliente)+" me mandou a estação"+data.decode("utf-8"))
               	estacoes = ["PRIMAVERA","VERÃO","OUTONO","INVERNO"]
                i = 0
                while i < len(estacoes):
                    estacao = data.decode("UTF-8")
                    if(estacao.isupper() == estacoes[i] or estacoes[i+1] != None):
                       print("Estacao: " + estacoes[i])
                       break
                    else:
                       print(estacoes[0])
                       break
                try:
                    	conn.send (str.encode ("Proxima Estação: " + "UTF-8"))
                except:
                       	break

        print ("Fim da conexao com "+str(cliente))
        conn.close

s = socket ()
host = "ec2-107-22-11-255.compute-1.amazonaws.com"
porta = 8765
s.bind ((host, porta))
s.listen (100)
nthr = 0

while True:
        (conn, cliente) = s.accept ()
        print ("Recebi a conexao de "+str(cliente))
        nthr += 1
        print ("Criando thread "+str(nthr))
        t = Thread(target=atende,args=(conn, cliente,))
        t.start()

