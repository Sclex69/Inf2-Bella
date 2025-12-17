import numpy as np
import matplotlib.pyplot as plt
from skimage import io, filters, morphology



def gaussian(x):
    """
    Apply a 3×3 Gaussian-like smoothing filter to a flattened neighborhood.

    The kernel used corresponds to:
        [1 2 1]
        [2 4 2]  * (1 / 16)
        [1 2 1]

    Parameters
    ----------
    x : numpy.ndarray
        A 1D array of length 9 representing a flattened 3×3 pixel neighborhood.

    Returns
    -------
    float
        The filtered pixel value after applying the Gaussian kernel.
    """
    c=x[0]+ x[2]+x[6]+ x[8]+2*x[1]+2*x[3]+2*x[5]+2*x[7]+4*x[4]
    c=c/16
    return c

def median(x):
    """
    Apply a median filter to a flattened 3×3 neighborhood.

    Parameters
    ----------
    x : numpy.ndarray
        A 1D array of length 9 representing a flattened 3×3 pixel neighborhood.

    Returns
    -------
    float
        The median value of the neighborhood.
    """
    c=np.median(x)
    return c

def apply_filter(img,filter_fn):
    """
    Apply a given filter function to a 2D image using a sliding 3×3 window.

    Border pixels are ignored to avoid boundary issues.

    Parameters
    ----------
    img : numpy.ndarray
        A 2D grayscale image.
    filter_fn : callable
        A function that takes a flattened 3×3 neighborhood (length 9)
        and returns a single filtered value.

    Returns
    -------
    numpy.ndarray
        The filtered image.
    """
    h, w = img.shape
    out = np.zeros_like(img)

    # avoid borders
    for i in range(1, h-1):
        for j in range(1, w-1):
            window = img[i-1:i+2, j-1:j+2].flatten()
            out[i, j] = filter_fn(window)

    return out

# Create an image with a single bright pixel
single_dot = np.zeros((20, 20))
single_dot[10, 10] = 1

# Create an image with random noise
random_dots = np.random.random((20, 20))

# Apply filters to the single-dot image
single_dot_gauss = apply_filter(single_dot, gaussian)
single_dot_median = apply_filter(single_dot, median)

# Apply filters to the random noise image
random_dots_gauss = apply_filter(random_dots, gaussian)
random_dots_median = apply_filter(random_dots, median)

# Loading image and applying filters
img=io.imread("46658_784_B12_1.tif",as_gray=True)
sk_gauss = filters.gaussian(img, sigma=1)
sk_median = filters.median(img, morphology.footprint_rectangle((3, 3)))




my_gauss = apply_filter(img, gaussian)
my_median = apply_filter(img, median)


# Create a grid of plots for visualization
fig, axs = plt.subplots(4, 3, figsize=(9, 6))

axs[0,0].imshow(single_dot, cmap='gray')
axs[0,0].set_title("Single dot")

axs[0,1].imshow(single_dot_gauss, cmap='gray')
axs[0,1].set_title("Gaussian")

axs[0,2].imshow(single_dot_median, cmap='gray')
axs[0,2].set_title("Median")

axs[1,0].imshow(random_dots, cmap='gray')
axs[1,0].set_title("Random dots")

axs[1,1].imshow(random_dots_gauss, cmap='gray')
axs[1,1].set_title("Gaussian")

axs[1,2].imshow(random_dots_median, cmap='gray')
axs[1,2].set_title("Median")

axs[2,0].imshow(my_gauss, cmap='gray')
axs[2,0].set_title("Image(my gaussian filter)")

axs[2,1].imshow( my_median, cmap='gray')
axs[2,1].set_title("Image(my median filter)")

axs[3,0].imshow(sk_gauss, cmap='gray')
axs[3,0].set_title("Image(real gaussian filter)")

axs[3,1].imshow(sk_median, cmap='gray')
axs[3,1].set_title("Image(real median filter)")


# Remove axis ticks for clarity
for ax in axs.flat:
    ax.axis("off")

plt.tight_layout()
plt.show()
