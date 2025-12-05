def normalize_country_name(country):
    country = country.strip().lower()
    lists = country.split()
    country = " ".join(lists)
    return country   

from portfolio_3 import read_csv
twoD_list = read_csv("Country_Data (1).csv", False)
def ensure_country_is_valid(country): 
    for row in twoD_list:
        if normalize_country_name(country) == normalize_country_name(row[0]):
            return True
    return False

def main_menu(country):
    while not ensure_country_is_valid(country):
        country = input("Invalid country. Please enter a valid country to analyze: ")
    print("Please select a menu #")
    print(f"Option 1: Calculate Average Population Growth for {country}")
    print(f"Option 2: Summarize Country data for {country}")
    print(f"Option 3: Calculate sustainability index for {country}")
    print(f"Option 4: Retrieve plot menu for {country}")
    print(f"Option 5: Exit")
    menu_number = int(input("Enter option number: "))
    validity_truth = True
    while validity_truth:
        if menu_number < 1 or menu_number > 5:
            menu_number = int(input("Invalid option number. Please enter a valid option number: "))
        else:
            validity_truth = False
    if menu_number == 4:
        plot_menu(country)
    

def plot_menu(country):
    compared_country = input(f"Please select a country to compare with {country}.")
    while not ensure_country_is_valid(compared_country):
        compared_country = input("Invalid country. Please enter a valid country to compare: ")
    plot_number = int(input("Please select a plot menu #\nPlot 1: Population Growth over time\nPlot 2: Threatened Species over time\nEnter option number: "))
    while plot_number < 1 or plot_number > 2:
        plot_number = int(input("Invalid option number. Please enter a valid option number: "))
    return plot_number, compared_country

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
main_menu("Canada")

import numpy as np

def summarize_country(all_data, country):
    country_row = isolate_country_row(country, all_data)
    population_row = isolate_population_row(country, all_data)
    species_row = isolate_threatened_species_row(country, all_data)
    
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
    

def average_population_growth(population_row,lower_year, upper_year):

    

#average_population_growth(["Afghanistan",38900000,38000000,37200000,36300000,35400000,34400000,33400000,32300000,31200000,30100000,29200000,28400000,27700000,27100000,26400000,25700000,24700000,23700000,22600000,21600000,20800000], 2000, 2020)


    
    

