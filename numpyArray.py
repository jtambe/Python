# standard python array
arr = [5,2.8,9,56,9.99]
print(arr)


import numpy as np

arr = np.array([5,2.8,9,56,9.99])
print(arr)

print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))

# this is important because in standard python list, one has to use append
# numpy library allows us to declare empty list and simply access memory using index
arr = np.empty(6)
arr[3] = 54
for i in range(len(arr)):
    print(arr[i])

print(arr[:2])


x = [0, 1, 6, 3, 9, 8, 2]
y = [1, 6, 3, 4, 2, 8, 3]
# this one requires, pip install matplotlib
import matplotlib.pyplot as plt
plt.plot(x,y,'ro')
plt.show()



