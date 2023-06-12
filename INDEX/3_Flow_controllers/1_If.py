if True:
    print("True")

a = 5
b = 10
if a == 5:
    print("a: ",a)
    if b == 10:
        print("b :", b)

if a == 5 and b == 10:
    print ('a: ',a, " and b :", b)

n =  10
if n%2 == 0 :
    print('pair')
else:
    print("odd")   

n =  9
if n%2 == 0 :
    print('pair')
elif n%3==0:
    print("multiple of 3") 
elif n % 5 ==0 :
    print("multiple of 5")
else:
    print("Nan")   