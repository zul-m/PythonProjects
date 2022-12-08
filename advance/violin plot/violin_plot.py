import seaborn as sns
import matplotlib.pyplot as plt

Data = sns.load_dataset("tips")
plt.figure(figsize = (10, 8))
sns.violinplot(x = Data["total_bill"])

plt.show()

# Visualize multiple violin plots grouped based on the categorical features of the dataset.
plt.figure(figsize = (12, 10))
sns.violinplot(x = "day", y = "total_bill", data = Data)

plt.show()