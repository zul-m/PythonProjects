def convert(s):
    f = float(s)
    c = (f - 32) * 5 / 9
    return c

print(convert(input("Enter temperature in fahrenheit: ")))