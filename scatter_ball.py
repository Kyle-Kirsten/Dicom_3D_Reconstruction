import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义球体的半径和体素分辨率
radius = 1.0
resolution = 32

# 生成体素网格
x = np.linspace(-radius, radius, resolution)
y = np.linspace(-radius, radius, resolution)
z = np.linspace(-radius, radius, resolution)

voxel_grid = np.zeros((resolution, resolution, resolution), dtype=int)

for i in range(resolution):
    for j in range(resolution):
        for k in range(resolution):
            if x[i]**2 + y[j]**2 + z[k]**2 <= radius**2:
                voxel_grid[i, j, k] = 1

np.save('sphere.npy', voxel_grid)

# 绘制体素网格
# 太慢了！！！
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# for i in range(resolution):
#     for j in range(resolution):
#         for k in range(resolution):
#             if voxel_grid[i, j, k] == 1:
#                 ax.scatter(x[i], y[j], z[k], color='b')
#
# # 设置坐标轴标签
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
#
# # 设置图形标题
# plt.title('Voxel Grid Representation of a Sphere')
#
# # 显示图形
# plt.show()
