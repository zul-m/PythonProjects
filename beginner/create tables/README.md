## Create Tables

Python is a very easy and versatile programming language. It offers libraries and modules for almost every task that you can think about. While working with data using python sometimes it becomes difficult to present it in a tabular format by using the standard formatting functions provided by Python.

### Tabulate Module in Python

The tabulate module in Python allows us to create and display data in a tabular format which makes the data look more readable. It can be used to organize your data to make it more understandable. Below are some of the data structures in Python which are supported by the tabulate module:
 1. Lists
 2. Dictionary
 3. NumPy Array
 4. Pandas DataFrame

The tabulate module doesn’t come preinstalled in the Python standard library so you can easily install it by using the pip command;

```
pip install tabulate
```

### Create Tables using Python

I hope you now have understood some of the important features provided by the tabulate module in Python. Now let’s see how to create tables using Python by using the tabulate module.

The code formats lists into a tabular format. We can separate the headers from the values.

```py
print(tabulate(data, headers = 'firstrow'))
```

We can also design this table by adding a grid, and make the grid look better.

```py
print(tabulate(data, headers = 'firstrow', tablefmt = 'grid'))
```

```py
print(tabulate(data, headers = 'firstrow', tablefmt = 'fancy_grid'))
```

### Output

```
-------  --------  ------
Name     Place     Gender
Alex     Bulgaria  Male  
Pauline  Malaysia  Female
Zahid    Malaysia  Male  
-------  --------  ------
```

```
Name     Place     Gender  
-------  --------  --------
Alex     Bulgaria  Male    
Pauline  Malaysia  Female  
Zahid    Malaysia  Male    
```

```
+---------+----------+----------+
| Name    | Place    | Gender   |
+=========+==========+==========+
| Alex    | Bulgaria | Male     |
+---------+----------+----------+
| Pauline | Malaysia | Female   |
+---------+----------+----------+
| Zahid   | Malaysia | Male     |
+---------+----------+----------+
```

```
╒═════════╤══════════╤══════════╕
│ Name    │ Place    │ Gender   │
╞═════════╪══════════╪══════════╡
│ Alex    │ Bulgaria │ Male     │
├─────────┼──────────┼──────────┤
│ Pauline │ Malaysia │ Female   │
├─────────┼──────────┼──────────┤
│ Zahid   │ Malaysia │ Male     │
╘═════════╧══════════╧══════════╛
```

### Summary

So this is how you can present your data in the form of tables. It is a good approach to format the data into tables as it makes the data look more readable.