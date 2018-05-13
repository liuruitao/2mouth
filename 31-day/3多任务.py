def test1():
	while True:
		print('hehehehe')
		yield None

def test2():
	while True:
		print('hahaaha')
		yield None

t1 = test1()
t2 = test2()

while True:
	t1.__next__()
	t2.__next__()
