#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cdpinta
#
# Created:     16/12/2019
# Copyright:   (c) cdpinta 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import time
from zipfile import ZipFile

inF = (input('Input folder: ')).strip()
outF = (input('Output folder: ')).strip()
target = outF + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

def get_all_file_paths(directory):

    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
            #print(file_paths)
    # returning all file paths
    return file_paths


def main():
    # path to folder which needs to be zipped
    directory = inF #ia in arhiva calea completa

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)


    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

    # writing files to a zipfile
    with ZipFile(target,'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)

    print('All files zipped successfully!')


if __name__ == "__main__":
    main()
