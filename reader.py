#!/usr/bin/env python3 
#
# python csv reader, for testing if a csv file can work with this module.
#
#
# create a function that can modfiy a csv file, or read historical data from Metatrader 5 market data.
#

import csv
'''
with open('msft_csv_15m.csv') as csvfile:
	reader = csv.reader(csvfile)

	for row in csvfile:
		print(row)
'''

#show a  row

'''

with open('msft_csv_15m.csv') as csvfile:
#	data = [row for row in csv.reader(csvfile)]
	data = list(csv.reader(csvfile))
	for csvfile in data:
		print(data[0],data[1])


file = open('msft_csv_15m_.csv')
reader = csv.reader(file)

for line in reader:
	print line([0], line[1])


'''
