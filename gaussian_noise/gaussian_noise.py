#####################################################################################
# Adam King                                                                         #
# CS 4410                                                                           #
# Implements a custom Gaussian Noise Filter to create a noisy image                 #
#####################################################################################

import cv2
import numpy as np


def gaussian_noise(image, mean, variance):
    img = image[..., ::-1] / 255.0

    # Gaussian noise
    # loc = noise mean, scale = variance
    gaussian = np.random.normal(loc=mean, scale=variance, size=img.shape)

    # Gaussian noise overlaid over the image
    noisy_image = np.clip((img + gaussian * 0.2), 0, 1)

    return noisy_image


def main():
    image_path = 'Fig0507a.tif'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    noisy = gaussian_noise(image, 0, 1)
    cv2.imshow('Noisy Image', noisy)
    cv2.imwrite('Fig0507a_gaussian_noise.png', noisy*255)


if __name__ == '__main__':
    main()
