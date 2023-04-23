import json
import codecs
# from mac
# path = '/Users/rose/Documents/OneDrive - Akoya Biosciences/Documents/Minerva/08-Breast/'
# from window
path = '/Users/rose/Library/CloudStorage/OneDrive-AkoyaBiosciences/Documents/Minerva/08-Breast/'
file_path = path + '08-breast_cancer_window0420.story copy.json'
output_file_path = path + '08-breast_cancer_window0420.story copy.json'
new_in_file_path = path + "20221220_S1614455_C21_Scan1.ome.tiff"
marker_path = path + "20221220_S1614455_C21_Scan1_marker.csv"
rootpath = "/Users/rose/Library/CloudStorage/OneDrive-AkoyaBiosciences/Documents/minerva_author_macos"
with open(file_path, "r") as f:
    data = json.load(f)

data["csv_file"] = marker_path
data["in_file"] = new_in_file_path
data["root_dir"]= rootpath

with open(output_file_path, "w") as f:
    json.dump(data, f)

print("Modified in_file path in", file_path)