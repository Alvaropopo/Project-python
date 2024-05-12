import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data=pd.read_csv("Covid Data.csv")

print(data.info())
date=data.DATE_DIED.str.split("/",expand=True)
print(date)
data["year"]=date[2]
data["month"]=date[1]
data["day"]=date[0]
print(data.SEX.value_counts())
data.dropna(inplace=True)
data["year"]=pd.to_numeric(data.year)
data["month"]=pd.to_numeric(data.month)
data["day"]=pd.to_numeric(data.day)
print(data.info())
print(data.SEX.value_counts())

# data.sort_values(by="DATE_DIED").DATE_DIED.value_counts(sort=False)[1:10].plot(kind="line")
# plt.show()
# print(data.DATE_DIED.nunique())
# ndeath=data.DATE_DIED.value_counts()
# ndeath=pd.DataFrame(ndeath)
# print(ndeath.info())
# plt.figure(figsize=(16,8))
# sb.lineplot(x=data.DATE_DIED,y=data.USMER)
# plt.title("number of daily severity level")
# plt.show()

# plt.figure(figsize=(16,8))
# sb.lineplot(data=data.DATE_DIED.nunique(),x=data.DATE_DIED.unique())
# plt.title("number of daily death rate level")
# plt.show()