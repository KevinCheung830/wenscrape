import csv

# Read the input file
input_file = 'input.txt'
output_file = 'output.csv'

# Assuming the delimiter is a comma
data = []
with open(input_file, 'r') as file:
    for line in file:
        data.append(line.strip().split(','))

# Write the data to a CSV file
with open(output_file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)