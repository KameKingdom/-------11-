import numpy as np
import csv
import random
import matplotlib.pyplot as plt

# クラスタの中心座標
cluster_centers = [(2, 2), (8, 8), (5, 5)]
data_per_cluster = 200  # 1クラスタあたりのデータ数
noise_std = 0.5  # ノイズの標準偏差

# データ生成
data = []
for center in cluster_centers:
    x = np.random.normal(center[0], noise_std, data_per_cluster)
    y = np.random.normal(center[1], noise_std, data_per_cluster)
    cluster_data = np.column_stack((x, y))
    data.append(cluster_data)

# ノイズ生成
noise_num = 50
for _ in range(noise_num):
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)
    noise_data = np.column_stack((x, y))
    data.append(noise_data)

data = np.vstack(data)

# CSVファイルへの書き込み
with open('cluster_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y'])
    writer.writerows(data)

# 二次元分布の表示
plt.scatter(data[:, 0], data[:, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data Distribution')
plt.show()
