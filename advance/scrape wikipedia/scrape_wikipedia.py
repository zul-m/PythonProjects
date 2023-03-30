# Importing the necessary package.
import wikipedia as wiki

# Get all the search suggestions of Python.
print(wiki.search("Python"))

# Suggestion if we type only some alphabets of its spelling.
print(wiki.suggest("Pyth"))

# Get the summary of Python article on Wikipedia.
print(wiki.summary("Python"))

# Get the summary in French language.
wiki.set_lang("fr")
print(wiki.summary("Python"))

# To get the title.
wiki.set_lang("en")
p = wiki.page("Python")

print(p.title)

# To get the url of the article.
print(p.url)

# To scrape the full article.
print(p.content)

# To get all the images in the article.
print(p.images)

# To get all the referals used by Wikipedia in the article.
print(p.links)