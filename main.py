import csv
import numpy as np

with open("titanic.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  headers = next(data)
  data = list(data)
  data = np.array(data)
  

survived = np.array(data[:,[0]], dtype=int).flatten()
print(headers)
fare = np.array(data[:,[7]], dtype=float).flatten()

#empty lists to hold data from  the for loop
fare_survived = []
fare_not_survived = []

#ADD CODE: for loop and if/else statements
for i in range(0, len(fare)):
  if survived[i] == 1:
    fare_survived.append(fare[i])
  else:
    fare_not_survived.append(fare[i])
    
#ADD CODE: print lists
print(fare_survived)

print(headers)
print(fare_not_survived)