def palindrome(sentence):
    for i in (",.'?/><}{{}}'"):
        sentence = sentence.replace(i, "")

    palindrome = []

    words = sentence.split(' ')

    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
    return palindrome

# Now let’s input a sentence and use this algorithm.
sentence = input("Enter a sentence: ")

print(palindrome(sentence))