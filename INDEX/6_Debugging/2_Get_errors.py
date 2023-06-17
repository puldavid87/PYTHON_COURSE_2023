try: # code to evaluate
    n=float(input("number 1: " ))
    m = 4
    print('Result: ',m/n)
except Exception as error:
    print("Type of error:")
    print(type(error).__name__)

