import csv 

class convert:
	def readCSV(filer):
		exampleFile = open(filer)
		exampleReader = csv.reader(exampleFile)
		for row in exampleReader:
			print('Row #'+str(exampleReader.line_num)+' '+str(row))

	def writeCSV():
		outputFile = open('output.csv','w')
		outputWriter = csv.writer(outputFile)
		outputWriter.writerow(['Hello,world!','choco','hero'])
		outputFile.close()

	if __name__ == "__main__":
		readCSV('output.csv')
		writeCSV()