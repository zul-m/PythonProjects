import random

when = ['A few years ago', 'Yesterday', 'Last night', ' A long time ago', 'On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Mariam', 'Daniel', 'John', 'Gary']
residence = ['Barcelona', 'Malaysia', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'cafe', 'school', 'laundry']
happened = ['made a lot of friends', 'eats a burger', 'found a secret key', 'solved a mystery', 'wrote a book']

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened) + '.')