
#               ********   NOTES    *************
# also note, to research: in zylabs outline, talks about an "overwrite" feature
#      it is a flag for the write feature
# "Your application must return useful information"

#STILL TO DO FOR READ_CSV: header, \n and scope?, docstrings, actually return data array

#need to do the docstrings
def read_csv(filename, include_headers):
    file = open(filename, "r")
    data = []

    for line in file:
            #deal with headers by::: if line==0

        line_content = line.split(",")

        for i in range(len(line_content)):
            element = line_content[i]
            if element == "\n":
                del element
                continue
            else:
                if "\n" in element:
                    line_content[i] = element.replace("\n","")
            print(line_content[i], "this is line content") 
                
            #element and char are correct values (words and singular characters)
           # if ( "0" in element or "1" in element or "2" in element or)

#******************************************
#****************************************** (see comments below)
            for char in element:
                #seems to always error on the last digit of the number: does this have something
                #to do with /n replacement above?

                #it seems to be running one too many times for only the last item

 # ******BOOM***** adding "/n" not in char to if statement SUUGGETS 
 # that it's an issue with SCOPE/depth
 #    this is quite odd: how can a singular char be compared to "/n" (two chars?)
 #******** def issue with scope and "updating": if using country data, proves that 
 #         /n cannot be converted to a float (it's still there???)
               

                #very helpful test print right below (proves above assertion)
                print(element, char)
                #technically printing this for monaco area, just element AND char are 
                #    BOTH still \n (they AREN'T empty, they are \n)
                #    further proof of fucked scope
                if (char != "0" and char != "1" and char != "2" and char != "3" 
                and char != "4" and char != "5" and char != "6" and char != "7"
                and char != "8" and char != "9" and char != "." and char != "-" 
                and "\n" not in char):
#*********still don't really think the \n not in char is the way to fix this: 
#    it kinda fixes some bugs but makes others (not getting to root of problem here)
                    #using test print, KNOW that this loop is successfully checking the chars
                    #however, it is ALWAYS triggering (see assertion above)

                    #this test print PROVES that this is evaluating the element again 
                            #with a completely empty char!
                    #print("element is", element, "char is", char)
                    break 
            else:
                line_content[i] = float(element)
                print("changed element to float")
        
        data += [line_content]


    #to test print::: 
    for row in data: print(row)
 
    #return the 2d list (data)

#tester: not PEP 8 naming, but fuck that
twoD_list = read_csv( "Threatened_Species (1).csv", False )

#country data is only one fucked up w this code atm (bc of \n)
#    erroring at Monaco because it has no sq km data after the comma (sudan also missing this data)
#    so, likely that the ONLY content in that spot where there SHOULD be sq km is \n
#    presence of only /n triggers the float conversion (no #s)



    

