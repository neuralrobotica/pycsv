#!/usr/bin/env python3 
#
# python csv reader, for testing if a csv file can work with this module.
#
#
# create a function that can modfiy a csv file, or read historical data from Metatrader 5 market data.
#

import csv
with open('msft_csv_15m.csv', newline='') as f:
	reader = csv.reader(f)

	for row in reader(['SPREAD']):
		print(row)
