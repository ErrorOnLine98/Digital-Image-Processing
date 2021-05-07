#####################################################################################
# Adam King                                                                         #
# CS 4410                                                                           #
# Implements a Salt and Pepper noise filter to create a noisy image                 #
#####################################################################################

import random

import cv2


def s_and_p_noise(image, salt_amount, pepper_amount):
    # Getting the dimensions of the image
    y, x = image.shape

    # Salt noise component
    # Pick a random number in the weighted amount of pixels
    number_of_pixels = int(x * y * salt_amount)
    for i in range(number_of_pixels):
        # Find a random x coordinate
        x_coord = random.randint(0, x - 1)

        # Find a random y coordinate
        y_coord = random.randint(0, y - 1)

        # Color the pixel white
        image[y_coord][x_coord] = 255

    # Pepper noise component
    # Pick a random number in the weighted amount of pixels
    number_of_pixels = int(x * y * pepper_amount)
    for i in range(number_of_pixels):
        # Pick a random x coordinate
        x_coord = random.randint(0, x - 1)

        # Pick a random y coordinate
        y_coord = random.randint(0, y - 1)

        # Color the pixel black
        image[y_coord][x_coord] = 0

    return image


def main():
    # Read the color image as a grayscale image
    image_file = cv2.imread('Fig0507a.tif', cv2.IMREAD_GRAYSCALE)

    # Add noise and show noisy image
    # Include probabilities of the noise components
    noisy = s_and_p_noise(image_file, 0.2, 0.2)
    cv2.imshow('Noisy Image', noisy)

    # Save the image
    cv2.imwrite('Fig0507a_salt_and_pepper_noise.png', noisy)


if __name__ == '__main__':
    main()
