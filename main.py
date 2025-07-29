import csv
import numpy as np

with open("tips.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  data_numpy = np.array(data_list)

size=data_numpy[:6]
#print(size)

tips=np.array(data_numpy[:,1],dtype=float)
#print(tips)

bills=np.array(data_numpy[:,0],dtype=float)
#print(bill)

tips_percentage=(tips/bills)*100
#print(tips_percentage)

#print average mean of the bills array
print(f"The average bill amount is ${round(np.mean(bills),2)}")

#print the median of the bills array
print(f"The median bill amount is ${round(np.median(bills),2)}")

#print the smallest and maximum bill amount
print(f"The smallest bill amount is ${round(np.min(bills),2)}")
print(f"The largest bill amount is ${round(np.max(bills),2)}")


