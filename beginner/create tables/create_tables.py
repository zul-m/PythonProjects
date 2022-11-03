from tabulate import tabulate

data = [["Name", "Place", "Gender"],
       ["Alex", "Bulgaria", "Male"],
       ["Pauline", "Malaysia", "Female"],
       ["Zahid", "Malaysia", "Male"]]

print(tabulate(data, headers = 'firstrow', tablefmt = 'fancy_grid'))