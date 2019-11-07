from socket import *

s = socket ()

host = "ec2-107-22-11-255.compute-1.amazonaws.com"
porta = 8753
s.bind ((host, porta))
s.listen (10)

while True:
        (conn, cliente) = s.accept ()

        print ("Recebi a conexao de "+str(cliente))

        while True:
                data = conn.recv (4096)

                if not data:
                        break

                print (str(cliente)+" me mandou "+data.decode("utf-8") )

                conn.send (str.encode ("Eu sei que voce me mandou "+data.decode("utf-8") , "UTF-8"))

        print ("Fim da conexao com "+str(cliente))

        conn.close
