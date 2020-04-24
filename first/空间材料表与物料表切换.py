a =set( ["s1","s2","s3"])
b =set( ["s2","s3","s5"])
c =set(["s1","s2","s3","s4"])
A = {'a': a, 'b': b, 'c': c}
x=a|b|c
print(x)
for i in x:
    B={i:[]}
    for j in A:
        if i in A[j]:
             B[i].append(j)
    print(i, "=", B[i])