def infitive_args (*args):
    for arg in args:
        print(arg)

array = (5,'hello',3.4,7)
infitive_args(array)

#Dictionaries
def infitive_args (**kwargs):
    for arg in kwargs:
        print(arg)
infitive_args(n = 5,c ='hello',f=3.4,p=7)