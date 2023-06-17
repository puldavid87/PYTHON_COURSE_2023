###########
#countdown

def countdown(num):
    num -=1
    if num > 0:
        print(num)
        countdown(num)
    else:
        print("Booom")

countdown(10)
   
def factorial (num):
    if num > 1 :
        num = num * factorial(num-1)
    return num 
print(factorial(5))
   