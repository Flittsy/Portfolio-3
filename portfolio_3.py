
#               ********   NOTES    *************
#docstrings, commenting, check if merge compatible




#STILL TO DO FOR READ_CSV: docstrings, commenting. \n not in char is janky but fixes things (still not ideal, tho)
def read_csv(filename, include_headers):
    file = open(filename, "r")
    data = []

    for line in file:

        line_content = line.split(",")

        for i in range(len(line_content)):
            element = line_content[i]
            if element == "\n":
                del element
                continue
            else:
                if "\n" in element:
                    line_content[i] = element.replace("\n","")
            
            for char in element:
                if (char != "0" and char != "1" and char != "2" and char != "3" 
                and char != "4" and char != "5" and char != "6" and char != "7"
                and char != "8" and char != "9" and char != "." and char != "-" 
                and "\n" not in char):
                    #there shouldn't BE any \ns left
                    #still have janky /n, which I'm not entirely happy with :(
                    break 
            else:
                line_content[i] = float(element)
        
        data += [line_content]


    if include_headers == False:
        del data[0]

    #to test print::: 
    #for row in data: print(row)
    return data
#***********end of read_csv function



# ************WRITE_CSV************************************
#     slap write_csv into one of the fxns to log "search history"
#     if theres a function where only SOME sorted data is graphed, log that portion of the list/array

#just need to take away the , if ends w commma
def write_csv(filename, data, overwrite):
    appending = "a"
    if overwrite:
        appending = "w"

    file = open(filename, appending)

    for i in range(len(data)):
        line = data[i]
        line_csv = ""
        for element in range(len(line)):
            if element == 0:
                line_csv += str(line[element])
            else:
                line_csv += ","
                line_csv += str(line[element])
        if line_csv[-2] == ",":
            #prob best to just do list slicing
            line_csv = line_csv[:-2]
        file.write(f"{line_csv}\n")

    file.close()

#**********************end write_csv function**************





#***********code that ISNT in a function definition goes below this line**************


#tester: not PEP 8 naming, but fuck that
twoD_list = read_csv( "Threatened_Species (1).csv", False )
#print(twoD_list)

tester_var = write_csv( "Elle_Country_Tester.csv", twoD_list, True)