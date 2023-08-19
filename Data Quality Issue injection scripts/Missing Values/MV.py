import os
import random

#Set path to original sensor log file
dr = 'C:/xxx/Sensor Log 100 records.txt'
lines = 0

#Open the file
with open(dr, "r") as datafile:
    #Write the new log with missing values to this file
    with open("MV.txt","w") as test:
        for line in datafile:
            words = line.split()
            l = " ".join([words[0],words[1],words[2],words[3]])
            # 10% chance the following statement is true, when this happens the line doesnt get written down and the counter increases by 1
            if random.randint(0,9) == 0:
                lines += 1
                continue
            else:
                test.write(l + '\n')

#Print the number of skipping lines to the log
print(lines)