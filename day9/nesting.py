capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },

    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

dict_in_list = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]


def add_new_country(negara, total_kunjungan, kota):
    new_country = {}
    new_country["country"] = negara
    new_country["cities_visited"] = kota
    new_country["total_visits"] = total_kunjungan
    dict_in_list.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(dict_in_list)
