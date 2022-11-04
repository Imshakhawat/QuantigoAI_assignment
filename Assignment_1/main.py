from modifier import *

directory = 'sampleJson/pos_0.png.json'

f = open(directory)
data = json.load(f)
sample = open('sampleJson/defaultformat.json')
sample_json = json.load(sample)

output = file_formatter(sample_json, data, directory)

with open(output_directory(directory), 'w') as f2:
    json.dump(output, f2)
f.close()
f2.close()
