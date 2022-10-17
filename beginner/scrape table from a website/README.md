## Scrape Table from a Website

[Web Scraping](https://thecleverprogrammer.com/2021/05/14/web-scraping-to-create-a-dataset-using-python/) is one of the skills that every data science professional should know. Sometimes the data we need is available on a website in the form of a table which cannot be downloaded directly from the website. To use that data for any data science task, we need to collect it from the website using web scraping techniques. So if you want to learn how to scrape a table from a website, this project is for you.

### Scrape Table from a Website using Python

There are many Python libraries and modules that you can use for web scraping. To scrape a table from a website, I will use the **urllib** module in Python, which is already available in the Python standard library. So you don’t need to install any external library to scrape data from a website.

In the code, I am collecting data from a table available on a [webpage](https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites) that contains a table describing the programming languages used in most popular companies. You can see the data we have received after web scraping is about the programming languages and databases being used by companies. So this is how you can scrape tables from any website using the Python programming language.

If you want to save this data in a CSV file, below is how you can save it:

```py
data.to_csv("programming.csv")
```

After running the above code, you will see the CSV file saved on the same directory where your Python file is.

### Output

```
    Websites Popularity(unique visitors per month)[1]  Front-end(Client-side)  \
0  Google[2]                               1600000000  JavaScript, TypeScript   
1   Facebook                               1120000000              JavaScript   
2    YouTube                               1100000000   JavaScript,TypeScript   
3      Yahoo                                750000000              JavaScript   
4       Etsy                          516,000,000[15]              JavaScript   

                               Back-end(Server-side)  \
0             C, C++, PHP, Go,[3] Java, Python, Node   
1  Hack, PHP (HHVM), Python, C++, Java, Erlang, D...   
2             C, C++, Python, PHP, Java, [11] Go[12]   
3                                                PHP   
4                                        PHP[16][17]   

                                     Database  \
0                     Bigtable,[4] MariaDB[5]   
1     MariaDB, MySQL,[9] HBase, Cassandra[10]   
2            Vitess, BigTable, MariaDB[5][13]   
3  PostgreSQL, HBase, Cassandra, MongoDB,[14]   
4                            MySQL, Redis[18]   

                                               Notes  
0           The most used search engine in the world  
1            The most visited social networking site  
2  The most popular video sharing site [YouTube i...  
3                                                NaN  
4                                E-commerce website.  
```

### Summary

So this is how we can scrape tables from a website using Python. Web Scraping is one of the skills that every data science professional should know.