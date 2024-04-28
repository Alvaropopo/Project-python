import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import pandas as pd

datafifaplayer= pd.read_csv("players_22.csv")
print(datafifaplayer.head())

print(datafifaplayer.shape)

print(datafifaplayer["nationality_name"].value_counts()[0:10])

print((datafifaplayer["nationality_name"]=="Papua New Guinea").value_counts())

# plt.figure(figsize=(8,5))
# plt.bar(list(datafifaplayer["nationality_name"].value_counts()[0:5].keys()),list(datafifaplayer["nationality_name"].value_counts()[0:5]),color="r")
# plt.show()

# datawageplayer=datafifaplayer[["short_name","wage_eur"]]
# print(datawageplayer.sort_values(by=["wage_eur"],ascending=True).head(10))

# datawageplayer=datafifaplayer[["short_name","height_cm"]]
# print(datawageplayer.sort_values(by=["height_cm"],ascending=True).head(10))

# datawageplayer=datafifaplayer[["short_name","weight_kg"]]
# print(datawageplayer.sort_values(by=["weight_kg"],ascending=False).head(10))

# datawageplayer=datafifaplayer[["short_name","shooting"]]
# print(datawageplayer.sort_values(by=["shooting"],ascending=True).head(10))

Manchesterunited=datafifaplayer[datafifaplayer["club_name"]=="Manchester United"]
datawageplayermu=Manchesterunited[["short_name","wage_eur"]]
print(datawageplayermu.sort_values(by=["wage_eur"],ascending=True).head(10))
# print(datafifaplayer["club_name"].value_counts().tail())