from PIL import Image, ImageFilter

im = Image.open('img7.jpg')
im_r = im.rotate(270)
im_r_b = im_r.filter(ImageFilter.GaussianBlur(radius=int(input())))
im_r_b.save('res7.jpg')
