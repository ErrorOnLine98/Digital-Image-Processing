##########################################################################################################################
# Adam King														 #
# CS 4410														 #
# Last Updated: 11/11/2021												 #
##########################################################################################################################
# Implements the Laplacian enhancement technique to sharpen an image							 #	
##########################################################################################################################

import numpy as np
from PIL import Image, ImageDraw


def spatial_filter(image, kernel, offset):
    # Convert to Greyscale
    img = image.convert('L')

    # Create a new image to output to
    output_image = Image.new('L', img.size)

    # Allow pixels to be drawn
    draw_pixel = ImageDraw.Draw(output_image)

    # Apply mask to image
    for i in range(offset, img.size[0] - offset):
        for j in range(offset, img.size[1] - offset):
            tmp = 0

            # Apply kernel to each pixel
            for m in range(len(kernel)):
                for n in range(len(kernel)):
                    x = i + m - offset
                    y = j + n - offset
                    luminance = img.getpixel((x, y))  # Luminance value of pixel at x, y
                    tmp = tmp + luminance * kernel[m][n]

            # Draw the pixel
            draw_pixel.point((i, j), tmp)

    return output_image


def laplacian(image, kernel, offset, c):
    im = image

    # Convert to greyscale
    img = image.convert('L')

    # Create a new image to output to
    laplacian_output = Image.new('L', img.size)

    # Allow pixels to be drawn to output
    draw_pixel = ImageDraw.Draw(laplacian_output)

    # Convert image to array
    image_arr = np.array(img)

    # Apply the kernel to image
    laplacian_image = spatial_filter(im, kernel, offset)
    laplacian_arr = np.array(laplacian_image)

    # Add laplacian to original image
    result = image_arr + (c * laplacian_arr)

    # Convert back to an image and draw to output
    result_img = Image.fromarray(result)
    for i in range(0, result_img.width):
        for j in range(0, result_img.height):
            pixel = result_img.getpixel((i, j))
            draw_pixel.point((i, j), pixel)

    return laplacian_output


def main():
    # Original image
    image_file = "Fig0338a_blurry_moon.png"
    image = Image.open(image_file)
    image.show()

    # Laplacian masks
    kernel1 = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]  # c = -1
    kernel2 = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]  # c = -1, includes diagonals

    # Calculate offset
    offset1 = len(kernel1) // 2
    offset2 = len(kernel2) // 2

    # Show laplacian images
    lap1 = spatial_filter(image, kernel1, offset1)
    lap1.save('laplacian_1.png')
    lap1.show()
    lap2 = spatial_filter(image, kernel2, offset2)
    lap2.save('laplacian_2.png')
    lap2.show()

    # Show sharpened images
    sharpened1 = laplacian(image, kernel1, offset1, -1)  # c is 1 or -1 depending on kernel
    sharpened1.save('laplacian_sharp_1.png')
    sharpened1.show()
    sharpened2 = laplacian(image, kernel2, offset2, -1)
    sharpened2.save('laplacian_sharp_2.png')
    sharpened2.show()


main()
