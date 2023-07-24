"""
This script creates image collages from randomly selected images in a given folder.
The collages are created by flipping and combining four images.
The script then generates different color variations (red, green, white) of these collages,
where the color change applies only to the non-transparent parts of the image.
"""

import os
import random
from PIL import Image

def flip_image(image, axis):
    """
    Flip an image along the specified axis.

    Parameters:
    image (PIL.Image): The original image.
    axis (str): The axis along which to flip the image ('x', 'y', or 'both').

    Returns:
    PIL.Image: The flipped image.
    """
    if axis == 'x':
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    elif axis == 'y':
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        return image

def colorize_image(image_path, color):
    """
    Change the color of non-transparent parts of an image.

    Parameters:
    image_path (str): Path to the original image.
    color (tuple): RGB color tuple for the new color.

    Returns:
    str: Path to the saved colorized image.
    """
    image = Image.open(image_path)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            current_color = image.getpixel((x, y))
            if current_color[3] != 0:  # Check if the pixel is not fully transparent
                new_color = (*color, current_color[3])  # Keep the original alpha value
                image.putpixel((x, y), new_color)

    colorized_output_path = os.path.splitext(image_path)[0] + f'_{color[0]}_{color[1]}_{color[2]}.png'
    image.save(colorized_output_path)

    return colorized_output_path

def combine_images(folder_path, output_path):
    """
    Create a collage by combining four random images from a folder.

    Parameters:
    folder_path (str): Path to the folder containing the images.
    output_path (str): Path to save the collage.

    Returns:
    str: Path to the saved collage.
    """
    image_files = os.listdir(folder_path)
    random_images = random.sample(image_files, 4)

    images = []
    parts_numbers = []
    for image_file in random_images:
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)
        images.append(image)

        # Extract the part number from the image filename
        part_number = os.path.splitext(image_file)[0].split('_')[-1]
        parts_numbers.append(part_number)

    width, height = images[0].size
    full_image = Image.new('RGBA', (2 * width, 2 * height), (0, 0, 0, 0))

    positions = [(0, 0), (width, 0), (0, height), (width, height)]
    flip_axes = [None, 'y', 'x', 'both']
    for image, position, axis in zip(images, positions, flip_axes):
        if axis == 'both':
            image = flip_image(image, 'x')
            image = flip_image(image, 'y')
        else:
            image = flip_image(image, axis)
        full_image.paste(image, position)

    # Create the filename based on the part numbers
    filename = '_'.join(parts_numbers) + '.png'
    output_path = os.path.join(output_path, filename)

    full_image.save(output_path)
    print(f"Collage created and saved as {output_path}")

    return output_path


if __name__ == "__main__":
    # Set the folder path where the quadrant images are located
    folder_path = 'C:/Users/lehma/PycharmProjects/CERAS/imagegenerator/component_folder'
    # Set the output path for the full image
    output_path = 'C:/Users/lehma/PycharmProjects/CERAS/imagegenerator/result'
    # Generate stimuli
    for i in range(20):
        collage_path = combine_images(folder_path, output_path)
        # Generate color variations
        colors = [(224, 76, 76), (94, 224, 76), (255, 255, 255)]  # Red, green, white
        for color in colors:
            colorized_path = colorize_image(collage_path, color)
            print(f'Colorized image saved as {colorized_path}')