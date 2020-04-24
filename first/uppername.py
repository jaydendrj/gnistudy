# def prod(L):
#     def fn(x,y):
#         return x*y
#     from functools import reduce
#     return reduce(fn,L)
# print(prod([1,3,45,5]))

# from functools import reduce
# digital={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':12}
# def str2float(s):
#     def fn(x):
#         return digital[x]
#     l=list(map(fn, s))
#     n=0
#     while n<len(l):
#         n=n+1
#         if l[n]==12:
#             break
#     a=l[:n]
#     b=l[n+1:]
#     b.reverse()
#     print(a,b)
#     def yn(x, y):
#         return 10 * x + y
#     def xn(x,y):
#         return x*0.1+y

from functools import reduce
digital={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':-1}
def str2float(s):
    def fn(x):
         return digital[x]
     nums=list(map(fn,s))
     point = 0
     def f(x,y):
        if y==-1:
            point=1
            return x
        if point==0:
            return x*10+y
        else:
            point = point *10
            return x+y/b
     return  reduce(f,nums)

    # return reduce(yn,a) + reduce(xn,b)/10

print(str2float('123.4562'))


