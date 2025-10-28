#5x10난수 배열의 cylinder상 도식화

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D

# matplotlib 설정
plt.rcParams['image.cmap'] = 'jet'
plt.rcParams['image.origin'] = 'lower'

# raw 데이터 생성
raw = np.random.random((5, 10))
data = raw
#data.appdend(raw[])

# x, y 좌표값 생성
x, y = np.mgrid[0:raw.shape[0], 0:raw.shape[1]]
xy = np.concatenate([x.reshape(-1, 1), y.reshape(-1, 1)], axis=1)

# 그리드 생성
grid_x, grid_y = np.mgrid[0:4:100j, 0:9:200j]

# 선형 보간법으로 그리드 데이터 생성
z_l = griddata(xy, raw.ravel(), (grid_x, grid_y), method='linear')

# 3차원 보간법으로 그리드 데이터 생성
z_n = griddata(xy, raw.ravel(), (grid_x, grid_y), method='cubic')

# 실린더 그래프 출력
fig = plt.figure(figsize=(12, 6))

for i, z in enumerate([z_l, z_n]):
    # 3차원 그래프 생성
    ax = fig.add_subplot(121 + i, projection='3d')
    
    # 데이터 산점도 출력
    r=(raw.shape[0]-1)/(np.pi*2)
    deg=grid_x/r
    ax.scatter(np.ravel(grid_y), np.ravel(r*np.cos(deg)), np.ravel(r*np.sin(deg)), cmap='jet', c=np.ravel(z), marker='o' if i == 0 else 's')
    
    # 축 이름 설정
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # 그래프 제목 설정
    ax.set_title('linear' if i == 0 else 'cubic')
    
    # 그래프 시점 설정
    ax.view_init(elev=0, azim=0)
    
    # 축 범위 설정
    ax.set_xlim([0, 9])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])

# 평면 그래프 출력
fig = plt.figure(figsize=(12, 6))

for i, z in enumerate([z_l, z_n]):
    # 3차원 그래프 생성
    ax = fig.add_subplot(121 + i, projection='3d')
    
    # 데이터 산점도 출력
    ax.scatter(np.ravel(grid_y), 0, np.ravel(grid_x), cmap='jet', c=np.ravel(z), marker='o' if i == 0 else 's')
    
    # 축 이름 설정
    ax.set_xlabel('Z')
    ax.set_ylabel('Y')
    ax.set_zlabel('X')
    
    # 그래프 제목 설정
    ax.set_title('linear' if i == 0 else 'cubic')
    
    # 그래프 시점 설정
    ax.view_init(elev=0, azim=0)
    
    # 축 범위 설정
    ax.set_xlim([0, 9])
    ax.set_ylim([-2, 3])
    ax.set_zlim([0, 4])

# 그래프 출력 설정
plt.subplots_adjust(left=0, right=1, bottom=0, top=0.95)

# 그래프 출력
plt.show()
