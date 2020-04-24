information={'first_name':'c',"last_name":'m',"age":21,'city':'sh'}
print(information['first_name'])
print(information['last_name'])
print(information["age"])
print(information['city'])
favorite_numbers={
    'cm':2,
    'dy':4,
    'az':5,
    'jz':21,
    'ZX':45,
    }
for name in favorite_numbers:
    print(name+'最喜欢的数字是'
    +str(favorite_numbers[name]))

for name,num in favorite_numbers.items():
    print(name)
    print(num)
    print("\n")

jieshi={
    'python':'she',
    'grasshopper':'mazha',
    'rhino':'xiniu',
    'cad':'jisuanjifuzhusheji',
    'c':'biancheng'
    }
# for a,b in jieshi.items():
#     print(a,b)
jieshi['aflk']='asfjld'
jieshi['sagf']='asfhg'
for a,b in jieshi.items():
    print(a,b)