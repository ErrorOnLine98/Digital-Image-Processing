##########################################################################################################################
# Adam King                                                                                                              #
# CS 4410                                                                                                                #
# Last Updated: 11/11/2021                                                                                               #
##########################################################################################################################
# Applies a log transformation to an image to expand the values of dark pixels while compressing the higher-level values #
##########################################################################################################################

import math
from PIL import Image


def log_equation(c, r):
    s = c * math.log(float(1 + r), 10)
    return s


def log_transform(image):
    img = image
    in_pixel_val = 255
    out_pixel_val = 255
    c = out_pixel_val / math.log(in_pixel_val + 1, 10)

    for i in range(0, img.size[0] - 1):
        for j in range(0, img.size[1] - 1):
            p = img.getpixel((i, j))

            # Apply the log transform equation to RGB values
            red = round(log_equation(c, p[0]))
            green = round(log_equation(c, p[1]))
            blue = round(log_equation(c, p[2]))

            # Apply to the pixel
            img.putpixel((i, j), (red, green, blue))

    return img


def main():
    # Show original image then show the image after applying log_transform
    image = Image.open('Img3-8a.png')
    image.show()
    log_transform(image).show()


if __name__ == "__main__":
    main()
