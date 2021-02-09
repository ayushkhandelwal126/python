# while True:
#      try:
#          x = int(input("Please enter a number: "))
#          break
#      except ValueError:
#          print("Oops!  That was no valid number.  Try again...")

# while True:
#     try:
#         a=10 * (1/0)
#         print("The value of a is ",a)
#         break
#     except ZeroDivisionError:
#         print("Your infinite")

# while True:
#     try:
#         # b= input("Enter a number")
#         # print(type(b))
#         a=10 * b
#         print("The value of a is ",a)
        
#     except NameError:
#         print("There is an erroooorrrrrrrrr")
#         break
# try:
#     print(x)
# except:
#     print("An exception occurred")
# try:
# print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")
# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
#   try:
#   print(x)
# except:
#   print("Something went wrong")
# finally: # must and should even if it executes try block and also exceot block must have to print finally block
#   print("The 'try except' is finished")

try:
  f = open("a2.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()