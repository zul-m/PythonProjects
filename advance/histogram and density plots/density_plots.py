import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = np.random.multivariate_normal([0,0], [[5, 2], [2, 2]], size = 2000)
data = pd.DataFrame(data, columns = ['x', 'y'])

sns.kdeplot(data["x"], fill = True)
sns.kdeplot(data["y"], fill = True)
plt.show()