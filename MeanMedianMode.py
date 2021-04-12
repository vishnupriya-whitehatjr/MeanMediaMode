import csv
from collections import Counter

with open ("data.csv",newline="") as f:
  reader = csv.reader(f)
  file_data = list(reader)
file_data.pop(0)

newData = []
for i in range(len(file_data)):
    num = file_data[i][2]
    newData.append(float(num))
n = len(newData)

def mean():
  sum = 0
  for x in newData:
    sum += x 
  mean = sum/n
  print("Mean =",mean,"lbs")

def median():
  newData.sort()
  if n%2 == 0:
    median1 = float(newData[n//2])
    median2 = float(newData[n//2 - 1])
    median = (median1 + median2)/2
  else:
    median = float(newData[n//2])
  print("Median =",str(median),"lbs")

def mode():
  data = Counter(newData)

  modeRange = {"75-85":0,"85-95":0,"95-105":0,"105-115":0,"115-125":0,"125-135":0,"135-145":0,"145-155":0,"155-165":0,"165-175":0}

  for height,occurance in data.items():
    if 75 < float(height) < 85:
      modeRange["75-85"]+=occurance
    elif 85 < float(height) < 95:
      modeRange["85-95"]+=occurance
    elif 95 < float(height) < 105:
      modeRange["95-105"]+=occurance
    elif 105 < float(height) < 115:
      modeRange["105-115"]+=occurance
    elif 115 < float(height) < 125:
      modeRange["115-125"]+=occurance
    elif 125 < float(height) < 135:
      modeRange["125-135"]+=occurance
    elif 135 < float(height) < 145:
      modeRange["135-145"]+=occurance
    elif 145 < float(height) < 155:
      modeRange["145-155"]+=occurance
    elif 155 < float(height) < 165:
      modeRange["155-165"]+=occurance
    elif 165 < float(height) < 175:
      modeRange["165-175"]+=occurance
  mode,modeOccurance = 0,0
  for range,occurance in modeRange.items():
    if occurance > modeOccurance:
      mode,modeOccurance = [int(range.split("-")[0]),int(range.split("-")[1])],occurance
  totalMode = float((mode[0]+mode[1])/2) 
  print("Mode =",totalMode,"lbs")

mean()
median()
mode()