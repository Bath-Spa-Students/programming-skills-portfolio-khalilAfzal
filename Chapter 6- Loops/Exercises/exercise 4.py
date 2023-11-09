#List of sandwiches
sandwich_orders = ['roast beef', 'turkey and cranberry', 'grilled cheese', 'BLT', 'egg salad']
finished_sandwiches = []
#Here we insert the loop
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)
#Then we print he list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

