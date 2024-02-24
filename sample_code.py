
import csv
import json

# Read the CSV file
with open('sample_test_data.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Get the column headers
    headers = next(csv_reader)

    # Create an empty list to store the JSON data
    json_data = []

    # Iterate over the remaining rows in the CSV file
    for row in csv_reader:
        # Create a dictionary to store the row data
        row_data = {}

        # Iterate over the columns in the row
        for i, column in enumerate(headers):
            # Add the column data to the dictionary
            row_data[column] = row[i]

        # Add the dictionary to the list of JSON data
        json_data.append(row_data)

# Save the JSON data to a file
with open('sample_test_data.json', 'w') as json_file:
    # Convert the list of dictionaries to a JSON string
    json_string = json.dumps(json_data)

    # Write the JSON string to the file
    json_file.write(json_string)
