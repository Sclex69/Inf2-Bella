import numpy as np
import matplotlib.pyplot as plt
import skimage
import skimage.io
import skimage.morphology
from skimage import io
import skimage.filters



# Load image---------------------

# Read a multi-channel TIFF image into a NumPy array
image_stack = skimage.io.imread('46658_784_B12_1.tif')

# Store the shape of the image (height, width, channels)
f = image_stack.shape



# Display original image-----------------------

plt.subplots(figsize=(10, 10))
plt.imshow(image_stack)
plt.title("Original image stack")



# Extract and visualize nuclei channel----------------------

# Extract the nuclei channel (channel index 2)
image_nuclei = image_stack[:, :, 2]

plt.subplots(figsize=(10, 10))
plt.imshow(image_nuclei, cmap='gray')
plt.title("Nuclei channel")



# Histogram and Otsu thresholding for nuclei--------------------

# Plot histogram of pixel intensities in the nuclei channel
plt.hist(np.ravel(image_nuclei))
plt.title("Histogram of nuclei intensities")

# Compute Otsu threshold for nuclei
my_otsu_threshold = skimage.filters.threshold_otsu(image_nuclei)
print(my_otsu_threshold)

# Create a binary mask for nuclei
mask_nuclei = image_nuclei > my_otsu_threshold

plt.imshow(mask_nuclei, cmap='gray')
plt.title("Nuclei mask (Otsu threshold)")



# Extract and visualize cell channel--------------

# Extract the cell channel (channel index 0)
image_cells = image_stack[:, :, 0]

plt.subplots(figsize=(10, 10))
plt.imshow(image_cells, cmap='gray')
plt.title("Cell channel")



# Otsu thresholding for cells---------------

# Create a binary mask for cells using Otsu threshold
mask_cells = image_cells > skimage.filters.threshold_otsu(image_cells)

plt.subplots(figsize=(10, 10))
plt.imshow(mask_cells, cmap='gray')
plt.title("Cell mask (Otsu threshold)")



# Combine masks-----------------

# Combine cell and nuclei masks to get overlapping regions
both_masks = mask_cells * mask_nuclei

plt.subplots(figsize=(10, 10))
plt.imshow(both_masks, cmap='gray')
plt.title("Combined cell + nuclei mask")



# Show all plots
plt.show()
