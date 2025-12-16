import numpy as np
import matplotlib.pyplot as plt
import skimage
import skimage.io
import skimage.morphology
from skimage import io
import skimage.filters


image_stack = skimage.io.imread('46658_784_B12_1.tif')
f= image_stack.shape
plt.subplots(figsize=(10,10))
plt.imshow(image_stack)
image_nuclei = image_stack[:,:,2]
plt.subplots(figsize=(10,10))
plt.imshow(image_nuclei, cmap = 'gray')

plt.hist(np.ravel(image_nuclei))
my_otsu_threshold = skimage.filters.threshold_otsu(image_nuclei)
print(my_otsu_threshold)
mask_nuclei = image_nuclei > my_otsu_threshold
plt.imshow(mask_nuclei, cmap = 'gray')

image_cells = image_stack[:,:,0]
plt.subplots(figsize=(10,10))
plt.imshow(image_cells, cmap = 'gray')
mask_cells = image_cells > skimage.filters.threshold_otsu(image_cells)
plt.subplots(figsize=(10,10))
plt.imshow(mask_cells, cmap = 'gray')
both_masks = mask_cells * mask_nuclei
plt.subplots(figsize=(10,10))
plt.imshow(both_masks, cmap = 'gray');

plt.show()