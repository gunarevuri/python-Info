from multiprocessing import Process


def showSquare(num=2):
	print(n ** 2)

proc = []
for i in range(5):
	proc.append(Process(target=showSquare,args=(i+1)))


def process():
	for p in proc:
		p.start()
	print("Helo")

process()