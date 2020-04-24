import matplotlib.pyplot as plt

min=-59
max=56
values=[i for i in range(min,max)]
squares=[i**2 for i in range(min,max)]
# squares = [1,3,9,16,25]
plt.plot(values,squares,linewidth=5)
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)
plt.tick_params(axis='both',labelsize=10)
plt.show()
