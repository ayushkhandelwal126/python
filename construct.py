class User: # base class
 def __init__(self, name,age, college):
     self.name = name   #properties
     self.age = age 
     self.college = college 

 def details(self): #method
     
     print("my name is " + self.name + "my age is " + self.age + "my college is "+ self.college)
# inheritance means acquiring the properties of the parent class to the child class.

class Student(User): #child class/ inherited class/ derived class

    def __init__(self, name,age, college):
        self.name = name
        self.age = age 
        self.college = college 

    
objectx = Student("Raj", "45", "nmims") # objects
objectx.details() #method overriding from child class to the parent class
