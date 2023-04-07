## Get Real Time Weather

There are many ways to get real-time weather updates using Python. So many developers use API for this task, but as a newbie, you can’t afford to get API.

To get real-time weather conditions for any city using Python, I write Python code that takes the name of a city and returns the weather information for that city by scratching the web. So instead of using a paid API, we’ll be using web scraping for this task.

For this task, I use `Beautifulsoup` and the requests library in Python to extract the data directly from Google. The requests library comes preinstalled in the Python programming language, you can install the `Beautifulsoup` library by using a pip command;

```py
pip install beautifulsoup4
```

Remember that this library is imported by the name of bs4 in your Python code.

### Output

```
Enter the city name:
Sofia
Searching in google......

Weather
Friday 12:00 pm
Mostly cloudy  
8°C
```

### Summary

The time generated in the report may not be equals with the exact real-time but it will be somewhere around the live timings. This is how to get the live weather conditions of any place with Python programming language. You can use this logic for creating an advanced GUI application.