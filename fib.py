print "enter max: "
MAX = raw_input(":")
MAX = int(MAX)

def fib(n):
	if n < 2:
		return 1	
	return n + fib(n-1) # is this correct math? would Fibonacci approve?

for j in range(0, MAX + 1):
	print "Fib: ", j, fib(j)
