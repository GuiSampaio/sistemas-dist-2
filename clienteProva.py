
from socket import  *

s = socket ()

servidor=" "
porta=8792
s.connect((servidor, porta))

while ( sequencias != "" ):


    sequencias = input("Digite uma Sequencia de DNA: ")
    parSequencia = input("Digite o par da Sequencia: ")

    if (sequencias == ""):
        break
    print ("DNA SEQ 1 = "+ sequencias)
    sequencia = str.encode (sequencias, "UTF-8")
    s.send (sequencia)
    data = s.recv(8192)
    print (data.decode("utf-8"))

    if (parSequencia == ""):
        break
    print ("DNA SEQ 2 = " +parSequencia)
    par = str.encode (parSequencia, "UTF-8")

    s.send (par)
    data = s.recv(8192)
    print (data.decode("utf-8"))
    seqPar = "isPar"
    pares = str.encode (seqPar,"UTF-8")
    s.send(pares)



fim = "FIM"
bytes = str.encode (fim,"UTF-8")
s.send(bytes)
data = s.recv(8192)
print (data.decode("UTF-8"))

s.close ()

