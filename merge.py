#!/usr/bin/env python3

import os, sys
import csv

if len(sys.argv) != 3:
	print('usage:', sys.argv[0], 'orbits-file impacts-file > merged-file')
	exit(1)

all_orbits = {}
fields = []

with open(sys.argv[1], 'r') as f_orbits:
	reader = csv.DictReader(f_orbits)	
	fields = reader.fieldnames
	for row in reader:
		name = ' '.join(row['Object Name'].split())
		all_orbits[name] = row

with open(sys.argv[2], 'r') as f_impacts:
	reader = csv.DictReader(f_impacts)	
	for field in reader.fieldnames:
		if field not in fields:
			fields.append(field)
	writer = csv.DictWriter(sys.stdout, fieldnames=fields)
	writer.writeheader()

	for row in reader:
		name = row['Object Name']
		if name in all_orbits:
			orbit = all_orbits[name]
		else:
			for key in all_orbits:
				if name in key:
					orbit = all_orbits[key]
					break
			else:
				continue
		merged = {**orbit, **row}
		merged['Object Name'] = name
		writer.writerow(merged)
