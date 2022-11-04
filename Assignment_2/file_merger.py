import json
import os
from merger_func import *

# Enter the directory here
directory ='E:\Codes\IDE\Pycharm\Python_Scripts\Quantigo\sampleJson'

# recieving the file list exist in the given directory
file_list = file_list_handler(directory)
#sending the file list to the merger function
# this function will create the marged file
merge_JsonFiles(file_list)



