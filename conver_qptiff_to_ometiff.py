import os
import shutil
import subprocess


def convert_qptiff_to_ometiff_bioformat(input_folder, output_folder, bioformats2raw_path, raw2ometiff_path):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        if filename.endswith('.qptiff'):
            input_filepath = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.ome.tiff'
            output_filepath = os.path.join(output_folder, output_filename)
            intermediate_raw_folder = os.path.join(output_folder, os.path.splitext(filename)[0]+'_raw')

            subprocess.run([bioformats2raw_path,input_filepath,intermediate_raw_folder])


            subprocess.run([raw2ometiff_path, intermediate_raw_folder,output_filepath])
            shutil.rmtree(intermediate_raw_folder)

        print('done')


if __name__ == '__main__':
    input_folder = 'C:/Users/hjchiang/Documents/Minerva/test/'
    output_folder = 'C:/Users/hjchiang/Documents/Minerva/test/'
    bioformats2raw_path = 'c:/users/hjchiang/anaconda3/bin/bioformats2raw.bat'
    raw2ometiff_path = 'c:/users/hjchiang/anaconda3/bin/raw2ometiff.bat'
    convert_qptiff_to_ometiff_bioformat(input_folder,output_folder, bioformats2raw_path, raw2ometiff_path)