from socket import  *

s = socket ()


servidor=" "
porta=8765
s.connect((servidor, porta))

while True:
    minhastr = input("Digite uma estação: ")

    if (minhastr == ""):
        break
    print (minhastr)
    meusbytes=str.encode (minhastr, "UTF-8")
    s.send (meusbytes)
    data = s.recv (8192)
    print (data.decode("utf-8"))

s.close ()
