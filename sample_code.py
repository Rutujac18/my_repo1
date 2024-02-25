
import csv
import json
import sys
# Get the input CSV file name from the command line argument
input_csv_file = sys.argv[1]

# Read the input CSV file
with open(input_csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Get the column headers from the first row of the CSV file
    headers = next(csv_reader)

    # Create an empty list to store the JSON data
    json_data = []

    # Iterate over all the lines in the CSV file and convert them into JSON format
    for line in csv_reader:
        json_data.append(dict(zip(headers, line)))

# Save the JSON data to a file with the same name but with a .json extension
output_json_file = input_csv_file.replace('.csv', '.json')
with open(output_json_file, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print("output .json file successfully created.")