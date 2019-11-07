from threading import Thread

cont = 0

def Contador(tid):
	global cont
	for i in range (10):
		cont += 1

threads = []
for i in range (5):
	print("Thread "+str(i))
	threads.append (Thread(target=Contador,args=(i,)))
	threads[-1].start()

for i in range(5):
	print("Aguardando "+str(i))
	threads[i].join ()

print (str(cont))
