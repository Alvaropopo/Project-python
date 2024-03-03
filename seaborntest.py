import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

sb.set()
# x=np.linspace(0,10,1000)
# plt.plot(x,np.sin(x),x,np.cos(x))
# plt.show()

datatips=sb.load_dataset("tips")
sb.relplot(x="total_bill",y="tip",data=datatips,kind="scatter",hue="time",col="sex")
plt.show()