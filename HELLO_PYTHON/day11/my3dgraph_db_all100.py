import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day11.dao_stock import DaoStock
import numpy as np


ds = DaoStock()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
xs=np.zeros(10)

ys=range(10) 
 
# s_names = ["삼성전자", "LG전자", "SK"]
s_names = ds.getAllNames()

zs = []

for n in s_names:
    zs.append(ds.mySelect100n(n))
    
# zs.append(ds.mySamsung("삼성전자"))
# zs.append(ds.mySamsung("LG전자"))
# zs.append(ds.mySamsung("SK"))

for idx, z in enumerate(zs):
    ax.plot(xs+idx, ys, z)
    
# ax.plot(xs+0, ys, zs[0])
# ax.plot(xs+1, ys, zs[1])
# ax.plot(xs+2, ys, zs[2])


plt.show()

 
