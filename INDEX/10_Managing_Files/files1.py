from io import open

text = "A text file\n New line\n new line"
file = open('file.txt','w')# w-> write, r -> read
file.write(text)
file.close()
print('############################')
file1= open('C:/Users/LENOVO/Documents/PYTHON_COURSE_2023/file.txt','r')
text1 = file1.read()
file1.close()
print(text1)
print('############################')
file1= open('C:/Users/LENOVO/Documents/PYTHON_COURSE_2023/file.txt','r')
lines = file1.readlines()
file1.close()
print(lines)
print(lines[0])
print('############################')
lines.append('New line edited')
print(lines)
print('############################')
for i in lines:
    print(i)


print('############################')
with open ('file.txt','r') as file:
    for i in file:
        print(i)

# del (file) - > delete


