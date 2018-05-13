def fib(times):
	i = 0
	a,b = 0,1
	while i<times:
		yield b
		a,b = b,a+b
		i+=1
F = fib(5)
print(next(F))
