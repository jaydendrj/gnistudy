language='   python  '
message='1'+language.rstrip()+"1"
print(message)
message2='1'+language.lstrip()+'1'
print(message2)
message3='1'+language.strip()+'1'
print(message3)
print(language)  #剔除只是暂时的，language 还是原来的值
#'   python  '