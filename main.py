import os
import random
from PIL import Image

def flip_image(image, axis):
    if axis == 'x':
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    elif axis == 'y':
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        return image

def combine_images(folder_path, output_path):
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
    full_image = Image.new('RGB', (2 * width, 2 * height))

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
    print(f"Full image created and saved as {output_path}")


if __name__ == "__main__":
    # Set the folder path where the quadrant images are located
    folder_path = './ai_images'


    # Set the output path for the full image
    output_path = './result/'

    # Generate stimuli
    for i in range(100):
        combine_images(folder_path, output_path)
