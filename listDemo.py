myList=list()
print(myList)

# CREATE
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)
print(myList)

myList.insert(1,25)
print(myList)


#READ
n = myList[3]
print(n)

for i in myList:
    print(f'i={i}')

# Update
#myList[1:3]=[100,300,300]
myList[1]=250
print(myList)

# Delete
myList.remove(250)
print(myList)
myList.pop(2)
print(myList)




