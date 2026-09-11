from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# Load image
image = np.array(Image.open("sample.jpg"))

# Step factor
N = 8

# --------------------------------------------------
# 1. DOWNSAMPLE USING NUMPY STRIDING
# --------------------------------------------------

downsampled = image[::N, ::N, :]

# --------------------------------------------------
# 2. RE-EXPAND USING np.repeat()
# --------------------------------------------------

pixelated = np.repeat(
    np.repeat(downsampled, N, axis=0),
    N,
    axis=1
)

# Crop back to original dimensions
pixelated = pixelated[:image.shape[0], :image.shape[1], :]

# --------------------------------------------------
# 3. CALCULATE SPATIAL DIMENSION DROP
# --------------------------------------------------

original_height, original_width, channels = image.shape
down_height, down_width, _ = downsampled.shape

original_spatial_pixels = original_height * original_width
downsampled_spatial_pixels = down_height * down_width

spatial_drop = (
    (original_spatial_pixels - downsampled_spatial_pixels)
    / original_spatial_pixels
) * 100

# --------------------------------------------------
# CALCULATE MEMORY FOOTPRINT DROP
# --------------------------------------------------

original_memory = image.nbytes
downsampled_memory = downsampled.nbytes

memory_drop = (
    (original_memory - downsampled_memory)
    / original_memory
) * 100

# --------------------------------------------------
# PRINT RESULTS
# --------------------------------------------------

print(f"--- DOWNSAMPLING ANALYSIS (N = {N}) ---")

print(
    f"Original Shape : {image.shape} | "
    f"Memory: {original_memory:,} bytes"
)

print(
    f"Downsampled Shape : {downsampled.shape} | "
    f"Memory: {downsampled_memory:,} bytes"
)

print(
    f"Re-expanded Shape : {pixelated.shape} | "
    f"Visual: Blocky Pixelation"
)

print(
    f"Dimension Reduction: "
    f"{spatial_drop:.2f}% reduction per axis"
)

print(
    f"Memory Savings : {memory_drop:.2f}% data reduction"
)

# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Original image
axes[0].imshow(image)
axes[0].set_title("Original Image")
axes[0].axis("off")

# Downsampled image
axes[1].imshow(downsampled)
axes[1].set_title("Downsampled (N=8)")
axes[1].axis("off")

# Pixelated image
axes[2].imshow(pixelated)
axes[2].set_title("Pixelated Image")
axes[2].axis("off")

plt.tight_layout()
plt.show()