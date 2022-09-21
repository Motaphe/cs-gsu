# Prolog
# Author:  Suzal Regmi
# Email:  sregmi2@student.gsu.edu
# Section: 036
# Reference: no one
# Timestamp: 11:25
# Approximate Time Taken: 20 minutes

# Assignment Info: We coded a program that allows Road Runner to determine what time he should 
# should put his alarm at for his desired need.

print()
hours = int(input("HOURS:"))
minutes = int(input("MINUTES:"))
time = int(input("TIME:"))

conversion = ((hours*60 + minutes) - time)/60
hours = int(conversion) 
minutes = round((conversion - hours) * 60)

print (f"\nALARM TIME: {hours:02}:{minutes:02}\n")

