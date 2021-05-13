from PIL import Image
import numpy as np


# Gray-scale values from http://paulbourke.net/dataformats/asciiart/
g_scale_1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "       # 70 levels
g_scale_2 = " .:-=+*#%@"[::-1]                                                             # 10 levels


def get_avg(image):   # returns average of grays-scale value of image

    im = np.array(image)
    width, height = im.shape
    return np.average(im.reshape(width * height))     # 1-D average of im array of dimensions 1 x (w*h)


def convert_to_ascii(filename, columns, scale, more_levels, reverse, map_scale=g_scale_2):
    img = Image.open(filename).convert('L')            # saves RGB brightness values of image

    width, height = img.size[0], img.size[1]                    # width and height of image
    print("Input image dimensions: ", width, ' x', height)

    tile_width, tile_height = width / columns, (width / columns) * scale
    rows = int(height / tile_height)
    print("Columns: ", columns, "Rows: ", rows,'\nTile dimensions: ', tile_width, 'x ', tile_height)

    if columns > width or rows > height:
        print("Image too small for specified columns.")
        exit(0)

    if more_levels:
        map_scale = g_scale_1[0::]

    if reverse:
        map_scale = map_scale[::-1]

    ascii_image = []
    for j in range(rows):
        y_1 = int(j * tile_height)
        y_2 = int((j + 1)*tile_height)
        if j == rows - 1:
            y_2 = height
        ascii_image.append("")
        for i in range(columns):
            x_1 = int(i * tile_width)
            x_2 = int((i + 1) * tile_width)
            if i == columns - 1:
                x_2 = width
            img_crop = img.crop((x_1, y_1, x_2, y_2))
            avg = int(get_avg(img_crop))

            gs_val = map_scale[int(avg * (len(map_scale) - 1) / 255)]

            ascii_image[j] += gs_val

    return ascii_image

