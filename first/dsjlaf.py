from functools import reduce
digital={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':-1}
# def str2float(s):
#     def fn(x):
#          return digital[x]
#      nums=list(map(fn,s))
#      point = 0
#      def f(x,y):
#         if y==-1:
#             point=1
#             return x
#         if point==0:
#             return x*10+y
#         else:
#             point = point *10
#             return x+y/b
#      return  reduce(f,nums)
#
#     # return reduce(yn,a) + reduce(xn,b)/10
#
# print(str2float('123.4562'))
# def str2float(s):
#     nums = map(lambda ch: digital[ch], s)
#     point = 0
#     def to_float(f, n):
#         nonlocal point
#         if n == -1:
#             point = 1
#             return f
#         if point == 0:
#             return f * 10 + n
#         else:
#             point = point * 10
#             return f + n / point
#     return reduce(to_float, nums, 0.0)
# print(str2float('123.4562'))
s=[3,4,5]
s.

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))