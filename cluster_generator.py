import numpy as np
import csv

# クラスタの中心座標
cluster_centers = [(2, 2), (8, 8), (5, 5)]

# クラスタごとのデータ数
data_per_cluster = 150

# ノイズの標準偏差
noise_std = 0.3

# データ生成
data = []
for center in cluster_centers:
    x = np.random.normal(center[0], noise_std, data_per_cluster)
    y = np.random.normal(center[1], noise_std, data_per_cluster)
    cluster_data = np.column_stack((x, y))
    data.append(cluster_data)

data = np.vstack(data)

# CSVファイルへの書き込み
with open('cluster_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y'])
    writer.writerows(data)
