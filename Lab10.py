
import matplotlib.pyplot as plt
import numpy as np

from skimage import io
from skimage.draw import ellipse
from skimage.measure import label, regionprops, regionprops_table
from skimage.transform import rotate
#%%
# Load and diplay the url image by skimage.io
BC = io.imread("https://upload.wikimedia.org/wikipedia/commons/8/82/SEM_blood_cells.jpg")
io.imshow(BC)
io.show()

#%%

# Thresholding:
reddish = BC[:, :, 0] > 160
BC[reddish] = [200, 0, 0]
plt.imshow(BC)
#%%

label_img = label(BC)
regions = regionprops(label_img)

#%%
