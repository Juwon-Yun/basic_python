import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day11.dao_stock import DaoStock
 
ds = DaoStock()

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

xs = [0,0,0,0,0 ,0,0,0,0,0]
xy = [0,1,2,3,4 ,5,6,7,8,9]
zs = ds.mySamsung("삼성전자")

ax.plot(xs, xy, zs);

plt.show()