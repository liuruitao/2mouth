def makeBold(fn):
	def wrapped():
		return '<b>' + fn() + '</b>'
	return wrapped

def makeItalic(fn):
	def wrapped():
		return 'i' + fn() + '</i>'
	return wrapped

@makeBold
def test1():
	return 'hello-1'
@makeItalic
def test2():
	return 'hello-2'
@makeBold
@makeItalic
def test3():
	return 'hello-3'
print(test1())
print(test2())
print(test3())
