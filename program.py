#!/usr/bin/env python3
#
# program for testing csv file reading

import  csv

data = csv.reader(open('data.csv', newline=''), delimiter=' ', quotechar='|')

for row in data:
	print (','.join(row))


'''
with open('data.csv', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		print(row)

'''
'''
with open('data.csv', newline='') as f:
	reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
	for row in reader:
		print(row)
'''
