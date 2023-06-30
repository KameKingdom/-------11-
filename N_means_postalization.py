import cv2
import numpy as np
import random

def kmeans(X, n_clusters, random_state=0, max_iter=300):
    random.seed(random_state)
    centers = X[random.sample(range(X.shape[0]), n_clusters)]
    for _ in range(max_iter):
        labels = np.argmin(np.linalg.norm(X[:, np.newaxis] - centers, axis=-1), axis=-1)
        new_centers = np.array([np.mean(X[labels == i], axis=0) for i in range(n_clusters)])
        if np.all(centers == new_centers):
            break
        centers = new_centers
    return labels, centers

def posterize_image(image_path, n_colors):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    pixels = img.reshape(-1, 3)
    labels, centers = kmeans(pixels, n_clusters=n_colors, random_state=0)

    new_pixels = centers[labels].astype(int)
    new_img = new_pixels.reshape(img.shape)

    new_img = cv2.cvtColor(new_img, cv2.COLOR_RGB2BGR)
    cv2.imshow('Posterized image', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'C:\\Users\\yudai\\Pictures\\gogh.jpg'
posterize_image(image_path, 2)
