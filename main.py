""" Authorship: Code Submission by Devan Hall
    Contributors: Logan Keech and Cesar Martinez in 
    developing the dataset and providing accurate insights 
    into programming methodology """


import csv                                         # import csv module to handle files


def read_csv(csv_file_name):                       # define read() function
    with open(csv_file_name, "r") as csvfile:      # open file with read permissions
        csvreader = csv.reader(csvfile)            # iterate through csv file and store lines in csvreader

        for lines in csvreader:                    # for loop to iterate over all lines in csv
            results = []                           # creating an empty list to store lines
            results.append(lines)                  # adding each line to the new list
            print(results)                         # printing the new list of lists

def main():                                        # main function
    read_csv("Data.csv")                           # function call to read_csv to read and print the data


if __name__ == "__main__":
    main()