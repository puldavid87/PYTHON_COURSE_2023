###############################
print("First fuction:")
def math_5 ():
    for i in range(11):
        print("5 *",i,'=',i*5)
math_5()

################################
print("Second fuction:")
def math_5_limit(limit):
    for i in range(limit+1):
        print("5 *",i,'=',i*5)

math_5_limit(2)    

#################################
print("Third fuction:")
def math_5_limit_return(limit):
    for i in range(limit+1):
        result =+ i*5
    return result
out = math_5_limit_return(5)
print(out)

################################
print("Fourth fuction:")
def math_5_default(limit=1):
    for i in range(limit+1):
        result =+ i*5
    return result
out = math_5_default()
print(out)

out = math_5_default(2)
print(out)

###############################
print("Fifth fuction A:")
def math_5_default(limit=1):
    if limit < 0:
        print("Error")
        return
    else:
        for i in range(limit+1):
            result =+ i*5
        return result
out = math_5_default(-2)
print(out)
print("Fifth fuction B:")
out = math_5_default(5)
print(out)

