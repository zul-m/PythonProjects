from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today?"]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you "]
    ],
     [
        r"(.*) your name ?",
        ["My name is zul-m, but you can just call me robot and I'm a chatbot.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "I am great!"]
    ],
    [
        r"sorry (.*)",
        ["It's alright","It's OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great!",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there"]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse"]
        
    ],
    [
        r"(.*)created(.*)",
        ["Zulfikar Muhamad created me using Python's NLTK library ", "top secret ;)"]
    ],
    [
        r"(.*) (location|city) ?",
        ['Sofia, Bulgaria']
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain"]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health "]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Badminton"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]

# Default message at the start of the chat.
print("Hi, I'm zul-m and I like to chat.\nPlease type here to start a conversation. Type quit to leave.")

# Create chatbot.
chat = Chat(pairs, reflections)

# Start conversation.
chat.converse()