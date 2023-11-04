# A Python glossary (dictionary) with programming terms and their meanings
glossary = {
    "Variable": "A named storage location in memory to store data.",
    "Function": "A block of reusable code that performs a specific task.",
    "Loop": "A control structure that repeatedly executes a set of statements.",
    "List": "A collection of ordered and mutable elements, often used to store multiple values.",
    "Conditional Statement": "A decision-making structure that executes code based on a condition.",
    "Dictionary": "A collection of key-value pairs with unique keys.",
    "String": "A sequence of characters used to represent text.",
    "Boolean": "A data type that represents either True or False.",
    "Module": "A file containing Python code that can be used in other programs.",
    "Exception": "An error that occurs during the execution of a program."
}

# Print the glossary using a loop 
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
