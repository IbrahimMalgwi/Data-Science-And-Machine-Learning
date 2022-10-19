import matplotlib.pyplot as plt
from matplotlib import style

style.use('classic')

x = [3, 6, 7, 9, 10]
y = [5, 10, 25, 3, 1]

plt.title('SCATTERED CHART')
plt.xlabel('text x')
plt.ylabel('text y')

plt.scatter(x, y)

plt.show()