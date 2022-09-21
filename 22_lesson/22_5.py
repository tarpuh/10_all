from PIL import Image


def makeanagliph(filename, delta):
    im = Image.open(filename)
    pixels = im.load()
    x, y = im.size
    newImage = Image.new('RGB', (x, y), (255, 255, 255))
    p = newImage.load()
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            if i - delta >= 0:
                R = pixels[i - delta, j][0]
                p[i, j] = R, g, b
            else:
                p[i, j] = 0, g, b
    newImage.save('res5.jpg')


makeanagliph('im2.jpg', 10)
