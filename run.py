        
# Install pandas in env with pip install pandas
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
    



# print(input_data)
# print(abp_data)
print(output_data)