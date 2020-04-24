# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('you can\' divide by zero.')

file_name='F:\学习\专业课\8毕设\开题报告\开题报告160301KTBG_保佳祺.doc'
file_name=""
try:
    with open(file_name)  as file_object:
        words=file_object.read()
except FileNotFoundError:
    msg="Sorry,the file "+file_name+' does not exist.'
    print(msg)