# x = int(input("enter a no."))
# if(x%2)== 0:
#     print("even")
# else:    
#     print("odd") 
# def o_e():
#     print("hello")

#  = lambda a,b:a**b
# print(f(2,3))


# div(4,2)

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