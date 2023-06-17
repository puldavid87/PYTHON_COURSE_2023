#check if the the variable n gets a float
try:
    n=float(input("number1: " ))
    m = 4
    print('Result: ',m/n)
except:
    print("Error")

#####
#while
while(True):
    try:
        n=float(input("number 1: " ))
        m = 4
        print('Result: ',m/n)
        break
    except:
        print("Error")


while(True):
    try: # code to evaluate
        n=float(input("number 1: " ))
        m = 4
        print('Result: ',m/n)
    except:
        print("Error")
    else: # rest of the code
        print('End')
        m = 4
        print('Result: ',m*n)
        break
    finally: # end of the code
        print ("Loop end")

