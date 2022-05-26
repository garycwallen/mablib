# Defining the user inputs
adjective = input("Adjective: ")
verb = input("Verb: ")
famous_person = input("Famous Person: ")

# String concatenating to build the madlib using f string
# Ensuring the adjective and verb are formatted in lowercase
# Ensuring the person is formatted as a title for first and last name
mad_lib = f"This is so cool, I feel {adjective.lower()}. When I {verb.lower()}, I look like {famous_person.title()}."

# Printing the complete mab lib
print(mad_lib)