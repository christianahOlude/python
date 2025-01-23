def update_countries():
    countries = {
        "USA": {"California": {"Los Angelos": 4000000, "San Francisco": 870000}},
        "Canada": {"Ontario": {"Toronto": 2930000, "Ottawa": 994837}},
    }
    countries.update({"Nigeria":{"lagos":{"mainland":4_200_329, "ikorodu":4_230_000}}})

    print(countries)
print(update_countries())