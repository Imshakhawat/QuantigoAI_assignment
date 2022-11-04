import json
import os

def directory_builder(file_directory):
	path1 = os.path.normpath(file_directory)
	dir = path1.split(os.sep)
	json_directory = ""
	for item in range(len(dir)):
		json_directory = json_directory + dir[item]+'/'
	return json_directory

def file_list_handler(directory):
	files = []
	dir = directory_builder(directory)
	for file in os.listdir(directory):
		files.append(dir+os.fsdecode(file))
	return files


def merge_JsonFiles(filename):
    result = []
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.append(json.load(infile))

    with open('merged_json_file.json', 'w') as output_file:
        json.dump(result, output_file)



