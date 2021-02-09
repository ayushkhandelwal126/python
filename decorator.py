
# example of decorator
def sampleDecorator(func):
   
    print("This is the added text to the actual function.")
   
    func()

    return 
# decorator is defined with @ symbol

@sampleDecorator
def actualFunction():
    print("This is the actual function.")


actualFunction()