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
    full_image = Image.new('RGBA', (2 * width, 2 * height), (0, 0, 0, 0))

    positions = [(0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1)]
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
    return output_path



if __name__ == "__main__":
    # Set the folder path where the quadrant images are located
    folder_path = 'REDACTED'


    # Set the output path for the full image
    output_path = 'REDACTED'

    # Generate stimuli
    # Generate stimuli
    for i in range(20):
        output = combine_images(folder_path, output_path)
        picture = Image.open(output)


        # Get the size of the image
        width, height = picture.size

        # RED IMAGES:
        for x in range(width):
            for y in range(height):
                current_color = picture.getpixel((x, y))
                if current_color[3] != 0:  # Check if the pixel is not fully transparent
                    new_color = (224, 76, 76, current_color[3])  # Keep the original alpha value
                    picture.putpixel((x, y), new_color)

        red_output_path = os.path.splitext(output)[0] + '_red.png'
        picture.save(red_output_path)

        picture = Image.open(output)  # Reset to original image

        # GREEN IMAGES:
        for x in range(width):
            for y in range(height):
                current_color = picture.getpixel((x, y))
                if current_color[3] != 0:  # Check if the pixel is not fully transparent
                    new_color = (94, 224, 76, current_color[3])  # Keep the original alpha value
                    picture.putpixel((x, y), new_color)

        green_output_path = os.path.splitext(output)[0] + '_green.png'
        picture.save(green_output_path)

        picture = Image.open(output)  # Reset to original image

        # WHITE IMAGES:
        for x in range(width):
            for y in range(height):
                current_color = picture.getpixel((x, y))
                if current_color[3] != 0:  # Check if the pixel is not fully transparent
                    new_color = (255, 255, 255, current_color[3])  # Keep the original alpha value
                    picture.putpixel((x, y), new_color)

        white_output_path = os.path.splitext(output)[0] + '_white.png'
        picture.save(white_output_path)

