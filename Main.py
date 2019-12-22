#This code analyze the budget data presented by the company
#The dataset is composed of two columns: `Date` and `Profit/Losses`.
#Financial Data is located on PyBank\Resources\budget_data.csv

import os
import csv

#Create a path to the resource file
#Resources file is is located on Resources\budget_data.csv
Budget_csv=os.path.join("Resources","budget_data.csv")

#create the list to storage data Date & Profit/loss columns
#list for the date which are the same type of element dd-mmm"
Date=[]
#list for Profit/Loss which are only integer
Profit_Loss=[]
#the difference is
Profit_Loss_Difference=[]

#reading the data from Budget_csv file, string default 'r'
#open the reader plain text in the csv file
with open(Budget_csv,'r') as csvfile:
    csvreader=csv.reader(csvfile)

#skid the header
    next(csvreader)
#append an element at the end of the list 
    for row in csvreader:
        Profit_Loss.append(int(row[1]))
        Date.append(row[0])
#Determine the The total number of months included in The dataset
#use len to determine the lenght of the list
Total_Number_Months=len(Date)

#Verifying the result for number of months by printing it
print(Total_Number_Months)

#Calculate Total amount of "Profit/Losses" over the entire period
#loop through the Profit/Loss values to find the greatest increase profit and greatest decrease loss values
for i in range(1,len(Profit_Loss)):
    Profit_Loss_Difference.append(Profit_Loss[i]-Profit_Loss[i-1])
    Total_Profit_Loss=sum(Profit_Loss)
    Average_Profit_Loss_Difference=sum(Profit_Loss_Difference)/len(Profit_Loss_Difference)
    Maximum_Profit_Loss_Difference=max(Profit_Loss_Difference)
    Minimum_Profit_Loss_Difference=min(Profit_Loss_Difference)
    
for i in range(len(Profit_Loss_Difference)):
    if Profit_Loss_Difference[i]>=Maximum_Profit_Loss_Difference:
        Maximum_Profit_Loss_Difference_Date=Date[i+1]
    elif Profit_Loss_Difference[i]<=Minimum_Profit_Loss_Difference:
        Minimum_Profit_Loss_Difference_Date=Date[i+1]

#print intermedium results
print(Total_Profit_Loss)
print(Average_Profit_Loss_Difference)
print(Maximum_Profit_Loss_Difference)
print(Maximum_Profit_Loss_Difference_Date)
print(Minimum_Profit_Loss_Difference)
print(Minimum_Profit_Loss_Difference_Date)

#Define the output file

output_path=os.path.join('outputPybank.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as outfile:
    #Initialize csv.writer
    csv.writer=csv.writer(outfile, delimiter=',')
    #write title of the results
    outfile.writelines("Financial Analisys\n")
    outfile.writelines('----------------------------' + '\n')
    #write the number of months
    outfile.writelines("Total Months: " + str(Total_Number_Months) + "\n")
    #Write Net Total Amount of Profit/Loss
    outfile.writelines("Net Total Amount: $" + str(Total_Profit_Loss) + "\n")
    # Write Average Changes in Profit/Loss
    outfile.writelines('Average Changes in Profit/Loss: $' + str(Average_Profit_Loss_Difference) + '\n')
    # Write the greatest increase in profits (date and amount) over the entire period
    outfile.writelines("Greatest Increase Profit : " + Maximum_Profit_Loss_Difference_Date + ' ($' + str(Maximum_Profit_Loss_Difference)+')'+'\n')
    # write the greatest decrease in loss (date and amount) over the entire period
    outfile.writelines("Greatest Decrease Loss : " + Minimum_Profit_Loss_Difference_Date + ' ($' + str(Minimum_Profit_Loss_Difference) +')')

#Open the outfile to write in Terminal
with open(output_path, 'w',newline='') as csvfile:
    csv_writer =csv.writer(csvfile)
    #write the header row
    csv_writer.writerow(["Financial Analisys"])
    print(csvfile.read())

#open the file to write
filewriter=open(output_path, mode='w')

#Print the Financial Results to the output file 

