import pandas as pd #exel 데이터 불러올 때
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day11.dao_stock import DaoStock
 
ds = DaoStock()

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
ay = fig.add_subplot(2,1,1, projection='3d')
ac = fig.add_subplot(3,3,3, projection='3d')
#ax.plot([0,0],[0,2],[0,0],'r') 

#ax.plot([1,1],[0,2],[0,0],'g') 
# 떠있는 이유 auto 스케일

# ax.plot([0,0,0],[0,1,2],[0,0.1,0],'b') 
# ax.plot([1,1,1],[0,1,2],[0,-0.1,0],'b') 
# ax.plot([2,2,2],[0,2,0],[0,0,0],'b') 
# ax.plot([3,3,3],[0,2,0],[0,0.1,0],'b') 

samxs = [0,0,0,0,0 ,0,0,0,0,0]
samxy = [0,1,2,3,4 ,5,6,7,8,9]
samzs = ds.mySamsung("삼성전자")

lgxs = [0,0,0,0,0 ,0,0,0,0,0]
lgxy = [0,1,2,3,4 ,5,6,7,8,9]
lgzs = ds.mySamsung("LG전자우")

skxs = [0,0,0,0,0 ,0,0,0,0,0]
skxy = [0,1,2,3,4 ,5,6,7,8,9]
skzs = ds.mySamsung("SK이노베이션")

#숙제 LG, SK, 삼성 그래프 띄어오기

ax.plot(samxs, samxy, samzs, 'r')
ay.plot(lgxs, lgxy, lgzs, 'b')
ac.plot(skxs, skxy, skzs, 'g')

# ax.set_xlim3d(-10, 150000)
# ax.set_ylim3d(-10, 150000)
# ax.set_zlim3d(-10, 150000)

plt.show()