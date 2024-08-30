
myDict=dict()

#CREATE
myDict["Messi"]=10
myDict["Ronaldo"]=7
myDict["Neur"]=1

print(myDict)

# READ
n=myDict["Messi"]
print(n)

try:
    n=myDict["Maldini"]
    print(n)
except Exception as e:
    print('The key does not exist')


for key,value in myDict.items():
    print(f'key={key}')
    print(f'value={value}')

# UPDATE
myDict["Ronaldo"]=11
print(myDict)


# DELETE
n=myDict.pop("Ronaldo", -1)
print(n)

n=myDict.pop("Neimar", "Not Found")
print(n)

print(myDict)