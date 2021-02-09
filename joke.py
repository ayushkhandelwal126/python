import requests
print("welcome to the joke application")
x = input("Press S to know the joke")
JOKE = "http://api.icndb.com/jokes/random"
r = requests.get(url = JOKE)
details = r.json()

print (details["value"]["joke"])