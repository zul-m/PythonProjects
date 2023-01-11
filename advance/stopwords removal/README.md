## Stopwords Removal

Stop words removal is an important step while working on any application of natural language processing. Stop Words are words that carry very little or no significant semantic context in a piece of text which is why such words need to be removed.

### What are Stop Words?

While working on natural language processing tasks where the output depends on the text we have trained the model on. When creating such applications, the text should be filtered by removing words with very little or no semantic context in the text to increase the accuracy of the model. These words are known as stop words.

Removing stop words is an important step while working on any application of natural language processing like chatbots, recommendation systems etc. If these words are not removed then it may affect the accuracy of the model. Almost all text processing applications remove stop words before processing the user input including applications like search engines also.

### Output

```
['Hi', ',', 'my', 'name', 'is', 'Zulfikar', 'Muhamad', '.', 'I', 'am', 'here', 'to', 'guide', 'you', 'to', 'your', 'journey', 'in', 'Machine', 'Learning', 'for', 'free', '.']
['Hi', ',', 'name', 'Zulfikar', 'Muhamad', '.', 'I', 'guide', 'journey', 'Machine', 'Learning', 'free', '.']
```

### Summary

Stop words are frequently used words in any language that are not considered very important when building natural language processing applications. These words include words such as conjunctions, prepositions, and adverbs.