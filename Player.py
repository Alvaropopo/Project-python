import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import pandas as pd

datafifaplayer= pd.read_csv("players_22.csv")
print(datafifaplayer.head())

print(datafifaplayer.shape)

print(datafifaplayer["nationality_name"].value_counts()[0:10])

print((datafifaplayer["nationality_name"]=="Papua New Guinea").value_counts())