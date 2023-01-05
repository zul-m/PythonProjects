# Import the CountVectorizer class from Scikit-learn library.
from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer()

# Store some texts into a Python list.
text = ["Hello there", "How are you", "I hope you are doing great", "My name is Zulfikar Muhamad"]

# Fit the list into the CountVectorizer function to convert the list of texts into numerical data.
vect.fit(text)

train = vect.transform(text)
train.toarray()

# Present it in the form of pandas DataFrame.
import pandas as pd

data = pd.DataFrame(train.toarray(), columns = vect.get_feature_names_out())
data