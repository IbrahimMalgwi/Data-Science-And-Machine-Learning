import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data_base = sb.load_dataset('tips')
print(data_base)

sb.jointplot(x='tips', y='total_bill', data=data_base)
plt.show()