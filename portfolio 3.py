
#               ********   NOTES    *************
# also note, to research: in zylabs outline, talks about an "overwrite" feature
#      it is a flag for the write feature
# "Your application must return useful information"




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
    for row in data: print(row)
    return data
#***********end of read_csv function



#***********code that ISNT in a function definition goes below this line**************


#tester: not PEP 8 naming, but fuck that
twoD_list = read_csv( "Threatened_Species (1).csv", True )
#print(twoD_list)

