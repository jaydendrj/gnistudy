import matplotlib.pyplot as plt

# plt.scatter(2,4,s=200)
# plt.title('Square Numbers',fontsize=20)
# plt.xlabel('x',fontsize=14)
# plt.ylabel('y',fontsize=14)
# plt.tick_params(axis='both',which='major',labelsize=10)
# plt.show()

n=100
x_values=[i for i in range(n)]
y_values=[i**2 for i in range(n)]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=12)
plt.title('Squarepoints',fontsize=20)
plt.xlabel('x',fontsize=14)
plt.ylabel('y',fontsize=14)
plt.tick_params(axis='both',labelsize=10)
plt.axis([0,n,0,n**2])
# plt.show()
plt.savefig('aquare.png')