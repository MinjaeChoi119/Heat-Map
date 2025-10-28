#5x10 난수배열의 실린더 상 도식화 및 seam 보간

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D

# matplotlib 설정
plt.rcParams['image.cmap'] = 'jet'
plt.rcParams['image.origin'] = 'lower'

# raw 데이터 생성
raw = np.random.random((5,10))

# data 데이터 생성 (raw 데이터의 제일 첫값을 뒤에 붙임)
data=np.concatenate((raw,[raw[0]]))

# x, y 좌표값 생성
x, y = np.mgrid[0:data.shape[0], 0:data.shape[1]]
xy = np.concatenate([x.reshape(-1, 1), y.reshape(-1, 1)], axis=1)

#보간정도 설정
rate=20

# 그리드 생성
grid_x, grid_y = np.mgrid[0:data.shape[0]-1:data.shape[0]*rate*1j, 0:data.shape[1]-1:data.shape[1]*rate*1j]

# 3차원 보간법으로 그리드 데이터 생성
z_n = griddata(xy, data.ravel(), (grid_x, grid_y), method='cubic')
    
# cylider heatmap 출력
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(projection='3d')
        
# 데이터 산점도 출력
r=(data.shape[0]-1)/(np.pi*2) #cylinder radius
deg=(grid_x)/r #r*deg=호의 길이
ax.scatter(np.ravel(grid_y), np.ravel(r*np.cos(deg)), np.ravel(r*np.sin(deg)), cmap='jet', c=np.ravel(z_n)) #(y,z) 1,0에서 시계방향으로그림

# 축 이름 설정
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
    
# 그래프 제목 설정
ax.set_title('cubic')
    
# 그래프 시점 설정
ax.view_init(elev=0, azim=70, roll=0)
    
# 축 범위 설정
ax.set_xlim([0, 9])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

# 그래프 출력 설정
plt.subplots_adjust(left=0, right=1, bottom=0, top=0.95)

# 그래프 출력
plt.show()