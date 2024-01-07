import csv
with open('premier-league-tables.csv') as i:
  data=csv.reader(i)
  datalist=list(data)
  for row in data:
    print(row)
  totalPts=0
  totalrow=0
  for k in datalist:
    print(k)
    print(k[1])
    if(k[10]=="Pts"):
        continue
    totalPts += int(k[10])
    totalrow+=1
  print(totalPts/totalrow)