"""
Sunset image analysis.
"""

import numpy as np
import imageio
import matplotlib.pyplot as plt

file_name = 'sunset.jpg'

photo_data = imageio.imread(file_name) # Read an image from the specified file


def show_photo(photo_data):    
    plt.figure()
    plt.imshow(photo_data)


def get_statistics(phoo_data):    
    '''Get some statistics about the photo_data.'''
    print(type(photo_data))
    print(photo_data.shape)
    print(photo_data.size)
    print(photo_data.min())
    print(photo_data.max())
    print(photo_data.mean())


def high_magnitude_color(photo_data):
    '''remove all color which magtitude falls below 200'''
    low_value_filter = photo_data < 200
    photo_data[low_value_filter] = 0
    plt.imshow(photo_data)


def low_magnitude_color(photo_data):
    '''remove all color which magtitude falls above 60'''
    low_value_filter = photo_data > 60
    photo_data[low_value_filter] = 0
    plt.imshow(photo_data)


def locate_sun_flare(photo_data):
    red_mask = photo_data[:,:,0] < 200
    photo_data[red_mask] = 0
    plt.imshow(photo_data)
    plt.savefig('sun_flare.png')


def remove_sky(photo_data):
    '''Provided that the sky is comprised of red and blue colors.'''
    red_mask = photo_data[:,:,0] > 100
    blue_mask = photo_data[:,:,2] > 100
    mask = np.logical_or(red_mask, blue_mask)
    photo_data[mask] = 0
    plt.imshow(photo_data)
    plt.savefig('remove_sky.png')


def draw_arch(photo_data, radius=0):
    total_row, total_col, total_layer = photo_data.shape
    x, y = np.ogrid[:total_row, :total_col]
    center_row, center_col = total_row/2, total_col/2
    if radius == 0:
        if total_row > total_col:
            radius = (total_col/2)**2
        else:
            radius = (total_row/2)**2
    else:
        radius = radius**2
    dist_from_center = (x - center_row)**2 + (y - center_col)**2
    circle_mask = dist_from_center > radius
    half_upper_mask = x < center_row
    arch_mask = np.logical_and(circle_mask, half_upper_mask)
    photo_data[arch_mask] = 0
    plt.imshow(photo_data)
    plt.savefig('draw_arch.png')