# Opening file
myfile = open('files/fruits.txt')
print(myfile.read())
content = myfile.read()

#Closing file
myfile.close()

print(content)
print(content)

myfile = open('files/fruits.txt')
content = myfile.read()
print(content[:10])

# function with string e pathfiles that returns number of occurencies of a character
def ocorrencias(param1, arquivo="files/fruits.txt"):
    file = open(arquivo)
    content = file.read()
    return content.count(param1)

print(ocorrencias('a'))


# opening with open, dont need closing file
with open('files/fruits.txt') as myfile:
    content = myfile.read()

print(content)

# Writing a text file
with open('files/vegetables.txt', 'w') as myfile:
    myfile.write('Tomato\nCucumber\nOnion')
    myfile.write('\nGarlic')

#Appendind Text to an existing file
# read an write the same time use 'a+'
with open('files/fruits.txt', 'a+') as myfile:
    myfile.write('\nOkra')
    myfile.seek(0)
    content = myfile.read()

print(content)