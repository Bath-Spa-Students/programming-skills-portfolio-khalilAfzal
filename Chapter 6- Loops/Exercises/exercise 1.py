#creating a loop
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break  #It will exit the created loop if the user enters 'quit'
   
    print("I'll add", topping, "to your pizza.")
print("Your pizza is done!")
