pip install scikit-image
from skimage import io, filters
from matplotlib import pyplot as plt

img = io.imread('home/Bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')
gaussian_img = filters.gaussian(img, sigma=2)
plt.show(gaussian_img)