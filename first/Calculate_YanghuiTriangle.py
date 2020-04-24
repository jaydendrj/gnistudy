#
# def tr():
#
#
#     b=[1]
#     while True:
#         yield b
#         c=b[:]
#         c.append(0)
#         b.insert(0,0)
#         # print(c, b)
#         b=[c[i]+b[i] for i in range(len(b))]

# n=0
# r=[]
# for f in tr():
#     print (f)
#     r.append(f)
#     n=n+1
#     if n==10:
#        break
# n = 0
# results = []
# for t in tr():
#     print(t)
#     results.append(t)   #为什么？t是正常的，resulets.append(t)就多了一个0
#     n = n + 1
#     if n == 10:
#          break
# print(results)




# for t in results:
#     print(t)

# while True :
#     try:
#         print(next(tr(2)))
#     except StopIteration as e:
#         print(e.value)
#         break
#     if n==1:
#         [1]
#     elif n==2:
#         [1,1]
#     else:
#         [1,1].insert(a+b for a in tr(n-1) for b in tr(n-1))
# print(tr(4))

# from collections.abc import Iterable
# a=isinstance("23",Iterable)
# print(a)
# a=[1,3,5,6]
# b=iter(a)
# for i in range(3):
#     print(next(b))

# def f(x):
#     return x*x
#
# # L=[1,3,4,5]
# r=map(f,[2,3,4,5])
# print(list(map(str,[1,3,4,5,6])))
# from functools import reduce
# def add(x,y):
#     return x+y
# l=reduce(add,[22,34,532])
# print(l)
# def fn(x,y):
#     return x*10+y
# from functools import reduce
# print(reduce(fn,[1,2,4,5,]))
# from functools import  reduce
# def chr2int(s):
#     digits={"0":0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return digits[s]
# def fn(x,y):
#     return x*10+y
#
# l=map(chr2int,'123')
# print(reduce(fn,l))

def normalize(*name):
    digital={'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L','m':'M','n':'N','o':'O','p':'P','q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'}
    for i in name:
        if i==o:
            b=s[i].upper()
        else:
            b=
            name[0] = digital[name[o]]
    return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
# print(L2)
l={'i':'j' for i in 'afd' for j in 'dfdfg'}
print(l)