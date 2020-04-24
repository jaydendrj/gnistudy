# alien_color='red'
# if alien_color=='green':
#     print('玩家获得了5个点')
#
# alien_color='green'
# if alien_color=='green':
#     print('玩家获得了5个点')
#
# alien_color='red'
# if alien_color=='green':
#     print('玩家获得了5个点')
# else:
#     print('玩家获得了10个点')
#
# #3
# alien_color='red'
# if alien_color=='green':
#     print('5gedian')
# elif alien_color=='yellow':
#     print('10gedian')
# else:
#     print('15gedian')
#
# age=24
# if age<2:
#     print('他是婴儿')
# elif age<4:
#     print('他正蹒跚学步')
# elif age<13:
#     print("他是儿童")
# elif age<20:
#     print("他是青少年")
# elif age<65:
#     print("他是成年人")
# else:
#     print('他是老年人')
#
# fruit='banana'
# print(fruit)
# favorite_fruits=['banana','apple','pear']
# if fruit  in favorite_fruits:
#     print('You are really like '+fruit)



requested_toppings=[]#['mushrooms','green peppers','extra cheese']
out=['mushrooms','green peppers']
for requested_topping in requested_toppings:
    if requested_topping in out:
        print('Sorry,we are out of '+requested_topping)
    else:
        print('Adding '+requested_topping+'.')

        
# requested_toppings=[]
# out=['mushrooms']
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         if requested_topping in out:
#             print("Sorry we are out of "+requested_topping)
#         else:
#             print('Adding '+requested_topping+'.')
# else:
#     print('Are you sure you want a plain pizza?')
