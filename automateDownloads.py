import os
import shutil
import logging

logging.basicConfig(level=logging.INFO)

def move_file_to_folder(file_path, folder_name, base_path):
    """Move a file to a specific folder, creating the folder if it doesn't exist."""
    folder_path = os.path.join(base_path, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    try:
        shutil.move(file_path, os.path.join(folder_path, os.path.basename(file_path)))
        return True
    except (shutil.Error, FileNotFoundError, PermissionError) as e:  # Handle specific exceptions
        logging.error(f"Error moving {file_path} to {folder_name}. Reason: {e}")
        return False

def organize_folder(dir_path, folders):
    """Organize files in the specified directory based on the given folders mapping."""
    moved_count = 0
    queue = [dir_path]

    while queue:
        current_path = queue.pop()
        try:
            items = os.listdir(current_path)
        except PermissionError as e:  # Handle permission error
            logging.error(f"Cannot access {current_path}. Reason: {e}")
            continue

        for item_name in items:
            item_path = os.path.join(current_path, item_name)

            # If it's a directory, add to the queue
            if os.path.isdir(item_path):
                queue.append(item_path)
                continue

            file_ext = os.path.splitext(item_name)[1].lower()
            has_moved = False

            for folder, extensions in folders.items():
                if file_ext in extensions:
                    if move_file_to_folder(item_path, folder, dir_path):
                        has_moved = True
                        moved_count += 1
                    break

            if not has_moved:
                if move_file_to_folder(item_path, 'Others', dir_path):
                    moved_count += 1

    return moved_count

def main(target_folder):
    folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.heif'],
        'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.txt', '.md'],
        'Audio': ['.mp3', '.wav', '.m4a', '.flac', '.aac'],
        'Video': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    }

    # Convert extensions to lowercase for case-insensitive check
    folders = {folder: [ext.lower() for ext in extensions] for folder, extensions in folders.items()}

    moved_files = organize_folder(target_folder, folders)
    logging.info(f"{moved_files} files have been organized.")

if __name__ == "__main__":
    directory_to_organize = input("Enter the path of the directory to organize (default is Downloads): ")
    if not directory_to_organize:
        directory_to_organize = os.path.expanduser("~/Downloads")
    main(directory_to_organize)
