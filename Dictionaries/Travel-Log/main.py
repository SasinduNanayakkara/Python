travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above


#to be added to the travel_log. 👇
def add_new_country(country_visited, times_visited, cities_visited):
  new_country = {} #initialize new dictionary
  new_country["country"] = country_visited # assign values to the dictionary
  new_country["times_visited"] = times_visited
  new_country["cities_visited"] = cities_visited

  travel_log.append(new_country) # assign the dictionary to a list




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"]) # call the function to add data
print(travel_log) # display the travel log



