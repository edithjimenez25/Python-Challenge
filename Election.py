#This code analyze the election data presented by the state
#The dataset is composed of three columns: `Voter ID`, 'County' and `Candidate`.
#Results of the votes results Data is located on Instructions\PyPoll\Resources\election_data.csv

import os
import csv

#Create a path to the resource file
#Resources file is is located on \Resources\election_data.csv
Election_path = os.path.join("Resources","election_data.csv")

#create the variables for Voter ID, and Candidate
candidates = []
Number_Votes=0
Number_Votes_Counts = []

#open the data file Election
with open(Election_path, newline='') as csvfile:
    #use the csvfile
    csvreader = csv.reader(csvfile, delimiter= ',')
#skid the header
    next(csvreader)
#read through the lines to obtain votes
    for line in csvreader:
        #obtain the total number of votes
        Number_Votes=Number_Votes + 1
        #obtain which candidate votes go
        candidate = line[2]
        #add votes to candidate
    if candidate in candidates:
        candidate_index=candidates.index(candidate)
        Number_Votes_Counts[candidate_index] = Number_Votes_Counts[candidate_index] + 1
    #create a candidate on the list
    else:
        candidates.append(candidate)
        Number_Votes_Counts.append(1)

#Calculate the percentage of votes per candidate
#create a variables
Percentages = []
Maximum_Votes = Number_Votes_Counts[0]
Maximum_Votes_Index = 0
#Determine the percentage of vote per candidate
for count in range(len(candidates)):
    Percentage_Votes= Number_Votes_Counts[count]/Number_Votes*100
    Percentages.append(Percentage_Votes)
    if Number_Votes_Counts[count] > Maximum_Votes:
        Maximum_Votes=Number_Votes_Counts[count]
        print(Maximum_Votes)
        Maximum_Votes_Index=count
winner = candidate[Maximum_Votes_Index]

#print the results of the votes
print("Election Results")
print("--------------------------")
print(f"Total Votes: {Number_Votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {Percentage_Votes}% ({Number_Votes_Counts})")
#    print(f"{candidates[count]}: {Percentage_Votes[count]}% ({Number_Votes_Counts[count]})")
print("--------------------------")
print(f"Winner: {winner} ")
print("--------------------------")

#Define the output file
output_path=os.path.join('outputPyPoll.txt')

#Write the file results to txt 
write_file_Election_Results = f"Election_Results_Summary.txt"

Election_writer=open(output_path, mode = 'w')

#write the results into the Output file
Election_writer.write("Election Results\n")
Election_writer.write("--------------------------")
Election_writer.write(f"Total Votes: {Number_Votes}\n")
for count in range(len(candidates)):
    Election_writer.write(f"{candidates[count]}:{Percentage_Votes[count]}%({Number_Votes_Counts[count]})\n")
Election_writer.write("--------------------------")
Election_writer.write(f"Winner: {winner}")
Election_writer.write("--------------------------")

#close the output file
Election_writer.close()
