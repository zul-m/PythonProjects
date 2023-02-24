## Web Scrapper

In this project, I create a web scraper with Python that pulls all the stories from Google News by extracting all the tags from the HTML of Google News.

Google News uses tags to create links to the various websites that make up the site. So in addition to some additional data, you’ll collect all the URLs of the articles that Google News displays. I use the `BeautifulSoup` module to analyze the articles from Google News.

Parsing means taking a format like HTML and using a programming language to give it structure. For example, transforming data into an object. Now, to start this task of creating a web scraper with Python, you need to install a module named `BeautifulSoup`. It can be easily installed using the pip command;

```py
pip install beautifulsoup4
```

### Web Scraper with Python

Python has a built-in module, named `urllib`, for working with URLs.

The `__init__` method uses a website to extract as a parameter. Later you will pass “https://news.google.com/” as a parameter. The Scraper class has a method called scrape that you will call whenever you want to retrieve data from the site you passed.

The `urlopen()` function sends a request to a website and returns a Response object in which its HTML code is stored, along with additional data. The response of the function.read() returns the HTML of the Response object. All the HTML for the website is in the html variable.

The `BeautifulSoup` object does all the hard work and parses the HTML. You can now add code to the scrape function that calls the `find_all` method on the `BeautifulSoup` object.

The `find_all` method returns an iterable containing the tag objects found. Each time around the for loop, the variable receives the value of a new Tag object. Each Tag object has many different instance variables, but you just want the value of the href instance variable, which contains each URL.

You can get it by calling the get method and passing “href” as a parameter. Finally, you verify that the URL variable contains data; that it contains the string “articles” (you don’t want to print internal links); and if so, you print it.

### Output

```
./articles/CBMiemh0dHBzOi8vd3d3Lm1hbGF5bWFpbC5jb20vbmV3cy9tYWxheXNpYS8yMDIzLzAyLzI0L3BtLWFud2FyLXRhYmxlcy1ybTM4NmItYnVkZ2V0LTIwMjMtbW9zdC1kZXZlbG9wbWVudC1zcGVuZGluZy1ldmVyLzU2Mzg20gF-aHR0cHM6Ly93d3cubWFsYXltYWlsLmNvbS9hbXAvbmV3cy9tYWxheXNpYS8yMDIzLzAyLzI0L3BtLWFud2FyLXRhYmxlcy1ybTM4NmItYnVkZ2V0LTIwMjMtbW9zdC1kZXZlbG9wbWVudC1zcGVuZGluZy1ldmVyLzU2Mzg2?hl=en-MY&gl=MY&ceid=MY%3Aen

./articles/CBMiSmh0dHBzOi8vd3d3Lm5zdC5jb20ubXkvbmV3cy9uYXRpb24vMjAyMy8wMi84ODMwODkvbGl2ZS11cGRhdGVzLWJ1ZGdldC0yMDIz0gFOaHR0cHM6Ly93d3cubnN0LmNvbS5teS9hbXAvbmV3cy9uYXRpb24vMjAyMy8wMi84ODMwODkvbGl2ZS11cGRhdGVzLWJ1ZGdldC0yMDIz?hl=en-MY&gl=MY&ceid=MY%3Aen

./articles/CBMiV2h0dHBzOi8vd3d3LnRoZXN0YXIuY29tLm15L25ld3MvbmF0aW9uLzIwMjMvMDIvMjQvdGhlLW1hbGF5c2lhbi1idWRnZXQtLS1iaXRzLWFuZC1ieXRlc9IBAA?hl=en-MY&gl=MY&ceid=MY%3Aen

./articles/CBMiUmh0dHBzOi8vd3d3Lm5zdC5jb20ubXkvb3Bpbmlvbi9sZWFkZXJzLzIwMjMvMDIvODgyOTQzL25zdC1sZWFkZXItYnVkZ2V0YXJ5LWNvbmNlcm7SAVZodHRwczovL3d3dy5uc3QuY29tLm15L2FtcC9vcGluaW9uL2xlYWRlcnMvMjAyMy8wMi84ODI5NDMvbnN0LWxlYWRlci1idWRnZXRhcnktY29uY2Vybg?hl=en-MY&gl=MY&ceid=MY%3Aen

./articles/CBMid2h0dHBzOi8vd3d3Lm5zdC5jb20ubXkvbmV3cy9jcmltZS1jb3VydHMvMjAyMy8wMi84ODMwNTAvY2hpZWYtanVzdGljZS1tYWNjLXByb2JlLWFnYWluc3QtbmF6bGFuLW5vdC1hY2NvcmRpbmctcHJvdG9jb2xz0gF7aHR0cHM6Ly93d3cubnN0LmNvbS5teS9hbXAvbmV3cy9jcmltZS1jb3VydHMvMjAyMy8wMi84ODMwNTAvY2hpZWYtanVzdGljZS1tYWNjLXByb2JlLWFnYWluc3QtbmF6bGFuLW5vdC1hY2NvcmRpbmctcHJvdG9jb2xz?hl=en-MY&gl=MY&ceid=MY%3Aen

./articles/CBMiiQFodHRwczovL3d3dy5mcmVlbWFsYXlzaWF0b2RheS5jb20vY2F0ZWdvcnkvbmF0aW9uLzIwMjMvMDIvMjQvc3llZC1zYWRkaXEtZGlkbnQtb3JkZXItcm0xbWlsLXdpdGhkcmF3YWwtZnJvbS1iZXJzYXR1LWFjY291bnQtc2F5cy13aXRuZXNzL9IBAA?hl=en-MY&gl=MY&ceid=MY%3Aen

./articles/CBMiKGh0dHBzOi8vd3d3Lm1hbGF5c2lha2luaS5jb20vbmV3cy82NTYyOTnSAQA?hl=en-MY&gl=MY&ceid=MY%3Aen
```

### Summary

Now with this web scraper with Python, you can collect Google News headlines, the possibilities are endless. You can write a program to analyze the most used words in headlines. You can create a program to analyze stock sentiment and see if it correlates with the stock market.

With this web scraper with Python, all the information in the world is yours.