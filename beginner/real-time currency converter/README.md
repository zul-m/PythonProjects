## Real-time Currency Converter

A currency converter is an application used to convert the value of one currency into another currency. In this project, I will take you through how to write a program to create a real-time currency converter with Python.

### How To Create a Real-time Currency Converter with Python?

To convert one currency to another, we need to write a program to accept user input where the user will enter the amount of money, and then the user has to choose the type of currency the user wants to check the value of.

Then our program should just display the result by calculating the converted amount as the output. A good currency converter application should show the converted amount in real-time, which will only be possible if our program is working on real-time conversion rates.

To use real-time exchange rates, we can use the forex-python library which is used as a free tool in Python to work with exchange rates and currency conversion.

### Features of Forex-Python Library

Some of the important features provided by this library are:
 1. List all exchange rates
 2. BitCoin price for all currencies
 3. Converting the amount into BitCoins
 4. Get historical rates for any day since 1999
 5. The conversion rate for a currency (ex; USD to INR)
 6. Convert the amount from one currency to another. (‘USD $ 10’ to INR)
 7. Currency symbols
 8. Names of currencies

It uses [ratesapi](https://ratesapi.io/) which is a free API to work with real-time and historical exchange rates published by the European Central Bank.

### Real-time Currency Converter with Python

To create a realtime currency converter with Python, we first need to install the forex-python library which can be easily installed by using the pip command; 

```py
pip install forex-python
```

### Output

```
Enter the amount: 56000
From Currency: usd
To Currency: myr
USD to MYR 56000
262724.17571471265
```

### Summary

I hope you liked this project on how to create a realtime currency converter with Python programing language.