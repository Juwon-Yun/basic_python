import pandas as pd #exel 데이터 불러올 때
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
 

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
#ax.plot([0,0],[0,2],[0,0],'r') 

#ax.plot([1,1],[0,2],[0,0],'g') 
# 떠있는 이유 auto 스케일

ax.plot([0,0,0],[0,1,2],[0,0.1,0],'b') 
ax.plot([1,1,1],[0,1,2],[0,-0.1,0],'b') 

#0,0,0 0,2,0 
#1,0,0 1,2,0 

# ax.set_xlim3d(-5, 5)
#
# ax.set_ylim3d(-5, 5)
#
# ax.set_zlim3d(-5, 5)
plt.show()