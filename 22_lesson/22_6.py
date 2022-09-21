from PIL import Image


def transparency(filename1, filename2):
    im1 = Image.open(filename1)
    im2 = Image.open(filename2)
    pixels = im1.load()
    pixels2 = im2.load()
    x, y = im1.size
    for i in range(x):
        for j in range(y):
            r1, g1, b1 = pixels[i, j]
            r2, g2, b2 = pixels2[i, j]
            R = int(r1 * 0.5 + 0.5 * r2)
            G = int(g1 * 0.5 + 0.5 * g2)
            B = int(b1 * 0.5 + 0.5 * b2)
            pixels[i, j] = R, G, B
    im1.save('res6.jpg')


transparency('im1.jpg', 'im2.jpg')
