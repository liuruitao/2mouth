def upper_attr(future_class_name,future_class_parents,future_class_attr):
	newAttr = {}
	for name,value in future_class_attr.items():
		if not name.startswith('__'):
			newAttr[name.upper()] = value
	return type(future_class_name,future_class_parents,newAttr)

class Foo(object,metaclass=upper_attr):
	bar = 'bip'
print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))

f = Foo()
print(f.BAR)
		
