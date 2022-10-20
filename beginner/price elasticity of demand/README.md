## Price Elasticity of Demand

Price is one of the most important factors influencing the demand for a product. Elasticity refers to the degree of response, and the price elasticity of demand refers to the degree of responsiveness of demand for a product due to the change in its price. We study the price elasticity of demand in [economics](https://en.wikipedia.org/wiki/Economics), but if you want to learn how to calculate the price elasticity of demand using [Python](https://thecleverprogrammer.com/2021/06/19/fundamentals-of-python/), then this project is for you.

Price elasticity of demand refers to the degree of responsiveness of demand for a product to a change in price. Simply put, it means the degree to which the demand for a product changes with an increase or decrease in its price. For example, the demand for a product increases by 20% due to a 10% decrease in its price. This is what it means to change in demand with the change in the price of a product. And when you calculate the degree to which demand changes, it’s called the price elasticity of demand.

To calculate the price elasticity of demand, you have to use the formula mentioned below.

**Percentage Change in Quantity Demanded / Percentage Change in the Price**

### Price Elasticity of Demand using Python

I start the task of calculating price elasticity of demand using Python by creating a small dataset that should contain data about the change in the price and the demand for a product.

### Output

```
   Demand  Price
0      20   2000
1      30   1800
2      31   1850
3      33   1700
4      30   1800
5      33   1700
6      35   1600
```

The first rows of the dataset contain the **initial demand and price** for a product, and the subsequent rows contain the change in demand and the change in the price of the product. Now we add two more columns as the **Percentage change in Demand** and **Percentage change in Price** by calculating them.

```
   Demand  Price  % Change in Demand  % Change in Price
0      20   2000                 NaN                NaN
1      30   1800            0.500000          -0.100000
2      31   1850            0.033333           0.027778
3      33   1700            0.064516          -0.081081
4      30   1800           -0.090909           0.058824
5      33   1700            0.100000          -0.055556
6      35   1600            0.060606          -0.058824
```

Now the last step is to calculate the price elasticity of demand **(% Change in Demand / % Change in Price)** by adding a new column to the data.

```
   Demand  Price  % Change in Demand  % Change in Price  Price Elasticity
0      20   2000                 NaN                NaN               NaN
1      30   1800            0.500000          -0.100000         -5.000000
2      31   1850            0.033333           0.027778          1.200000
3      33   1700            0.064516          -0.081081         -0.795699
4      30   1800           -0.090909           0.058824         -1.545455
5      33   1700            0.100000          -0.055556         -1.800000
6      35   1600            0.060606          -0.058824         -1.030303
```

### Summary

Price elasticity of demand refers to the degree of responsiveness of demand for a product to a change in price. Simply put, it means the degree to which the demand for a product changes with an increase or decrease in its price.