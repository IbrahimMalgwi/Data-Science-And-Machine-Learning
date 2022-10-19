import matplotlib.pyplot as plt
from matplotlib import style

style.use('bmh')

x = [2, 4, 8]
y = [4, 8, 24]

x2 = [3, 6, 9]
y2 = [16, 15, 30]

plt.plot(x, y)
plt.plot(x2, y2)

plt.title('Test')
plt.xlabel('Text x values')
plt.ylabel('Text y values')

plt.show()