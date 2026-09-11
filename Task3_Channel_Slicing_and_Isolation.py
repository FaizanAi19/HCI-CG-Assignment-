from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# TASK 3: CHANNEL SLICING & ISOLATION
# --------------------------------------------------

# 1. Load the input image and convert it to NumPy array
image = np.array(Image.open("sample.jpg"))

# 2. Extract individual RGB channels using Axis 2 slicing
red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

# 3. Create separate 3D arrays for each isolated channel

# Red-only image
red_only = np.zeros_like(image)
red_only[:, :, 0] = red

# Green-only image
green_only = np.zeros_like(image)
green_only[:, :, 1] = green

# Blue-only image
blue_only = np.zeros_like(image)
blue_only[:, :, 2] = blue

# --------------------------------------------------
# PRINT CHANNEL EXTRACTION SUMMARY
# --------------------------------------------------

print("--- CHANNEL EXTRACTION SUMMARY ---")

print("Original Image Shape :", image.shape)

print(
    f"Red Channel 2D Shape : {red.shape} | "
    f"Mean Intensity: {red.mean():.2f}"
)

print(
    f"Green Channel 2D Shape : {green.shape} | "
    f"Mean Intensity: {green.mean():.2f}"
)

print(
    f"Blue Channel 2D Shape : {blue.shape} | "
    f"Mean Intensity: {blue.mean():.2f}"
)

print("Display Window : Matplotlib 2x3 Subplot Grid Rendered.")

# --------------------------------------------------
# 4. DISPLAY 2 x 3 SUBPLOT
# --------------------------------------------------

fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# -------- TOP ROW: RGB-ONLY COLOR IMAGES --------

axes[0, 0].imshow(red_only)
axes[0, 0].set_title("Red-Only")

axes[0, 1].imshow(green_only)
axes[0, 1].set_title("Green-Only")

axes[0, 2].imshow(blue_only)
axes[0, 2].set_title("Blue-Only")

# -------- BOTTOM ROW: GRAYSCALE INTENSITY MAPS --------

axes[1, 0].imshow(red, cmap="gray")
axes[1, 0].set_title("Red Intensity")

axes[1, 1].imshow(green, cmap="gray")
axes[1, 1].set_title("Green Intensity")

axes[1, 2].imshow(blue, cmap="gray")
axes[1, 2].set_title("Blue Intensity")

# Remove x and y axes
for ax in axes.flat:
    ax.axis("off")

# Adjust spacing
plt.tight_layout()

# Display figure
plt.show()