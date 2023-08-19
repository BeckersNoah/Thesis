#This script removes all sensor log records from a certain group, in this case its the Master Bedroom group
import os

#Set path to original sensor log file
dr = "C:/xxx/Sensor Log 100 records.txt"
Master_bedroom = 0

#Open original sensor log file
with open(dr, "r") as datafile:
    #Write new log to this file
    with open("Master_bedroom.txt","w") as test: 
        for line in datafile:
            words = line.split()
            #If the name of the sensor is in this list, the record gets skipped and a counter increases by one
            if words[2] in ("s1","s3","s4","s5","s6","pressure_bed"):
                Master_bedroom += 1
                continue
            #Otherwise, write the original record to the new file
            else:
                l = " ".join([words[0],words[1],words[2],words[3],words[4]])
                test.write(l + '\n') 

#Output the number of skipped lines to the console
print(Master_bedroom)