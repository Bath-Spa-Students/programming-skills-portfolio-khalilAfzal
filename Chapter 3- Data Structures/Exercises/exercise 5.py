guest_names=["Ilama Iqbal", "Mahatma Ghandi" , "Qaidai Azam Muhammad Ali Jinah"]
for guest_name in guest_names:
 print(f"Dear {guest_name} , I would like to invite you to a dinner with me where I would like to ask you some important questions today at 7pm at pera hotel New York.")
#just for a better view
guests_who_did_not_make_it="Ilama Iqbal"
print(f"\nUnfortunately, {guests_who_did_not_make_it} can't make it to dinner.")
#just for a better view
new_guest="Chahat Fateh Ali Khan"
guest_names[guest_names.index(guests_who_did_not_make_it)] = new_guest
for guest_name in guest_names:
 print(f"Dear {guest_name} , I would like to invite you to a dinner with me where I would like to ask you some important questions today at 7pm at pera hotel New York.")

