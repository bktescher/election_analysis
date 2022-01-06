#add our dependencies
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")

#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #read and print the header row
    headers = next(file_reader)
    print(headers)






# #Using the open() function with the "w" mode we will write data to the file.
# with open(file_to_save, "w") as txt_file:

    # #write three counties to the file
    # txt_file.write(
    #     "Counties in the Election\n"
    #     "------------------------\n"
    #     "Arapahoe\nDenver\nJefferson")















