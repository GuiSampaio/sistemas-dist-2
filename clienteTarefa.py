from socket import  *

s = socket ()


servidor="ec2-52-206-96-112.compute-1.amazonaws.com"
porta=8732
s.connect((servidor, porta))

nomeArq = input("Digite o nome do arquivo!: ")

print (nomeArq)

mybyte = str.encode(nomeArq,"UTF-8")
s.send(mybyte)
arq = f.open(nomeArq, 'r')
while True:
	linhas = arq.readline()
	if(linhas == ''):
		break
	meusbytes=str.encode(linhas, "UTF-8")
	s.send (meusbytes)
	data = s.recv (8192)
	print (data.decode("utf-8"))

s.close ()

