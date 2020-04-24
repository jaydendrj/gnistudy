L=[i**3for i in range(1,9)]
print(L)
print('The first three items in the list are:'+str(L[:3]))
print('The items from the middle of the list are:'+str(L[1:4]))
print('The last three items in the list are:'+str(L[-3:]))
myself_L=L[:]
L.append(3)
myself_L.append(6)
print('The list of computer is:')
for l in L:
    print(l)
print('My list is：')
for lm in myself_L:
    print(lm)