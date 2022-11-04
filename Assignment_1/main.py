from modifier import *

# Enter the directory here
directory = 'sampleJson/pos_0.png.json'

f = open(directory)
data = json.load(f)

# this is the sample json directory
sample = open('sampleJson/defaultformat.json')
sample_json = json.load(sample)

# sending the sample json, main json file and the directory
#then retriving the formatted data
output = file_formatter(sample_json, data, directory)

# now writing the formatted data in the source directory
with open(output_directory(directory), 'w') as f2:
    json.dump(output, f2)
f.close()
f2.close()
