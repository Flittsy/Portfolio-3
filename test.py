def normalize_country_name(country):
    country1 = country.strip().lower()
    country2 = country1.split()
    country3 = " ".join(country2)

    return country3
print(normalize_country_name("cote d'ivoire"))