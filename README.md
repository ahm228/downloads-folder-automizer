The provided script is a simple utility to organize files in a directory based on their file extensions. The script defines categories like Images, Documents, Audio, and Video, and automatically moves files to their respective folders within the target directory.
Requirements

    Python 3.x

How to Use

    Run the script by using the command:
    python automateDownloads.py
    
    When prompted, enter the path of the directory you want to organize. If you don't specify any directory, by default, it will organize the 'Downloads' folder of the user.
    Enter the path of the directory to organize (default is Downloads): [YOUR_DIRECTORY_PATH]

    The script will then process the specified directory and its sub-directories, moving the files to their respective folders based on their file extensions.

    Once done, the script will log the number of files it has organized.

Customization

    You can customize the categories and the file extensions that map to each category:

    In the main() function, the folders dictionary defines the folders and their associated file extensions:
    folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.heif'],
        'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.txt', '.md'],
        'Audio': ['.mp3', '.wav', '.m4a', '.flac', '.aac'],
        'Video': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    }
    You can add or remove entries from this dictionary to customize the behavior of the file organizer.

Note

    Files with extensions not matching any predefined category will be moved to an 'Others' folder.
    The script will also handle the scenario where the target directory or file already exists, logging an error in such cases.