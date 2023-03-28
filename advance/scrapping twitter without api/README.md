## Scrapping Twitter without API

In this project, we will scrape Twitter with Python without API using the twint module, and we'll also analyze some relationships based on followings and mentions among a group of Twitter users.

One of the hot topics in data science is social media analytics. People love these analyzes and interest them because everyone knows this world. Most of our time is spent on Twitter, Instagram, Facebook, and some other social media apps. The use of social media analysis is mostly used in the tasks of relationship analysis. With not only scraping twitter with python, but we will also do some relationship analysis based on our scrapped data.

### Scraping Twitter with Python

Now, let’s start with our task. In this task of scraping twitter with python, we need to install a package known as twint, which can be easily installed by using the pip command in your terminal;

```py
pip install twint
```

After importing the necessary libraries, now we need to start by creating a user list consisting of Twitter accounts. We will analyze the relationships between the popular Twitter users that everyone knows to make our analysis more interesting.

### Scraping Twitter with Python and Analyzing Relationships

I write a function named `get_followings` which will send a request to the twint library with a username. This function will return a list of users that our input user follows.

The `for` loop below will create two variables, as sometimes we get index error when Twitter does not respond to our request. For such cases, I added an exception to the code to ignore those users.

After getting all of the lists, we can just calculate the most common values ​​in the `following_list` variable to get the most popular accounts among our users. To get the 10 most followed accounts, we use the Counter function of the collection library.

What if we want to see who’s following who in our user group? To study it, I wrote a `for` loop that checks if anyone among the users is in the following list of another person. As a result, it creates a list dictionary displaying the following states represented by True and False.

In the code, the resulting dictionary is transformed into a pandas dataframe for a more user-friendly visualization. The rows of the dataframe show the users who follow, while the columns show the users who are followed.

### Summary

I hope you liked this project on Scraping twitter using python without using an API.