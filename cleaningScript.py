import csv

#Table to read data from
with open('test.csv', 'rb') as file:
	scanner = csv.reader(file, delimiter=',', quotechar='|')
	#Table to output results to
	with open ('cleaned.csv', 'wb') as table2:
		output = csv.writer(table2, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		#First row of table
		output.writerow(['Course name'] + ['Course#'] + ['Section#'] + ['Total grades'] + ['GPA'] + ['A'] + ['AB'] + ['B'] + ['BC'] 
			+ ['C'] + ['D'] + ['F'] + ['S'] + ['U'] + ['CR'] + ['N'] + ['P'] + ['I'] + ['NW'] + ['NR'] + ['Other'])
		#Initialize loop variables
		#The rowCount is used to filter out first 5 lines, its reset at the end of each page
		#foundTerm is used once to write the current term into output file
		#firstItr is used to cover 1st iter special cases
		rowCount = 0
		foundTerm = False
		firstItr = True
		for row in scanner:
			#marks end of a page
			if(row[0].find("* Please note:")!=-1):
				rowCount =  0
				#continue
			#marks finding and skipping the page number line
			elif(row[17].find("Page")!=-1 or row[18].find("Page")!=-1 
				or row[19].find("Page")!=-1 or row[20].find("Page")!=-1):
				rowCount = rowCount + 1
			#marks finding the curr term
			elif(rowCount==1 and foundTerm==False):
				output.writerow([row[0]])
				foundTerm = True
				rowCount = rowCount + 1
			#makrs finding the department name in 1st itr
			elif(firstItr and rowCount==4):
				output.writerow([row[0]])
				rowCount = rowCount + 2
				continue
			#makrs finding department name in the rest of itrs
			elif(rowCount==4):
				output.writerow([row[0]])
				rowCount = rowCount + 1
				#continue
			#marks finding classes
			elif(rowCount>=6):
				#skip the 6th row in 1st itr
				if(firstItr):
					firstItr = False
					rowCount = rowCount + 1
				else:
					output.writerow(row)
					rowCount = rowCount + 1
					#continue
			else:
				rowCount = rowCount + 1