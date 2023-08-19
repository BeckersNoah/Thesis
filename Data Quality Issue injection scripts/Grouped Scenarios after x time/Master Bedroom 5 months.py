#Example script of a group of sensors dissapearing from the log after a certain amount of time
import os

#Set path of original sensor log
dr = "C:/xxx/Sensor Log 100 records.txt"
Master_bedroom = 0

#Open sensor log file
with open(dr, "r") as datafile:
    #Write new log to this file
    with open("Master_bedroom.txt","w") as test: 
        for line in datafile:
            words = line.split()
            #Only when group of sensor is registered in the last month (2023-06), the records get removed and the counter increases by one
            if ("2023-06" in words[0]) and words[2] in ("s1","s3","s4","s5","s6","pressure_bed"):
                Master_bedroom += 1
                continue
            else:
                l = " ".join([words[0],words[1],words[2],words[3],words[4]])
                test.write(l + '\n') 

#Output number of changed records to console
print(Master_bedroom)