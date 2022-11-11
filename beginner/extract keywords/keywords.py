import nltk
nltk.download('stopwords')

from rake_nltk import Rake
rake_nltk_var = Rake()

# Now let's store some text into a variable.
text = """RAKE short for Rapid Automatic Keyword Extraction algorithm, is a domain independent 
keyword extraction algorithm which tries to determine key phrases in a body of text by analyzing 
the frequency of word appearance and its co-occurance with other words in the text."""

# Now let’s extract the keywords from the text and print the output.
rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases()
print(keyword_extracted)