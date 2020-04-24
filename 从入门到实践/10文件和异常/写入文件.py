filename='programming.txt'

with open(filename,'w') as file_objece:
    file_objece.write('I love programming.\n'*10)

with open(filename,'a') as file_objece:
    file_objece.write('asfjdjf')

with open(filename, 'r+') as file_objece:
    for i in file_objece.readlines():
        print(i.strip())