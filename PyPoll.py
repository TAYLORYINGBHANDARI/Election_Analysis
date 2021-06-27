#The data we need to retrieve
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.text")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader=csv.reader(election_data)
    # Print each row in the CSV file.
    #for row in file_reader:
       # print(row)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
  

with open(file_to_save,"w") as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the Election    \nArapahoe\nDenver\nJefferson")
    txt_file.write("----------------")


# 1. The total number of votes cast
# 2.A complete list of candidates who reveived votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidae won
# 5. The winner of the election based on popular vote.
#