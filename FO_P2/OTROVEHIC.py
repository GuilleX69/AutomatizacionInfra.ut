import os
import csv

# Get the current directory
current_dir = os.getcwd()

# Define the filename of your CSV file
csv_filename = 'Accidentes_ags_2021.csv'

# Construct the full path to your CSV file
csv_file = os.path.join(current_dir, csv_filename)

# Define the index of the column you want to sum (0-indexed)
column_index = 24  # Assuming 'OTROVEHIC' is the 25th column (0-indexed)

# Initialize total sum
total_sum = 0

# Open the CSV file and read its contents using 'latin-1' encoding
with open(csv_file, newline='', encoding='latin-1') as file:
    reader = csv.reader(file)
    
    # Skip the header row if it exists
    next(reader, None)
    
    # Iterate over each row and add the value of the specified column to the total sum
    for row in reader:
        try:
            # Convert the value to an integer and add it to the total sum
            total_sum += int(row[column_index])
        except ValueError:
            # Handle cases where the value cannot be converted to an integer
            print(f"Invalid value in row: {row}")

# Print the total sum
print("Total sum of 'OTROVEHIC' column:", total_sum)
