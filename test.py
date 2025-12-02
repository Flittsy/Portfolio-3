def normalize_country_name(country):
    country = country.lower()
    lists = country.split()
    country = " ".join(lists)
    return country   

from portfolio_3 import read_csv
twoD_list = read_csv("Country_Data (1).csv", False)
def ensure_country_is_valid(country): 
    for column in twoD_list:
        if country == twoD_list[0]:
            return True
    return False

def main_menu(country):
    country = normalize_country_name(country)
    ensure_country_is_valid(country)
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
    fixed_compared_country = normalize_country_name(compared_country)
    while ensure_country_is_valid(fixed_compared_country) == False:
        fixed_compared_country = input("Invalid country. Please enter a valid country to compare.")
        if ensure_country_is_valid(fixed_compared_country):
            break
    plot_number = int(input("Please select a plot menu #\nPlot 1: Population Growth over time\nPlot 2: Threatened Species over time\nEnter option number: "))
    validity_truth = True
    while validity_truth:
        if plot_number < 1 or plot_number > 2:
            plot_number = int(input("Invalid option number. Please enter a valid option number: "))
        else:
            validity_truth = False
            return plot_number, fixed_compared_country
        
main_menu("Canada")
    

    

#def average_population_growth(population_row,lower_year, upper_year):
    

#average_population_growth(["Afghanistan",38900000,38000000,37200000,36300000,35400000,34400000,33400000,32300000,31200000,30100000,29200000,28400000,27700000,27100000,26400000,25700000,24700000,23700000,22600000,21600000,20800000], 2000, 2020)


    
    

