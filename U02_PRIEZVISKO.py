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

def crop(img, r_start, r_end, c_start, c_end):
    """
    Crop an image to a selected rectangular region.

    Parameters
    ----------
    img : numpy.ndarray
        Input image.
    r_start, r_end : int
        Start and end row indices.
    c_start, c_end : int
        Start and end column indices.

    Returns
    -------
    numpy.ndarray
        Cropped image.
    """
    return img[r_start:r_end, c_start:c_end]



def thresholding(img, threshold):
    """
    Perform threshold segmentation on a grayscale image.

    Parameters
    ----------
    img : numpy.ndarray
        Grayscale image.
    threshold : float
        Threshold value (0–1).

    Returns
    -------
    numpy.ndarray
        Binary image.
    """
    return (img > threshold).astype(np.uint8)

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





# Loading image and applying filters
img=io.imread("Sahur2.webp",as_gray=True)
sk_gauss = filters.gaussian(img, sigma=1)
sk_median = filters.median(img, morphology.footprint_rectangle((3, 3)))

cropped_img = crop(img, 40, 60, 50, 250)
thresh_img = thresholding(img, 0.5)



my_gauss = apply_filter(img, gaussian)
my_median = apply_filter(img, median)


# Create a grid of plots for visualization
fig, axs = plt.subplots(2, 3, figsize=(12, 6))

axs[0,0].imshow(img, cmap='gray')
axs[0,0].set_title("Original")

axs[0,1].imshow(cropped_img, cmap='gray')
axs[0,1].set_title("Cropped")

axs[0,2].imshow(thresh_img, cmap='gray')
axs[0,2].set_title("Thresholded")

axs[1,0].imshow(my_gauss, cmap='gray')
axs[1,0].set_title("My Gaussian")

axs[1,1].imshow(my_median, cmap='gray')
axs[1,1].set_title("My Median")

for ax in axs.flat:
    ax.axis("off")



plt.tight_layout()
plt.show()
