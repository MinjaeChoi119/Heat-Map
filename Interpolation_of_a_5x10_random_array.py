#5x10난수 배열의 보간

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# 그림 색상 맵과 이미지 원점 설정
plt.rcParams['image.cmap'] = 'jet'
plt.rcParams['image.origin'] = 'lower'

# 5x10 크기의 무작위 2D 배열 생성
raw = np.random.random((5, 10))

# 보간
# 원본 데이터의 그리드 포인트 생성
x, y = np.mgrid[0:raw.shape[0], 0:raw.shape[1]]
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
xy = np.concatenate([x, y], axis=1)

# 보간된 데이터를 위한 그리드 포인트 생성
grid_x, grid_y = np.mgrid[0:4:50j, 0:9:100j]

# 보간 수행
z_l = griddata(xy, raw.ravel(), (grid_x, grid_y), method='linear')
z_n = griddata(xy, raw.ravel(), (grid_x, grid_y), method='cubic')

# 원본 데이터와 보간 결과를 시각화하기 위해 서브플롯 생성
fig, axs = plt.subplots(3, 1, figsize=(5, 8))
axs[0].imshow(raw)
axs[0].set_title('original')
axs[1].imshow(z_l)
axs[1].set_title('linear)')
axs[2].imshow(z_n)
axs[2].set_title('cubic')

# 레이아웃 조정 및 그래프 표시
plt.tight_layout()
plt.show()