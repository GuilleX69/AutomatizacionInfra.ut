import os
import csv

# Get the current directory
current_dir = os.getcwd()

# Define the filename of your CSV file
csv_filename = 'Accidentes_ags_2021.csv'

# Construct the full path to your CSV file
csv_file = os.path.join(current_dir, csv_filename)

# Define the indices of the 'ID' and 'AUTOMOVIL' columns (0-indexed)
id_column_index = 0  # Assuming 'ID' is the first column
automovil_column_index = 12  # Assuming 'AUTOMOVIL' is the 13th column

# Open the CSV file and read its contents using 'latin-1' encoding
with open(csv_file, newline='', encoding='latin-1') as file:
    reader = csv.reader(file)
    
    # Skip the header row if it exists
    next(reader, None)
    
    # Print the headers for the columns you want to report
    print("ID\tAUTOMOVIL")
    
    # Iterate over each row and print the values of the specified columns
    for row in reader:
        try:
            # Extract the values of the 'ID' and 'AUTOMOVIL' columns
            id_value = row[id_column_index]
            automovil_value = row[automovil_column_index]
            
            # Print the values of the 'ID' and 'AUTOMOVIL' columns
            print(f"{id_value}\t{automovil_value}")
        except IndexError:
            # Handle cases where the row doesn't have enough columns
            print("Invalid row:", row)

