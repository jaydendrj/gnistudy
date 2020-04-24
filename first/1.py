# def _odd_inter():
#     n=1
#     while True:
#         n=n+2
#         yield n
# def f(n):
#     return lambda x:x%n>0
# def primes():
#     yield 2
#     it=_odd_inter()
#     while True:
#         n=next(it)
#         yield n
#         it=filter(f,it)
# for n in primes():
#     if n<100:
#         print(n)
#     else:
#         break

from functools import  reduce


def f(x, y):
    return 10 * x + y
def fn(x):
    l=[]
    while x>0:
        a=x%10
        x=x//10
        l.append(a)
    return  reduce(f,l)
def yn(x):
    return x==fn(x)

def cd():
    n=0
    # j=[]
    while True:
        n=n+1
        if fn(n)==n:
            yield n
        else:
            continue
        # n=n+1
# def cv():
#     it=cd()
#     while True:
#         n=next(it)
#         yield n
#         it=filter(yn,it)
for n in cd():
    if n <10001:
        print(n)
    else:
        break


# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     a=[]
#     for i in L:
#        a.i[1]
#     return a
# L2 = sorted(L, key=by_name)
# print(L2)
