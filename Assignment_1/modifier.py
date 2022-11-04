import json
import os
from extractor import *
from pathlib import Path

# this function recieves sample json object and source json object 
# then it sets the values bbox data of sample object [ the bbox data comes from  bbox_extractor function in extractor file]
# returns the sample json object with updated value
def bbox_data_setter(sample, data):
	bbox_data = bbox_extractor(data)
	if(len(bbox_data[0])!= 0):
		sample[0]['annotation_objects']['vehicle']['presence'] = 1
		sample[0]['annotation_objects']['vehicle']['bbox'] = bbox_data[0]
	if (len(bbox_data[1]) != 0):
		sample[0]['annotation_objects']['license_plate']['presence'] = 1
		sample[0]['annotation_objects']['license_plate']['bbox'] = bbox_data[1]
		sample[0]['annotation_attributes']['license_plate']['Occlusion'] = 0
	return sample

# this function recieves sample json object and source json object 
# then it sets the values attribute data of sample object [ the bbox data comes from  attribute_extractor function in extractor file]
# returns the sample json object with updated value
def attribute_data_setter(sample, data):

	attribute_data = attribute_extractor(data)
	if len(attribute_data[0])!= 0:
		sample[0]['annotation_attributes']['vehicle'] = attribute_data[0]
	if len(attribute_data[1]) != 0:
		sample[0]['annotation_attributes']['license_plate']['Difficulty Score'] = attribute_data[1][
		'Difficulty Score']
		sample[0]['annotation_attributes']['license_plate']['Value'] = attribute_data[1]['Value']
	return sample
# this function recieves directory of source file
# returns output directory of formatted file
def output_directory(file_directory):
	file_name = "formatted_" + os.path.basename(file_directory)
	path1 = os.path.normpath(file_directory)
	dir = path1.split(os.sep)
	output_json_directory = ""
	for item in range(len(dir)-1):
		output_json_directory = output_json_directory + dir[item]+'/'
	output_json_directory = output_json_directory+file_name
	return output_json_directory

# this function recieves recieves directory of source file and sample json object
# then it updates the dataset_name key with the file name
# returns the sample json object with updated value
def file_name_setter(file_directory, sample):
	sample[0]['dataset_name'] = os.path.basename(file_directory)
	return sample


# this function is for reducing complexity in the main.py file
# this function recieves recieves directory of source file , sample json object and source json object
# then it calls all the functions exist in modifier.py file
# it process the whole formatted file and returns to the main.py

def file_formatter(formatted_data, data, directory):
	formatted_data = bbox_data_setter(formatted_data, data)
	formatted_data = attribute_data_setter(formatted_data, data)
	formatted_data = file_name_setter(directory, formatted_data)
	return formatted_data