## Create Font Art

The font that appears in the output of your Python program is the default font for your operating system. Changing the font of your output may not be possible without using an external library. This is where the **PyFiglet** library in Python can come in handy. So if you want to learn how to print your output in amazing fonts, this project is for you.

### Create Font Art using Python

The PyFiglet library in Python can be used to visualize the output of your Python program with an amazing font style. If you’ve never used this library before, you can easily install it using the pip command.


```ps1
pip install pyfiglet
```

Here I’m just going to print my name as an output in an amazing font art using Python.

### Output

```
 _____     _       __  __ 
|__  /   _| |     |  \/  |
  / / | | | |_____| |\/| |
 / /| |_| | |_____| |  | |
/____\__,_|_|     |_|  |_|


```

The above font is the default font style provided by the PyFiglet library in Python. If you want to change the font of the output, you can change it using the font parameter `pyfiglet.figlet_format(‘Zul-M’, **font** = ”font name”)`. You can find many font styles supported by this library [here](http://www.figlet.org/fontdb.cgi).

### Summary

