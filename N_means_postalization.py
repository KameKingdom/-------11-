import cv2
import numpy as np
from sklearn.cluster import KMeans

def posterize_image(image_path, n_colors):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pixel_array = img.reshape((-1, 3))
    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(pixel_array)
    colors = kmeans.cluster_centers_
    new_pixel_array = np.array([colors[label] for label in kmeans.labels_])
    new_pixel_array = new_pixel_array.astype(np.uint8)
    new_img = new_pixel_array.reshape(img.shape)
    new_img = cv2.cvtColor(new_img, cv2.COLOR_RGB2BGR)
    cv2.imshow('Posterized image', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'C:\\Users\\yudai\\Pictures\\gogh.jpg'
posterize_image(image_path, 2)
