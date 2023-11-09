sandwich_orders = ['roast beef', 'pastrami', 'turkey and cranberry', 'pastrami', 'grilled cheese', 'BLT', 'pastrami', 'egg salad']
finished_sandwiches = []
#We print a message that says that the pastrami sandwiches are no longer available
print("Sorry, the deli has run out of pastrami sandwiches.")

# remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
#the message that will be displayed when the order is ready
for order in sandwich_orders:
    print(f"We made your {order} sandwich.")
    finished_sandwiches.append(order)
#this will print the sanwiches that are already made
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
