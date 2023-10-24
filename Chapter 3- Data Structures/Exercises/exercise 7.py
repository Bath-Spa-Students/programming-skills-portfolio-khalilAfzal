# Define the list of places to visit
places_to_visit = ["Tokyo", "Paris", "Machu Picchu", "Santorini", "Kyoto"]

# Print the list in its original order
print("Original order:", places_to_visit)

# Use sorted() to print the list in alphabetical order without modifying the actual list
print("Alphabetical order:", sorted(places_to_visit))

# Verify that the original order is still intact
print("Original order:", places_to_visit)

# Use sorted() to print the list in reverse alphabetical order without changing the original list
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Verify that the original order is still intact
print("Original order:", places_to_visit)

# Use reverse() to change the order of the list
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

# Use reverse() again to restore the original order
places_to_visit.reverse()
print("Restored order:", places_to_visit)

# Use sort() to change the list to alphabetical order
places_to_visit.sort()
print("Alphabetical order (modified):", places_to_visit)

# Use sort() to change the list to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("Reverse alphabetical order (modified):", places_to_visit)
