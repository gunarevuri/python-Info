import Thread

def square(n):
	print("square is ", n**2)

def cube(n):
	print("cube is ", pow(n,3))

t1 = Thread(target = square, args=(3,))
t2 = Thread(target = cube, args = (4,))

def target():
	t1.start()
	t2.start()
	print("Hello")

target()
