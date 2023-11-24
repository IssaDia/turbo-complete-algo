import cv2
from sklearn.cluster import KMeans
import numpy as np
from webcolors import rgb_to_name

def analyze_dominant_color(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Reshape the image to be a list of pixels
    pixels = img.reshape((-1, 3))

    # Apply k-means clustering to find the dominant color
    kmeans = KMeans(n_clusters=1, n_init=10)
    kmeans.fit(pixels)

    # Get the dominant color
    dominant_color = kmeans.cluster_centers_.astype(int)[0]

    try:
        # Get the color name
        color_name = rgb_to_name(dominant_color, spec="css3")
        return color_name
    except ValueError:
        return "Unknown"
