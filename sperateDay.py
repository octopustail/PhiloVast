import csv
import datetime 
import time
# tt
# dubug
import pdb
pdb.set_trace()

csvFile = open('day1.csv')
reader = csv.reader(csvFile)

# records : save records which have formated time like (hour,minute,second)
records = []

def timeFormat(time):
	# hour 
	itime = int(time)
	hour = int(itime/3600)
	# minute
	minute =int( ( itime - (hour*3600) ) /60)
	# second
	second = itime - (hour*3600 + minute*60)

	arr= [hour,minute,second]

	return arr


# sid,id,time
for item in reader:
		records.append({'id' : item[0],'sid':item[1],'timeStamp':item[2],'timeFormated':timeFormat(item[2])})

csvFile.close()
print(records)

# GroupBySid

# GroupById 