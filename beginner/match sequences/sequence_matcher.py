from difflib import SequenceMatcher

text1 = "My name is Zulfikar Muhamad"
text2 = "Hi, my name is Zulfikar Muhamad"

sequenceScore = SequenceMatcher(None, text1, text2).ratio()

print(f"Both are {sequenceScore * 100}% similar")

# Now let’s try it with text inputs that are dissimilar from each other.
text3 = "My name is Zulfikar Muhamad"
text4 = "I am a Cloud Engineer"

sequenceScore = SequenceMatcher(None, text3, text4).ratio()

print(f"Both are {sequenceScore * 100}% simmilar")