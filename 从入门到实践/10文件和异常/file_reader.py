# with open('pi_digits.txt') as file_object:
#     contents=file_object.read()
#     print((contents.rstrip()))

# '''逐行读取'''
# filename='pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())


'''读取内容创建列表'''
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.strip())
pi_string=""
for line in lines:
    pi_string+=line.strip()
print(pi_string)