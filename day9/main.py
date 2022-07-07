programming_dictionary = {
    "Bug": "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's "
           "standard dummy text ever since the 1500s",
    "Function": "Lorem ipsum",
    "Loop": "The lorem ipsum kwkwkw"
}

# print(programming_dictionary)

# add new item into dictionary
programming_dictionary["While"] = "The loop using"
# print(programming_dictionary)

# declare empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# redifine value in dictionary
programming_dictionary["Bug"] = "okay"
# print(programming_dictionary)

# loop through dictionary
for key in programming_dictionary:
    # key only
    print(key)
    # the value
    print(programming_dictionary[key])

capitals = {
    "France": "Paris",
    "German": "Berlin",
}

# nest list in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "German": ["Berlin", "Hamburg", "Stuttgart"],
}

# nest dictionary in a dictionary
travel_log2 = {
    "France": {"city_visited": ["Paris", "Lille", "Dijon"], "total_visited": 12},
    "German": ["Berlin", "Hamburg", "Stuttgart"],
}

# nest dictionary in a list
travel_log3 = [
    {
        "country": "France",
        "city_visited": ["Paris", "Lille", "Dijon"],
        "total_visited": 12
    },
    {
        "country": "German",
        "city_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited": 5
    }
]
