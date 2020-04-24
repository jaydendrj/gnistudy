# name=input('Please enter your name: ')
# print('hello '+name.title()+'.')
#
# prompt='If you tell us who you are,we can personalize the messages you see.'
# prompt+='\nWhat is your first name?'
# name=input(prompt)
# print('\nHello,'+name.title()+'!')

# age=input('How old are you?')
# print(age)
#
# number=input('Enter a number,and iI\'ll tell you if it\'s even or odd:')
# number=int(number)
# if number%2==0:
#     print("\nThe number "+str(number)+' is even.')
# else:
#     print('\nThe number'+str(number)+' is odd.')
#
# car=input('What kind of car do you want to rent： ')
# print('Let me see if I can find you a '+car)
#
# number=input('有几个人')
# if int(number)<=8:
#     print('有空桌')
# else:
#     print('没空桌')

# prompt="\nTell me something,and I'll repeat it back to you: "
# prompt+="\nEnter 'quit'to end the program."
# message=''
# while message!='quite':
#     message=input(prompt)
#     print(message)

# sandwich_orders=['sadf','asgf','asfd']
# finished_sansiches=[]
# while sandwich_orders:
#     a=sandwich_orders.pop()
#     print('我做了：'+a)
#     finished_sansiches.append(a)
# for d in finished_sansiches:
#      print(d)
sandwich_orders=['sadf','pastrami','asgf','pastrami','asfd','pastrami']
print('wuxiangyanxunniuroumaiwanle')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)