import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("characters_stats.csv")
good=data[data["Alignment"]=="good"]
bad=data[data["Alignment"]=="bad"]
neutral=data[data["Alignment"]=="neutral"]
print(data.head)

print(data["Alignment"].value_counts())
# print(good.sort_values(by=["Speed"],ascending=False).head(20))
# print(bad.sort_values(by=["Speed"],ascending=False).head(20))

# print(good.sort_values(by=["Speed"]).head(10))
# print(bad.sort_values(by=["Speed"]).head(10))

# print(good.sort_values(by=["Power"],ascending=False).head(20))
# print(bad.sort_values(by=["Power"],ascending=False).head(20))

# print(good.sort_values(by=["Total"],ascending=False).head(20))
# print(bad.sort_values(by=["Total"],ascending=False).head(20))

# print(good.sort_values(by=["Combat"],ascending=False).head(20))
# print(bad.sort_values(by=["Combat"],ascending=False).head(20))
# badtotal= bad.sort_values(by=["Total"],ascending=False)
# plt.figure(figsize=(8,5))
# plt.bar(list(badtotal["Name"])[0:5],list(badtotal["Total"])[0:5])
# plt.show()

# goodtotal= good.sort_values(by=["Total"],ascending=False)
# plt.figure(figsize=(8,5))
# plt.bar(list(goodtotal["Name"])[0:5],list(goodtotal["Total"])[0:5])
# plt.show()

# plt.figure(figsize=(5,7))
# plt.hist(good["Speed"],bins=50)
# plt.title("histogram of heroes speed")
# plt.xlabel("Speed")
# plt.show()

# plt.figure(figsize=(5,7))
# plt.hist(bad["Speed"],bins=50)
# plt.title("histogram of Villains speed")
# plt.xlabel("Speed")
# plt.show()

# plt.figure(figsize=(5,7))
# plt.hist(good["Power"],bins=50)
# plt.title("histogram of Heroes Power")
# plt.xlabel("Power")
# plt.show()

Flashstats=good[good["Name"]=="Flash IV"]
Labels=list(Flashstats.columns.values)
print(Labels)
Labelsname=Labels[2:8]
Flashlist=list(Flashstats.values)
print(Flashlist)
plt.pie(Flashlist[0][2:8],labels=Labelsname)
plt.show()