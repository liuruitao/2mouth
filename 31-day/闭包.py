def test(a):
	def test1(c):
		print(a+c)
	return test1
f = test(1)
f(6)

print('*'*50)

def line_conf(a,b,c):
	def line(x,y):
		return a*x+b*c+y
	return line
line1 = line_conf(1,1,2)
line2 = line_conf(4,5,3)
print(line1(5,2))
print(line2(5,2))
