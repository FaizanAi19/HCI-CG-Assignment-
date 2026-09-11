import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Create a 300 x 400 x 3 image matrix filled with zeros
image = np.zeros((300, 400, 3), dtype=np.uint8)

# Top-Left: Red
image[0:150, 0:200] = [255, 0, 0]

# Top-Right: Green
image[0:150, 200:400] = [0, 255, 0]

# Bottom-Left: Blue
image[150:300, 0:200] = [0, 0, 255]

# Bottom-Right: White
image[150:300, 200:400] = [255, 255, 255]

# Print matrix metrics
print("--- SYNTHETIC MATRIX METRICS ---")
print("Array Shape (H, W, C) :", image.shape)
print("Data Type :", image.dtype)
print("Total Elements :", f"{image.size:,}", "values")
print("Memory Footprint :", f"{image.nbytes:,}", "bytes",
      f"({image.nbytes / 1024:.2f} KB)")

# Display the image
plt.imshow(image)
plt.axis("off")
plt.show()