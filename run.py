        
# Install pandas in env with 'pip install pandas'
import csv
import pandas as pd

# Creating variables for the CSV data
input_data = pd.read_csv('example_input_data.csv')
abp_data = pd.read_csv('example_abp_data.csv')


# Creating a new CSV with data from input_data
with open('example_output_data.csv', 'w') as f:
    data = pd.DataFrame(input_data)
    data.to_csv("example_output_data.csv")
    output_data = pd.read_csv('example_output_data.csv')
    
    df = pd.DataFrame(output_data)
    df["Street_In_Postcode"] = "test"

    # OPTION A
    # for loop to go through each address in the output_data individually to check against the abp
    # If else statement saying something along the lines of:
    # if address_line_2 (in input_data) has postcode == street_name (in abp_data):
    #    column 7 in output_data = "Yes"
    # else: 
    #    column 7 in output_data = "No"

    # OPTION B
    # vlookup (stack overflow search suggestion) for comparing CSV files, but I wouldn't know where to start,
    # seems less straightforward than some examples as there isn't an equal amount of data entries on the CSV files
    # Given more time, I'd work the problem and figure it out using vlookup for cleaner more readable/maintainable code, 
    # but currently, I'd be more likely to go for option A, as more comfortable with standard python syntax

    # Thanks for the challenge!
    # DW
   
# print(input_data)
# print(abp_data)
print(output_data)