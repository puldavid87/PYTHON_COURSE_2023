numbers = [1,2,3,4,5,6,7,8,9,10]

for i in numbers:
    print(i)

#update values
for index, i in  enumerate (numbers):
    numbers[index] *= 10
print(numbers)

text = "Hello Friends"
for cha in text:
    print(cha)

for cha,i in enumerate (text):
    if i == 'e':
        text=text.replace(text[cha],"*")
print(text)   



