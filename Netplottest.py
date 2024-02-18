import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("suku.csv")
print(data.columns)
plt.bar(data["Suku"],data["JumlahPenduduk"])
plt.show()