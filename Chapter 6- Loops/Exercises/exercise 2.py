while True:
    age_str = input("Please enter your age (or 'quit' to exit): ")
    if age_str.lower() == 'quit':
        break  
    # It exits the loop if the user enters 'quit'

    age = int(age_str)
    if age < 3:
        ticket_price = 0
    elif age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    print("The cost of your movie ticket is $", ticket_price)
print("Thank you for using our ticket service!")
