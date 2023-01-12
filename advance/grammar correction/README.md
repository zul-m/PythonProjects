## Grammar Correction

Using correct grammar is very important in any language. The role that syntax plays in a programming language is what grammar plays in any language.

### How to use Python for Grammar Correction?

There are so many applications that help you to correct your grammatical mistakes while writing. Grammarly is one of the best examples of such applications. It can correct every error while writing and helps you to complete your articles, emails, or any piece of writing without any errors.

So can we use Python for the task of grammar correction? Yes, we can! The [Gingerit](https://gingerit.readthedocs.io/en/latest/) library in Python is an open-source library that contains all the features that Grammarly provides. You can easily install it by using the pip command.
```py
pip install gingerit
```

*There is an issue with Cloudflare antibot which is blocking request to the session. The option is to disable Cloudflare V1 and replacing line 16 to below line on gingerit.py*
```py
scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
```

### Grammar Correction using Python

By using the `gingerit` library in Python you can eliminate all the grammatical mistakes, fix your spellings and punctuation errors and at the end, it helps you to enhance your text.

In the code, I am first importing the `GingerIt` function from the gingerit library, then I am storing a sentence as user input in the variable ‘text’. Then I am initializing the `GingerIt()` function on the input text. This function returns a dictionary of the text and the result, so to print the final output, I have selected ‘result’ to show the corrected text.

### Output

```
Enter a sentence >> My name is Zulfikar Muhamad. I will went to university tomorrow.
My name is Zulfikar Muhamad. I will go to university tomorrow.
```

### Summary

So this is how we can use Python to correct grammatical mistakes from any piece of text. The `Gingerit` library in Python can be used to enhance your writing by correcting all the mistakes in a few lines of code.