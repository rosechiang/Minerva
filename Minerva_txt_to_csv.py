import os 
import csv

folder_path = 'C:/Users/hjchiang/Documents/Minerva/test/'


for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        with open(os.path.join(folder_path, filename),'r') as txt_file:
            lines = txt_file.readlines()

        with open(os.path.join(folder_path,filename.replace('.txt','.csv')),'w',newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['marker_name'])

            for line in lines:
                writer.writerow([line.strip()])


