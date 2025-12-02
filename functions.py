
def average_population_growth(population,year):
    #Calculates average population growth per year
    #Uses NumPy, makes a graph

def species_density(species_data, country_data):
    #Computes amount of threatened species per 1000km
    #Uses 2 data sets

def find_country_with_fastest_growth(population_data):
    #Computes and returns data with fastest population growth
    #Simple, useful

def sustainability_risk_index(country_data, population_data, species_data):
    #Uses an index calculation like (threatened species/area) * population_growth_rate
    #Returns 5 worst (highest) index's
    #potentially uses data from previous function

def future_population_predictor(population_data, years_into_future):
    #User gives a country, finds current population, calculates average growth, returns population in future
    #Easily plottable, maybe more complicated

def summarize_country(all_data):
    #Creates averages, minimums, maximums, density, growth, etc.
    #Easily knocks out requirements

#Main plan:
#   -Calculate average population growth
#   -Summarize country data
#   -Sustainability risk index

def normalize_country_name(country):
    country = country.strip().lower()
    
def get_country():
    country = input("Enter the country you want to analyze: ")
    for c in country:
        if c == " " or c == "." or c == "-":

            
            
    fixed_country = country[0].upper() + country[1:].lower()
    if fixed_country 
    return fixed_country

def average_population_growth(population_data,year):
    country = input("Enter the country you want to analyze: ")
    fixed_country = country[0].upper() + country[1:].lower()
    for row in population_data:
        if row[0] == fixed_country:
            start_pop = row[21]
            end_pop = row[1]
            avg_growth = (end_pop - start_pop)/20
            #so avg linear growth then (secant line)?
            return avg_growth
        if 