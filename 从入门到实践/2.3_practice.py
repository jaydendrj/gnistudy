name='Eric'
message='Hello '+name+',would you like to learn some Python today?'

print(message)
print(name.lower())  #小写
print(name.upper())  #大写
print(name.title())  #首字母大写

print('Albert Einstein once said,"A person who never made a mistake never tried anything new."')
print("Albert Einstein once said,\"A person who never made a mistake never tried anything new.\"")

famous_person="Albert Einstein"
message=famous_person+' once said,\"A person who never made a mistake never tried anythign new.\"'
print(message)

name="\tjay\nden  "
print(name)
name1="1"+name.lstrip()+"1"
name2="1"+name.rstrip()+"1"
name3="1"+name.strip()+"1"
print(name1,)
print(name2)
print(name3)