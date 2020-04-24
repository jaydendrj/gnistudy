names=['admin','d','c','y','ct']
for name in names:
    if names==[]:
        print('We need to find some users!')
    else:
        if name=='admin':
             print('Hello '+name+',would you like to see a status report?')
        else:
            print('Hello '+name+',thank you for logging in again')

current_users=['d','g','h','j','SD']
new_users=['sd','l','G','t','p']
current_users_lower=[i.lower() for i in current_users]

print(current_users_lower)
print(current_users)

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(new_user+'已经被占用，需重新输入别的用户名。')
    else:
        print(new_user+'未被使用')

nums=list(range(1,10))
for num in nums:
    if num ==1:
        print('1st')
    elif num==2:
        print('2nd')
    else:
        print(str(num)+'th')