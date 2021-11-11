###############################################################################
# Adam King                                                                   #
# CS 4410                                                                     #
# Last Updated: 11/11/2021                                                    #
###############################################################################
# This program applies a Power Law translation (Gamma correction) to an image #
###############################################################################

from PIL import Image


# Equation for Power Law Transformation
def power_law_equation(c, r, y = 0.9):
    s = c * float(r ** y)
    return s


# Power Law Transformation  
def power_law_transform(image, c = 1):
    im = image

    for i in range(0, im.size[0]-1):
        for j in range(0, im.size[1]-1):
            r = im.getpixel((i,j))

            # Apply the power law equation to RGB values
            red = round(power_law_equation(c, r[0]))
            green = round(power_law_equation(c, r[1]))
            blue = round(power_law_equation(c, r[2]))

            # Apply to the pixel
            im.putpixel((i, j),(red, green, blue))
            
    return im


def main():
    # Show original image then show the image after applying power_law_transform
    im = Image.open('Img3-8a.png')
    im.show()
    power_law_transform(im).show()


if __name__ == '__main__':
    main()
