#####################################################################################
# Adam King                                                                         #
# CS 4410                                                                           #
# Implements the unsharp masking/high-boost filtering technique to sharpen an image #
#####################################################################################
import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw
# CV2 is only used to read, write, and show images. Everything else is done with PIL and numpy


def averaging_filter(image):
    kernel = np.ones((3, 3)) / 9
    offset = len(kernel) // 2

    # Convert array to PIL image
    pil_img = Image.fromarray(image).convert('RGB')

    # Create a new image to output to
    output_pil_image = Image.new('RGB', pil_img.size)

    # Allow pixels to be drawn
    draw_pixel = ImageDraw.Draw(output_pil_image)

    # Apply mask to image
    for i in range(offset, pil_img.size[0] - offset):
        for j in range(offset, pil_img.size[1] - offset):
            color = np.zeros(3, dtype=int)

            # Apply kernel to each pixel
            for m in range(len(kernel)):
                for n in range(len(kernel)):
                    x = i + m - offset
                    y = j + n - offset
                    r, g, b = pil_img.getpixel((x, y))  # RGB values of pixel at x, y
                    color[0] = round(color[0] + r * kernel[m][n])
                    color[1] = round(color[1] + g * kernel[m][n])
                    color[2] = round(color[2] + b * kernel[m][n])

            # Draw the pixel
            draw_pixel.point((i, j), (color[0], color[1], color[2]))

    # Convert PIL image to array
    output_image = np.array(output_pil_image)

    return output_image


def high_boost_filter(image, amount, threshold=0):
    # Return a sharp version of the image, using an unsharp mask

    # Blur image using an averaging filter
    blurred = averaging_filter(image)

    # Subtract original image from blurred image Amount is listed as a percentage and controls the magnitude of each
    # overshoot (how much darker and how much lighter the edge borders become)
    sharp = float(amount + 1) * image - float(amount) * blurred

    # Calculate using maximum and minimum
    sharp = np.maximum(sharp, np.zeros(sharp.shape))
    sharp = np.minimum(sharp, 255 * np.ones(sharp.shape))
    sharp = sharp.round().astype(np.uint8)

    # Threshold controls the minimal brightness change that will be sharpened or how far apart adjacent tonal values
    # have to be before the filter does anything.
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharp, image, where=low_contrast_mask)

    return sharp


def main():
    image = cv.imread('Fig0340a_dipxe_text.png')
    cv.imshow('Original Image', image)
    amount = 4.5  # Amount controls the magnitude of each overshoot (how much darker and how much lighter the edge
                  # borders become)
    sharpened_image = high_boost_filter(image, amount)
    cv.imshow('Sharpened Image', sharpened_image)
    cv.imwrite('Fig0340a_dipxe_sharpened.png', sharpened_image)


if __name__ == '__main__':
    main()

