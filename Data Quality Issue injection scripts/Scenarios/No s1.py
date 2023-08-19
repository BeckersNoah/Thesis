#This file is an example of how to remove all sensor log records from motion sensor s1
import os

#Set path to sensor log
dr = "C:/xxx/Sensor Log 100 records.txt"
s1 = 0

#Open sensor log file
with open(dr, "r") as datafile:
    #Write new log to this file
    with open("nos1.txt","w") as test: 
        for line in datafile:
            words = line.split()
            #If the name of the sensor equals 's1', the line gets skipped and a counter increases by one
            if words[2] == 's1':
                s1 += 1
                continue
            #Otherwise, write the original record to the new file
            else:
                l = " ".join([words[0],words[1],words[2],words[3],words[4]])
                test.write(l + '\n') 

#Output the amount of 's1' instances to the console
print(s1)