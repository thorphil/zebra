import numpy as np
import PIL
import skimage
import skimage.io as skio
import skimage.morphology as morphology
file = '2021-left-sucessful-warp-2.png'
image = skio.imread(file,as_gray=True)

print(image.shape)
# image = np.array(image)
image = image>0.4
diameter = 20
image = morphology.diameter_opening(image,diameter_threshold=10)
image = morphology.diameter_closing(image,diameter_threshold=diameter)
image = skimage.util.invert(image)
skio.imsave('extracted-closed{}.bmp'.format(diameter),image)
# im = PIL.Image.fromarray(image)
# im.show()
#potrace --svg -o polygon.svg extracted-closed20.bmp
