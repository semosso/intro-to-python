# The following is a LIST, one of Python's data structures; note the []
cliches = [
    "At the end of the day",
    "Having said that",
    "The fact of the matter is",
    "Be that ast it may",
    "The bottom line is",
    "If you will",
]
print(cliches[int(input("> "))]) # modificado do original para permitir input em vez de escolha fixa

# The following is a DICTIONARY (collection of unique KEYS and their associated VALUES), another type data structure
quotes = { # would it change if I used [] instead of {}? nope, error
    "Moe": "A wise guy, huh?", 
    "Larry": "Ow!",
    "Curly": "Nyuk nyuk!",
}
stooge = "Curly"
print(stooge, "says:", quotes[stooge]) # why does this print with a space between says: and the quote?