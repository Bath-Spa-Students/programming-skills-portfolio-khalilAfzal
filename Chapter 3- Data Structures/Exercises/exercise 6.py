guest_names = ["Ilama Iqbal", "Mahatma Gandhi", "Quaid-e-Azam Muhammad Ali Jinnah"]

# Initial invitations
for guest_name in guest_names:
    print(f"Dear {guest_name}, I would like to invite you to a dinner at 7 pm at Pera Hotel, New York to discuss some important matters.")

# Announcement about limited space
print("\nUnfortunately, our new dinner table won't arrive in time, and we can only invite two people for dinner.\n")

# Using pop() to remove guests and send them messages
while len(guest_names) > 2:
    removed_guest = guest_names.pop()
    print(f"Sorry, {removed_guest}, but we can't invite you to dinner this time.")

# Sending invitations to the two remaining guests
for guest_name in guest_names:
    print(f"Dear {guest_name}, you're still invited to dinner at 7 pm at Pera Hotel, New York to discuss some important matters.")

# Clearing the list using del
del guest_names[:]

# Printing the empty list
print("\nAfter clearing the list, it's now empty:", guest_names)
