word = "Python"
'''
+---+---+---+---+---+---+
|P  |y  |t  |h  |o  |  n|
+---+---+---+---+---+---+
|0  |1  |2  |3  |4  |5  | 
+---+---+---+---+---+---+
|0  |-5 |-4 |-3 |-2 |-1 |
+---+---+---+---+---+---+
'''
print(word[0])
print(word[-0])
print(word[5])
print(word[-1])
print(word[0:2])
print(word[2:-1])
print(word[2:])
word = "N"+ word[1:]
print(word)