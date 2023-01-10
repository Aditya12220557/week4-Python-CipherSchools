# installation of pillow library
# change the image extension
# resize image files
# resize  multiple images using loop
# sharpness
# brightness
# color
# contrast
# image blur , gaussianblur

from PIL import Image, ImageEnhance,ImageFilter
import os

# img1 = Image.open('dog1.jpg')
# img1.save('dog1.pdf')
# img1.show()
# 250
# MAX_SIZE = (250,250)
# img1.thumbnail(MAX_SIZE)
# img1.save('dog1small.jpg')

# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename,extension = os.path.splitext(item)
#         img1.save(f'{filename}.png')
# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(5).save('dog1edited.jpg')
# 0:blurry
# 1:original image
# 2:image with increased sharpness


# ------color------------
img1 = Image.open('dog1.jpg')
enhancer = ImageEnhance.Color(img1)
enhancer.enhance(2).save('dog1edited.jpg')

# ------brightness------------
img1 = Image.open('dog1.jpg')
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(2).save('dog1edited.jpg')

# ------contrast------------
img1 = Image.open('dog1.jpg')
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(5).save('dog1edited.jpg')

# image blur

img1.filter(ImageEnhance.GaussianBlur(radius=2)).save('dog1edited.jpg')








