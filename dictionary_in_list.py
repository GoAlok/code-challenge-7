"""
    Introduction:
        Write a program that add to a travel_log. You can see a travels_log 
        which contains 2 Dictionaries.
        
        add_new_country("Russia", 2 , ["Moscow", "Saints Petersburg"] )
"""

travel_log = [
    {
        "country" : "France", 
        "cities_visited" : ["Paris", "Lille", "Dijon"], 
        "total_visits": 12 
    },
    {
        "country" :"Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 4 
    },
]


def add_new_country(country, cities_visited, total_visits):
    add_new_country = {}
    add_new_country["country"] = country
    add_new_country["cities_visited"] = cities_visited
    add_new_country["total_visits"] = total_visits
    travel_log.append(add_new_country)
add_new_country(country='Russia', cities_visited=["Moscow", "Saint Petersburg"], total_visits=6)
print(travel_log)