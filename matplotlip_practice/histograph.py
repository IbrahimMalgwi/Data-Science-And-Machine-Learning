import matplotlib.pyplot as plt
from matplotlib import style

style.use('bmh')

numbers = [1, 20, 15, 23, 69, 18, 10, 23, 69, 87, 10,  23, 56, 4, 79, 52, 32, 14, 16, 96, 28, 23, 51, 48, 75, 96, 25, 96, 25, 63, 98, 74, 52, 14, 23, 69]
jumps = [0, 15, 30, 45, 60, 75, 90, 105]

plt.title('TEXT 1 HISTORIOGRAPHY')
plt.xlabel('text x label')
plt.ylabel('text y label')

plt.hist(numbers, jumps, histtype='bar')

plt.show()