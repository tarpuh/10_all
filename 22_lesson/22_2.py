from PIL import Image


def mirror():
    im = Image.open('img2.jpg')
    pixels = im.load()
    x, y = im.size
    for i in range(x // 2):
        for j in range(y):
            r, g, b = pixels[i, j]
            R, G, B = pixels[x - i - 1, j]
            pixels[i, j] = R, G, B
            pixels[x - i - 1, j] = r, g, b
    im.save('res2.jpg')


mirror()
