from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)

    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    
    return dfdict.values()

# Now let's test the function by creating a list of word containing anagrams and some other words.
words = ["tea", "eat", "bat", "ate", "arc", "car"]

print(group_anagrams(words))