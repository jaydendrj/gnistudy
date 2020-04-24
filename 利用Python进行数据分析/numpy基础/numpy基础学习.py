import numpy as np

# data1 = [6,7.5,8,0,1]
# arr1 = np.array(data1)
# print(arr1)
# print(arr1.shape)
#
# data2 = [[1,2,3,4,],[5,6,7,8]]
# arr2 = np.array(data2)
# arr2.shape
# print(arr2,arr2.shape,arr2.dtype)
#
# print(np.arange(15))
# np.zeros(10)

arr = np.empty((8,4))
for i in range(8):
    arr[i] = i
# print(arr)

arr[[2,4,5,]]=0
# print(arr)

arr = np.arange(16).reshape((2,2,4))
# print(arr.T,8)
# print(arr.transpose((2,1,0)))
# print(arr.swapaxes(0,1))
import random
arr =np.random.randn(7)*5
print(np.modf(arr))