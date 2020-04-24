# def person(name,age,**kw):
#     if 'city' in kw:
#         print('error')
#     print("name:",name,'age:',age,'other:',kw)
# f={'city':12,"d":4}
# print(f)
# a=person('dai',13,**f)
# print(a)

# def f1(a,b,c=0,*args,**kw):
#     print(a,b,c,args,kw)
# s=(1,3,3,4,5)
# f1(*s)
# def product(*s):
#     b=1
#     for i in s:
#         b=b*i
#     return b
# s=[1,3.4,3]
# print(product(*s))
#汉诺塔
# def move(n,a,b,c):
#       if n==1:
#         print(a,"-->",c)
#
#       else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
#
#
# move(3,"A","B","C")

def trim(s):
    if len(s)==0:
        s=''
    else:
        while s[0]==" ":
            s=s[1:]
        while s[-1]==' ':
            s=s[:-2]
    return s


if trim('hello  ') != 'hello':
    print('测试失败!1')
elif trim('  hello') != 'hello':
    print('测试失败!2')
elif trim('  hello  ') != 'hello':
    print('测试失败!3')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!4')
elif trim('') != '':
    print('测试失败!5')
elif trim('    ') != '':
    print('测试失败!6')
else:
    print('测试成功!')

# for x,y in enumerate(['a','b']):
#    print(x,y)

# def findMinAndMax(L):
#     if len(L)==0:
#         return (None, None)
#     else:
#      m=L[0]
#      n=L[0]
#      for i in L:
#         if i>m:
#             m=i
#         if i<n:
#             n=i
#      return (n,m)
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

# [m n for m in 'abc'for n in "123"]
#print ([m+n for m in 'abc'for n in "sdf"])
# def tr(s):
#     if s==1:
#         tr=[1]
#     elif s==2:
#         tr=[1,1]
#     else:
#         tr(s)=[1,i for i in tr(s-1),1]
#     return tr(s)
# tr(3)
# def tr(n):
#     if n==1:
#         L=[1]
#     elif
#      L=[s for s in range(0,n)]
#      return L
# print(tr(90))
# a=[1,4,5]
# b=[3,4,5]
# a.append(0)
# b.insert(0,0)
# print(a,b)
# print([A+B for A in a for B in b ])

