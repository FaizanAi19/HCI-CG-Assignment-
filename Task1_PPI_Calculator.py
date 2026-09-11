import math

# taking input from user
W = int(input("Enter horizontal resolution(pixels): "))
H = int(input("Enter vertical resolution(pixels): "))
D = float(input("Enter physical diagonal size(inches): "))  

# calculate total number of pixels
total_pixels = W * H

# calculate simplifie aspect ratio
gcd = math.gcd(W ,H)
aspect_width = W // gcd
aspect_height = H // gcd

# calculate DPI/PPI
diagonal_pixels = math.sqrt(W**2 + H**2)
DPI = diagonal_pixels / D

# classify the display denisty
if DPI <100:
    category = "Low Density (Standard Monitor)"
elif DPI <=200:
    category = "Medium Density (HD Display)"
else:
    category = "High Density (Retina / Mobile)"

 # Display Results
print("\n--- DISPLAY MATRICES ANALYSIS---")
print(f"Total pixel count : {total_pixels:,} pixels")
print(f"Aspect Ratio : {aspect_width}:{aspect_height}")
print(f"Calculated DPI : {DPI:.2f} DPI")
print(f"Denisty Category : {category}")