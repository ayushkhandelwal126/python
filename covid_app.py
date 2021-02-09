import requests
print('"Welcome covid Sate Wise Result Application"')
x = input("Enter The state name to know the result: ")
URL=" https://covid-india-cases.herokuapp.com/states/"
r = requests.get(url = URL)
data = r.json()
flag = 0
print(len(data))
# for i, count in enumerate(data): 
#         print(i, count)

for i in data:
    if(x.lower() == i['state'].lower()):
     flag = 1

if flag == 1:
        print("The NUmber if Active Cases are:" , i['active'])    
        print("The NUmber if Active Cases in ",x," are:" , i['noOfCases']) 
        print("The NUmber if Active Cases are:" , i['cured']) 
        print("The NUmber if Active Cases are:" , i['deaths']) 
else:
        print("The Given State name is wrong, pls enter the coreect state name")
        

 
    



