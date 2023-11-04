#The name of the rivers and the countries they are in
rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"
}
#Creating a message
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")
#We then print or code
print("\nRivers in the dictionary:")
for river in rivers.keys():
    print(river)

print("\nCountries in the dictionary:")
for country in rivers.values():
    print(country)
