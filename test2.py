pip install numpy
import numpy  as np
from test import normalize_country_name
from portfolio_3 import read_csv
def summarize_country(country, country_data, population_data, species_data):
    country_row = isolate_country_row(country, country_data)
    population_row = isolate_population_row(country, population_data)
    species_row = isolate_threatened_species_row(country, species_data)
    
    population_values = np.array(population_row[1:])
    species_values = np.array(species_row[1:])
    avg_population = np.mean(population_values)
    max_population = np.max(population_values)
    min_population = np.min(population_values)
    area = country_row[2]
    population_density = avg_population / area
    species_density = np.mean(species_values) / area * 1000
    print(f"Summary for {country}:")
    print(f"Average Population: {avg_population}")
    print(f"Maximum Population: {max_population}")
    print(f"Minimum Population: {min_population}")
    print(f"Population Density: {population_density}")
    print(f"Species Density (per 1000 km²): {species_density}")

    #calculate averages, minimums, maximums, density, growth, etc.
    #Easily knocks out requirements
    return None

def isolate_country_row(country, data):
    isolated_row_country = normalize_country_name(country)
    for row in data:
        if normalize_country_name(row[0]) == isolated_row_country:
            return row

def isolate_threatened_species_row(country, species_data):
    isolated_row_country = normalize_country_name(country)
    for row in species_data:
        if normalize_country_name(row[0]) == isolated_row_country:
            return row
        
def isolate_population_row(country, population_data):
    isolated_row_country = normalize_country_name(country)
    for row in population_data:
        if normalize_country_name(row[0]) == isolated_row_country:
            return row

Country = normalize_country_name("Canada")
species_data = read_csv("Threatened_Species (1).csv", True)
population_data = read_csv("Population_Data (1).csv", True)
country_data = read_csv("Country_Data (1).csv", True)

summarize_country(Country, country_data, population_data, species_data)

