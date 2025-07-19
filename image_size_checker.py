# Imports the 'Image' module from the 'PIL' library for image processing
from PIL import Image

# Imports the 'os' module to interact with the file system
import os

# Prompts the user to input the path of the directory containing the images
output_directory = input("Enter the path to the directory containing the images: ")

# Checks if the specified directory exists
if not os.path.isdir(output_directory):
    # Displays an error message if the directory does not exist
    print("The specified directory does not exist. Please verify the path.")
else:
    # Iterates through the files in the directory if it exists
    for file_name in os.listdir(output_directory):
        # Builds the full path for the current file
        file_path = os.path.join(output_directory, file_name)
        try:
            # Attempts to open the file as an image using the 'PIL' library
            with Image.open(file_path) as img:
                # Prints the file name and the image size (width and height in pixels)
                print(f"{file_name} - Size: {img.size}")
        except Exception as e:
            # Displays an error message if an error occurs while processing the file
            print(f"Error processing file {file_name}: {e}")
