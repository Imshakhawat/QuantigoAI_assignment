import json
import os

# this function recieves a the whole json object and extracts bbox data
# returns the data in array format
def bbox_extractor(data):
	vehicle_bbox = []
	licence_bbox = []

	for items in data['objects']:
		if items['classTitle'] == "Vehicle":
			vehicle_bbox = items['points']['exterior'][0] + items['points']['exterior'][1]
		if items['classTitle'] == "License Plate":
			licence_bbox = items['points']['exterior'][0] + items['points']['exterior'][1]
	return vehicle_bbox, licence_bbox

# this function recieves a the whole json object and extracts attribute data
# returns the data in key-value format
def attribute_extractor(data):
	vehicle_attribute = {}
	licence_attribute = {}
	for items in data['objects']:
		if items['classTitle'] == "Vehicle":
			if("tags" in items):
				for key in items['tags']:
					vehicle_attribute[str(key['name'])] = key['value']
		if items['classTitle'] == "License Plate":
			if("tags" in items):
				for key in items['tags']:
					licence_attribute[str(key['name'])] = 0 if key['value'] == "0" else key['value']
	return vehicle_attribute, licence_attribute


