def describe_city(city, country="Default Country"):
    print(f"{city} is in {country}.")

#S Calling the funtion by three cities
describe_city("Reykjavik", "Iceland")
describe_city("Tokyo", "Japan")
describe_city("New York")  #This one on this line will use a default country

