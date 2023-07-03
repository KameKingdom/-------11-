import cv2
import numpy as np
import random

def kmeans(X, n_clusters, random_state=0, max_iter=300):
    random.seed(random_state)

    # ランダムにクラスタの初期中心を選択
    indices = random.sample(range(X.shape[0]), n_clusters)
    centers = X[indices]

    for _ in range(max_iter):
        # 各データ点に対して最も近いクラスタ中心を求める
        distances = np.linalg.norm(X[:, np.newaxis] - centers, axis=-1)
        labels = np.argmin(distances, axis=-1)

        # 新しいクラスタ中心を求める
        new_centers = np.array([np.mean(X[labels == i], axis=0) for i in range(n_clusters)])

        # クラスタ中心が収束したら終了
        if np.all(centers == new_centers):
            break

        centers = new_centers

    return labels, centers

def postalize_image(image_path, n_colors):
    # 画像を読み込む
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 画像のピクセルを1次元配列に変換
    pixels = img.reshape(-1, 3)

    # k-means法でクラスタリングを行う
    labels, centers = kmeans(pixels, n_clusters=n_colors, random_state=0)

    # 各ピクセルを最も近いクラスタ中心の色に置き換える
    new_pixels = centers[labels].astype(int)
    new_img = new_pixels.reshape(img.shape)

    # 画像を表示する
    new_img = cv2.cvtColor(new_img, cv2.COLOR_RGB2BGR)
    cv2.imshow('Posterized image', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'C:\\Users\\yudai\\Pictures\\gogh.jpg'
postalize_image(image_path, 2)
