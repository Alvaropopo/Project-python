import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data=pd.read_csv("Covid Data.csv")

print(data.info())

print(data.DATE_DIED.value_counts())
print(data.DATE_DIED.nunique())

# plt.figure(figsize=(16,8))
# sb.lineplot(x=data.DATE_DIED,y=data.USMER)
# plt.title("number of daily severity level")
# plt.show()

plt.figure(figsize=(16,8))
sb.lineplot(data=data.DATE_DIED.nunique(),x=data.DATE_DIED.unique())
plt.title("number of daily death rate level")
plt.show()