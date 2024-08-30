# CREATE
myTuple = tuple([10,20,30])

# READ
print(myTuple)

for item in myTuple:
    print(f'item = {item}')

# Update - indirectly
myTuple=tuple([myTuple[0],200,myTuple[2]])
print(myTuple)

# DELETE
myTuple=tuple([myTuple[0],myTuple[1]])
print(myTuple)

