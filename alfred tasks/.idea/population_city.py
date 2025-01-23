def get_population():
    countries = {
        "USA": {"California": {"Los Angelos": 4000000, "San Francisco": 870000}},
        "Canada": {"Ontario": {"Toronto": 2930000, "Ottawa": 994837}},
    }

    country = input("Enter a country name: ")
    city = input("Enter a city name: ")
    print(countries)



print(get_population())
