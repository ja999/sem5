from skimage import data
from skimage.morphology import disk
from skimage.filter.rank import autolevel, enhance_contrast
# Load test image
ima = data.camera()
# Stretch image contrast locally
auto = enhance_contrast(ima, disk(20))
