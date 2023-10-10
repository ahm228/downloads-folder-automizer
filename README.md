# File Organizer

File Organizer is a simple Python script to automatically organize your files into predefined folders based on their file extensions.

## Features
- Organize files into folders like `Images`, `Documents`, `Audio`, and `Video`.
- Move any other files that do not match predefined categories into the `Others` folder.
- Can handle nested folders and will search through them recursively to organize all files.
- Provides logging capabilities to track files that were moved.

## Requirements

- Python 3.x

## How to Use

1. **Clone the Repository**  
   Clone this repository to your machine or simply download the script.

2. **Run the Script**  
   Navigate to the directory containing the script and run:

   ```bash
   python automateDownloads.py

    Enter the Directory to Organize
    When prompted, enter the full path of the directory you want to organize. If you don't provide a path, by default, it will organize the Downloads folder.

How it Works

The script uses a predefined mapping of folders and their respective file extensions to move files. The current mappings are:

    Images: .jpg, .jpeg, .png, .gif, .tiff, .bmp, .heif
    Documents: .pdf, .docx, .doc, .xlsx, .xls, .pptx, .ppt, .txt, .md
    Audio: .mp3, .wav, .m4a, .flac, .aac
    Video: .mp4, .mov, .avi, .mkv, .flv

Any other file types will be moved to the Others folder.
Customization

To customize which file extensions go into which folders, simply edit the folders dictionary in the main function.