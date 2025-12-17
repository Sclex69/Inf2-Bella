import numpy as np
import matplotlib.pyplot as plt
import skimage
import skimage.morphology
from skimage import io

single_dot=np.zeros((20,20))
single_dot[10][10]=1

plt.imshow(single_dot, cmap = 'gray')
plt.show()

random_dots=np.random.random((20,20))
plt.imshow(random_dots, cmap = 'gray')
plt.show()


def crop_image(image, start_row, end_row, start_col, end_col):
    """
    Crop an image using array indices.

    Args:
        image (ndarray): Input image.
        start_row (int): Starting row index.
        end_row (int): Ending row index.
        start_col (int): Starting column index.
        end_col (int): Ending column index.

    Returns:
        ndarray: Cropped image.
    """
    return image[start_row:end_row, start_col:end_col]


#IMAGE PART ----------

# Load image
image = io.imread("13901.tif")

# Crop image
cropped_image = crop_image(image, 100, 300, 100, 300)
plt.imshow(cropped_image, cmap='gray')
plt.show()

# Add number 5 to array
cropped_image_plus_5 = cropped_image + 5

# Plot image
plt.imshow(cropped_image_plus_5, cmap='gray')
plt.show()

