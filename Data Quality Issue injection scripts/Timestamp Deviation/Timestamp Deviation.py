import os
import random
import datetime
from datetime import datetime, timedelta, time

#Set the path to the sensor log
dr = "C:/xxx/Sensor Log 100 records.txt"
records = 0
avtime = []
text = list()

#Open the sensor log file
with open(dr, "r") as datafile:
        for line in datafile:
            words = line.split()
            #random chance of 10% to deviate a timestamp
            if random.randint(0,9) == 0:
                records += 1
                dt = " ".join([words[0],words[1]])
                org_date = datetime.strptime(dt,'%Y-%m-%d %H:%M:%S')
                #Set a random delay between 1 and 59 seconds
                delay = datetime.strptime(str(random.randint(1,59)), '%S')
                avtime.append(delay.second)
                #50-50 chance of either adding or substracting the delay
                if random.randint(0,1) == 0:
                    new_time = org_date + timedelta(hours=delay.hour, minutes=delay.minute, seconds=delay.second)
                else:
                    new_time = org_date - timedelta(hours=delay.hour, minutes=delay.minute, seconds=delay.second)
                l = " ".join([str(new_time),words[2],words[3],words[4]])
            else:
                l = " ".join([words[0],words[1],words[2],words[3],words[4]])
            #Insert all lines of the log into a list so they can be sorted again by date and time
            text.append(l)

#Sort the log and write it to a file
text.sort()
with open("60_seconds.txt","w") as test:
    for line in text:
        test.write(line + '\n')

#Output number of records altered to the console, aswell as the average timestamp deviation
print(records)
average = sum(avtime)/len(avtime)
print(average)