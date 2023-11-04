#This is our glossary
glossary = {
    "Variable": "A named storage location in memory to store data.",
    "Function": "A block of reusable code that performs a specific task.",
    "Loop": "A control structure that repeatedly executes a set of statements.",
    "List": "A collection of ordered and mutable elements, often used to store multiple values.",
    "Conditional Statement": "A decision-making structure that executes code based on a condition."
}
#Then we print he code 
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")

