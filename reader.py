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

#show a specified row

with open('msft_csv_15m.csv') as csvfile:
#	data = [row for row in csv.reader(csvfile)]
	data = list(csv.reader(csvfile))

	print(data[1][0])
