import numpy as np
import matplotlib.pyplot as plt
import skimage
import skimage.io
import skimage.morphology

single_dot=np.zeros((20,20))
single_dot[9][9]=1
print(single_dot)
plt.imshow(single_dot, cmap = 'gray')
plt.show()

random_dots=np.random.random((20,20))
plt.imshow(random_dots, cmap = 'gray')
plt.show()