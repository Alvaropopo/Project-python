import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("suku.csv")
print(data.columns)
# plt.bar(data["Suku"][0:5],data["JumlahPenduduk"][0:5],color=["green","blue","yellow","red","black"])
# plt.show()
# plt.pie(data["JumlahPenduduk"][0:5],labels=data["Suku"][0:5],autopct='%0.1f%%')
# plt.show()
plt.pie(data["JumlahPenduduk"][-11:-1],labels=data["Suku"][-11:-1],autopct='%0.1f%%')
plt.show()