import json

# from mac in mac
# path = '/Users/rose/Documents/OneDrive - Akoya Biosciences/Documents/Minerva/08-Breast/'
# from window to mac
path = '/Users/rose/Library/CloudStorage/OneDrive-AkoyaBiosciences/Documents/Minerva/08-Breast/'
# from mac to window
path = "C:/Users/hjchiang/OneDrive - Akoya Biosciences/Documents/Minerva/09-Pancrease/"
# "C:\Users\hjchiang\OneDrive - Akoya Biosciences\Documents\Minerva\09-Pancrease\out_mac0418.story.json"

file_path = path + 'out_mac0418.story.json'
output_file_path = path + 'out_0422window.story.json'
new_in_file_path = path + "20230110_MGH PDAC_1B_30px_HJ_Scan1.ome.tiff"
marker_path = path + "MarkerList_MGH PDAC 1B.csv"

rootpath_mac = "/Users/rose/Library/CloudStorage/OneDrive-AkoyaBiosciences/Documents/minerva_author_macos"
rootpath_window = "C:/Users/hjchiang/OneDrive - Akoya Biosciences/Documents/minerva_author_macos"
with open(file_path, "r") as f:
    data = json.load(f)

data["csv_file"] = marker_path
data["in_file"] = new_in_file_path
data["root_dir"]= rootpath_window

with open(output_file_path, "w") as f:
    json.dump(data, f)

print("Modified in_file path in", file_path)