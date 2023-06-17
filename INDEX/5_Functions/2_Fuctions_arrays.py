def double_values(num):
    num *=2
n = 10
double_values(n)
print(n)    # Does not change

array = [10,20,30]
def double_array(numbers):
    for i, n in enumerate(numbers):
        numbers[i]*=2
double_array (array)
print(array) # it changes

array = [10,20,30]
double_array(array[:])
print(array) # Does not change