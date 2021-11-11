#####################################################################################
# Adam King                                                                         #
# CS 4410                                                                           #
# Last Updated: 11/11/2021							                                #
#####################################################################################
# Implements the 3x3 Median Filter to restore a noisy image                         #
#####################################################################################

import numpy as np
from PIL import Image, ImageDraw


def median_filter(image):
    # Convert to grayscale
    img = image.convert('L')

    # Create a new image file to output to
    output_file = Image.new('L', image.size)

    # Draw to output file
    draw_pixel = ImageDraw.Draw(output_file)

    # Calculate offset
    offset = 3 // 2

    # For every pixel, calculate and apply median of 3x3 area
    for i in range(offset, image.size[0] - offset):
        for j in range(offset, image.size[1] - offset):
            grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

            # Acquire the 3x3 neighborhood
            for m in range(len(grid)):
                for n in range(len(grid)):
                    x = i + m - offset
                    y = j + n - offset
                    temp = img.getpixel((x, y))  # pixel intensity at x, y
                    grid[m][n] = temp

            # Calculate median of the 3x3 area
            median = int(np.median(grid))

            # Draw pixel
            draw_pixel.point((i, j), median)

    return output_file


def main():
    image_file = "Fig0507a_salt_and_pepper_noise.png"
    image = Image.open(image_file)
    filtered = median_filter(image)
    filtered.show()
    filtered.save("Fig0507a_median_filtered.png")


if __name__ == "__main__":
    main()
