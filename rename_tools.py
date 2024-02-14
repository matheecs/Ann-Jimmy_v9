import os
from datetime import datetime

topics = ['chongqing', 'foods',  'hangzhou',
          'marriage', 'phd', 'travel', 'xiangyang']

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))


for topic in topics:
    # Directory containing the images
    directory = script_directory + "/images/" + topic

    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Directory {directory} not found.")
        exit(1)

    # Change directory to the target directory
    os.chdir(directory)

    # Get a list of all image files
    image_files = [file for file in os.listdir() if file.lower().endswith(
        ('.jpg', '.JPG', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'))]

    # Loop through all image files
    for file in image_files:
        # Get the latest modified time of the file
        modified_time = os.path.getmtime(file)

        # Format the modified time as YYYYMMDDHHMMSS
        formatted_time = datetime.utcfromtimestamp(
            modified_time).strftime('%Y%m%d%H%M%S')

        # Extract the file extension
        _, extension = os.path.splitext(file)

        # Construct the new filename with modified time and extension
        new_filename = f"{formatted_time}{extension}"

        # Rename the file
        os.rename(file, new_filename)

        print(f"Renamed '{file}' to '{new_filename}'")
