def tr(n):
    if n==1:
        [1]
    elif n==2:
        [1,1]
    else:
        [1,tr(n-1)[i]+tr(n-1)[i+1] for i in range()]

    L = [s + 1 for s in range(n)]
    return L
print(tr(3))
# L=[s+1 for s in range(10)]
# print (L)
#     return L
# tr(3)
