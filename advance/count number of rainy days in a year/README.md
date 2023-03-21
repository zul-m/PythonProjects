## Count Number of Rainy Days in a Year

Imagine you have a data series that represents the amount of precipitation each day for a year in a given city. For this task of numerical computing with python to count rainy days within a year, I start this off by loading the data, that you can download from here.

The table contains 365 values, giving the daily precipitation in inches from January 1 to December 31, 2014.

The histogram gives us a general idea of what the data looks like; despite its reputation, the vast majority of days in Seattle saw near the zero measured rainfall in 2014.

### Count Rainy Days with Numerical Computing

The focus of this project is about numerical computing with python to count rainy days within a year, so I focus more on solving this problem by numerical computing rather than machine learning algorithms.

If you don’t know to perform the task of numerical computing in python we can easily perform our tasks using the NumPy package in Python. So let’s perform some necessary NumPy functions for numerical computing with Python.

Using the numerical calculation functions using NumPy, we could begin to answer the types of questions we receive about our precipitation data.

### Output

```
             STATION                                STATION_NAME      DATE  PRCP  SNWD  SNOW  TMAX  ...  WDF5  WSF2  WSF5  WT01  WT05  WT02  WT03
0  GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20140101     0     0     0    72  ...   310    36    40 -9999 -9999 -9999 -9999
1  GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20140102    41     0     0   106  ...   200    94   116 -9999 -9999 -9999 -9999
2  GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20140103    15     0     0    89  ...    50    63    72     1 -9999 -9999 -9999
3  GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20140104     0     0     0    78  ...    40    45    58     1 -9999 -9999 -9999
4  GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20140105     0     0     0    83  ...    10    67    76 -9999 -9999 -9999 -9999

[5 rows x 17 columns]
(365,)
```

```
Number of days without rain: 215
Number of days with rain: 150
Number of days with rain more than 0.5 inches: 37
Number of days with rain < 0.2 inches: 75
```

### Summary

I hope you liked this project on how we can use the power of numerical computing in python to count the number of rainy days in Python.