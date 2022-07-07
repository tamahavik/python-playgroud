travel_log = [
    {
        "country": "France",
        "city_visited": ["Paris", "Lille", "Dijon"],
        "total_visited": 12
    },
    {
        "country": "German",
        "city_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited": 5
    }
]


def add_new_country(country, visited, city):
    record = {}
    record["country"] = country
    record["city_visited"] = city
    record["total_visited"] = visited

    travel_log.append(record)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
