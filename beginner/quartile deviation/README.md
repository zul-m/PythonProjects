## Quartile Deviation

Quartile deviation means the absolute measure of dispersion. It is the product of half the difference between the upper and lower quartiles (Quartile Deviation = (Q3 – Q1)/2).

### What is Quartile Deviation?

The quartile deviation is the absolute measure of dispersion, where dispersion is the extent to which the values of distribution differ from the mean value of the distribution. If only one very high or low value is present in the data it can still reduce the usefulness of the range as a measure of dispersion.

So, to calculate the quartile deviation, we need to divide the data into four parts where each part contains 25% of the values. Here, the product of half of the difference between the top (75%) and the bottom (25%) will give us the quartile deviation of the data.

### Quartile Deviation using Python

I hope you now have understood what is quartile deviation, you can learn more about it from [here](https://ncert.nic.in/textbook/pdf/kest106.pdf). Now let’s see how to calculate the quartile deviation of a dataset using Python. To calculate it by using Python programming language, I will first generate a dataset and then I will find the `quartile1`, `quartile2`, and `quartile3` from the data and then I will create a function that gives us the product of half the difference between `quartile3` and `quartile1`.

### Output

```
[20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
Quartile 1:  38.75
Quartile 2:  57.5 
Quartile 3:  76.25
18.75
```

### Summary

I hope you liked this project on how to calculate the quartile deviation of a dataset by using the Python programming language.