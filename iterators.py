# most commonly 3 words are used
# 1. iteration = porcess of making same process to run several times
# 2. iterable = python object which supports iteration
# 3. iterator = python object to perform iteration over an iterable

# iterable may be list,tuple , string
x = [1,2,3,4] 
x_iter = iter(x) # iterable function iter
print(next(x_iter)) # we can print each element in order until empty


# we can create our own iterable function

class yrange:
	# n is the number upto which i want the range
	def __init__(self, n):
		self.i = 0
		self.n = n
 	# this method makes our class iterable
	def __iter__(self):
		return self
	# this method should be implemented by the iterator
	def __next__(self):
		if self.i< self.n:
			i = self.i
			self.i += 1
			return i
		else:
			raise StopIteration()
			

