elements = ["hi", 4, "bye", [1,2,3]]

list(enumerate(elements))
print(list)

for i in enumerate(elements):
    print(i)

for index, i in enumerate(elements):
    print(index,i)   
