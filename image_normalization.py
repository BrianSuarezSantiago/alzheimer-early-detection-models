# Imports the 'Image' module from the 'PIL' library for image processing
from PIL import Image

# Imports the 'os' module to interact with the file system
import os

def normalize_images(input_dir, output_dir, size):
    """
    Normalizes the size of images in a directory.

    Args:
        input_dir (str): Path to the input directory containing the original images.
        output_dir (str): Path to the output directory where the normalized images will be saved.
        size (tuple): Target size to resize the images to (width, height).
    """
    # Creates the output directory if it does not already exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterates through all files in the input directory
    for file_name in os.listdir(input_dir):
        # Builds the full path to the input file
        input_path = os.path.join(input_dir, file_name)

        # Checks if the file is an image
        try:
            # Opens the file as an image using the 'PIL' library
            with Image.open(input_path) as img:
                # Converts the image to RGB format (in case it is in another mode like 'P' or 'L')
                img = img.convert("RGB")

                # Resizes the image to the specified size
                img_resized = img.resize(size, Image.Resampling.LANCZOS)

                # Builds the full path to the output file
                output_path = os.path.join(output_dir, file_name)

                # Saves the resized image to the output directory
                img_resized.save(output_path)

                # Prints a success message for the processed image
                print(f"Image normalized and saved to: {output_path}")
        except Exception as e:
            # Prints an error message if the file could not be processed
            print(f"Error processing file {file_name}: {e}")

if __name__ == "__main__":
    # Configures the script: Gathers input from the user
    input_directory = input("Enter the path to the input directory: ")
    output_directory = input("Enter the path to the output directory (will be created if it does not exist): ")
    width = int(input("Enter the desired width for the images: "))
    height = int(input("Enter the desired height for the images: "))

    # Calls the function to normalize images
    normalize_images(input_directory, output_directory, (width, height))
