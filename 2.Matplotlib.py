import matplotlib.pyplot as plt
import numpy as np

#print(plt.__version__)

xpoints = np.array([1, 80])
#xpoints = [1,2,3,4,5,6,7,8] ## does not work...
ypoints = np.array([3, 100])

print(xpoints)

plt.plot(xpoints, ypoints, marker = 'o')
plt.show()

##pie chart....
y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 