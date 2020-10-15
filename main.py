import os
import shutil
from datetime import datetime


end_date = 1483217999 # Saturday, December 31, 2016 11:59:59 PM GMT+03:00 Date in Epoch Timestamp
EvidencePath = r"" # Path of folder with evidence files
DestinationPath = r"" # Path of Destination folder
folder = [] # Temporary list of files

def path_input(): # Function that takes input path
    global EvidencePath
    global DestinationPath
    EvidencePath = str(input("Enter the Evidence Path: "))
    DestenationPath = str(input("Enter the Destination Path: "))

def csv_writer(): # Main function
    global folder
    for i in os.walk(EvidencePath): # Looking through all path (EvidencePath)
        folder.append(i)
    f = open('log.txt', 'w') # Opening log.txt file to log all operations
    for a, b, files in folder: # Iterating through file list
        for file in files:
            path = (a + "\\" + file)
            print(path)
            unsorted_time = os.path.getctime(path) # Time in unsorted format
            time = datetime.fromtimestamp(unsorted_time).strftime('%Y-%m-%d %H:%M:%S') # Sorting time
            print(time)
            if unsorted_time <= end_date: # If file creation was before 31DEC2016, then download it and log
                shutil.copy(path, DestinationPath)
                f.write(path + "|" + time + "|" + "IMPORTED" + "\n")
            else: # If not, just log it in txt
                f.write(path + "|" + time + "|" + "NOT IMPORTED" + "\n")


#Function calls

path_input()
csv_writer()
