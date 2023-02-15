import csv

with open("example_abp_data.csv", "r") as file:
  datalist = csv.reader(file)
  for row in datalist:
    row.append("test")
    print(row)




