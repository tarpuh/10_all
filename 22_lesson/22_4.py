from PIL import Image, ImageDraw


def gradient(color):
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    col = 0
    for i in range(0, 512, 2):
        if color in 'Rr':
            draw.line((i, 0, i, 200), fill=(col, 0, 0), width=1)
            draw.line((i + 1, 0, i + 1, 200), fill=(col, 0, 0), width=1)

        elif color in 'Gg':
            draw.line((i, 0, i, 200), fill=(0, col, 0), width=1)
            draw.line((i + 1, 0, i + 1, 200), fill=(0, col, 0), width=1)

        elif color in 'Bb':
            draw.line((i, 0, i, 200), fill=(0, 0, col), width=1)
            draw.line((i + 1, 0, i + 1, 200), fill=(0, 0, col), width=1)
        col += 1

    new_image.save('res4.jpg')


gradient('b')
