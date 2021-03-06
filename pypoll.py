#add our dependencies
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")

#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Candidate options
candidate_options = []

#Declare the empty dictionary
candidate_votes = {}

#Winning Candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #read and print the header row
    headers = next(file_reader)
    
    #print each row in CSV file
    for row in file_reader:

        #Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #add a vote to that canditate's count
        candidate_votes[candidate_name] += 1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    #After opening file, print the final count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #after printing, save the final vote count to the text file
    txt_file.write(election_results)
    
    #Determine the percentage of votes for each candidate by looping through the counts
    #iterate through the candidate list
    for candidate_name in candidate_votes:

        #retrive vote count of a candidate & percentage of votes
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}; {vote_percentage:.1f}% ({votes:,})\n")

        #Print each candidate results voter count and percentage then save 
        print(candidate_results)
        txt_file.write(candidate_results)

        #Determine winning vote count, winning percentage and winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #Print winning candidate's results to the terminal
    winning_candidate_summary = (
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)



















