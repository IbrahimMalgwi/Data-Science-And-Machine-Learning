import matplotlib.pyplot as plt
from matplotlib import style

style.use('classic')

food = ['pizza', 'ice cream', 'burgers']
sales = [20, 15, 30]
color = ['red', 'blue', 'yellow']

plt.pie(sales,labels=food, colors=color)

plt.title('FOOD SALES CHART')

plt.show()