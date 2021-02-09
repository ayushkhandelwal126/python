def div(a,b):
    print(a/b)
div(4,2)
div(2,4)

def smart_div(func):
	def inner_func(a,b):
		if a<b:
			a,b = b,a
		return(a,b)
	return inner_func
	
div1 = smart_div(div)
div1(4,2)
div1(2,4)