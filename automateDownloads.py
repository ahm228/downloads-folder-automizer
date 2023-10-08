import os
import shutil

# Define the folder to organize
download_folder = os.path.expanduser("~/Downloads")

# Extensions to folder mapping
folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.heif'],
    'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.txt', '.md'],
    'Audio': ['.mp3', '.wav', '.m4a', '.flac', '.aac'],
    'Video': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
}

def move_file_to_folder(file_path, folder_name):
    """Move a file to a specific folder, creating the folder if it doesn't exist."""
    folder_path = os.path.join(download_folder, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    try:
        shutil.move(file_path, os.path.join(folder_path, os.path.basename(file_path)))
        return True
    except Exception as e:
        print(f"Error moving {file_path} to {folder_name}. Reason: {e}")
        return False

def organize_folder(dir_path):
    moved_count = 0
    for item_name in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item_name)

        # If it's a directory, recurse into it
        if os.path.isdir(item_path):
            moved_count += organize_folder(item_path)
            continue

        file_ext = os.path.splitext(item_name)[1]
        has_moved = False

        for folder, extensions in folders.items():
            if file_ext in extensions:
                if move_file_to_folder(item_path, folder):
                    has_moved = True
                    moved_count += 1
                break

        if not has_moved:
            if move_file_to_folder(item_path, 'Others'):
                moved_count += 1

    return moved_count

moved_files = organize_folder(download_folder)
print(f"{moved_files} files have been organized.")
