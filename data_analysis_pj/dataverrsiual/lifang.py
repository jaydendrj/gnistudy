import matplotlib.pyplot as plt

n=5001
nlist=range(1,n)
x_values=[i for i in nlist]
y_values=[i**3 for i in nlist]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,edgecolors="none",s=0.1)
plt.title('sancifang',fontsize=20)
plt.xlabel('x',fontsize=14)
plt.ylabel('x**3',fontsize=14)
plt.tick_params(axis="both",labelsize=10)
plt.axis([0,n,0,n**3])

plt.show()
