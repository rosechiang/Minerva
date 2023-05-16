import os
import csv

# define the folder containing the CSV files
folder_path = 'C:/Users/hjchiang/Documents/Minerva/test/'

# create a dictionary to store the rows from each CSV file, with filenames as keys
file_rows = {}

# loop through each CSV file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # open the CSV file and read its contents
        with open(os.path.join(folder_path, filename), 'r') as csv_file:
            reader = csv.reader(csv_file)
            # skip the first row, assuming it contains only the column label
            next(reader, None)
            # add each row to the dictionary of rows for this file
            rows = []
            for row in reader:
                rows.append(row[0])
            file_rows[filename] = rows

# create the combined CSV file and write the rows to it
with open(os.path.join(folder_path, 'combined.csv'), 'w', newline='') as combined_file:
    writer = csv.writer(combined_file)
    # write the filename as the first row
    writer.writerow(['filename'] + list(file_rows.keys()))
    # write the data from each CSV file as a separate column
    num_rows = max(len(rows) for rows in file_rows.values())
    for i in range(num_rows):
        row = [str(i)]
        for filename in file_rows.keys():
            rows = file_rows[filename]
            if i < len(rows):
                row.append(rows[i])
            else:
                row.append('')
        writer.writerow(row)
