from socket import *
from threading import Thread

def func(conn,cliente):
       data = conn.recv(8192)
       seq = data.decode("utf-8")
       dna = ''
       complemento  = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
      
       while True:
           if(seq != 'FIM'):
               str = ''
               for i in seq:
                      
            else:
                break

       conn.send(str.encode(str1, "utf-8"))

s= socket()
host= " "
porta = 8792
s.bind((host, porta))
s.listen(10)

nthr=0

while True:
       (conn, cliente) = s.accept()
       nthr +=1
       print("Conexao aberta")
       print("Thread "+str(nthr))
       t = Thread(target=func,args=(conn,cliente,))
       t.start()
