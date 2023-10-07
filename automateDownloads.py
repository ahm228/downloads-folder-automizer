import os
import shutil

# Define the folder to organize
download_folder = os.path.expanduser("~/Downloads")  # Adjust the path to your specific Downloads folder

# Create subfolders
folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.heif'],
    'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.txt', '.md'],
    'Audio': ['.mp3', '.wav', '.m4a', '.flac', '.aac'],
    'Video': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    'Others': []
}

# Create subfolders in the Downloads folder
for folder, extensions in folders.items():
    folder_path = os.path.join(download_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Loop to move files to respective folders
for filename in os.listdir(download_folder):
    if os.path.isfile(os.path.join(download_folder, filename)):
        file_ext = os.path.splitext(filename)[1]

        has_moved = False

        for folder, extensions in folders.items():
            if file_ext in extensions:
                shutil.move(os.path.join(download_folder, filename), os.path.join(download_folder, folder, filename))
                has_moved = True
                break

        if not has_moved:
            shutil.move(os.path.join(download_folder, filename), os.path.join(download_folder, 'Others', filename))

print("Downloads folder organized.")
