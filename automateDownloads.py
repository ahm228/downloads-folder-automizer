import os
import shutil
import logging

#Set up logging with a basic configuration to show INFO level logs
logging.basicConfig(level=logging.INFO)

#Move a file to a specific folder, creating the folder if it doesn't exist.
def moveFileToFolder(filePath, folderName, basePath):
    folderPath = os.path.join(basePath, folderName) #Construct the destination folder path

    #Create the destination folder if it doesn't exist
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

    try:
        shutil.move(filePath, os.path.join(folderPath, os.path.basename(filePath))) #Move the file to the destination folder
        return True
    except shutil.Error as e:
        logging.error(f"Error moving {filePath} to {folderName}. Reason: {e}") #Log an error message if there's a problem with the move operation
        return False

#Organize files in the specified directory based on the given folders mapping.
def organizeFolder(dirPath, folders):
    movedCount = 0    #Keep track of how many files were moved
    queue = [dirPath]

    #Process each directory in the queue
    while queue:
        currentPath = queue.pop()
        for itemName in os.listdir(currentPath):
            itemPath = os.path.join(currentPath, itemName)

            #If it's a directory, add to the queue
            if os.path.isdir(itemPath):
                queue.append(itemPath)
                continue

            #Extract the file extension from the filename
            fileExt = os.path.splitext(itemName)[1].lower()
            hasMoved = False

            #Check if the file extension matches any of the predefined categories
            for folder, extensions in folders.items():
                if fileExt in extensions:
                    if moveFileToFolder(itemPath, folder, dirPath): #Move the file to the appropriate folder
                        hasMoved = True
                        movedCount += 1
                    break

            #If the file didn't match any category, move it to the 'Others' folder
            if not hasMoved:
                if moveFileToFolder(itemPath, 'Others', dirPath):
                    movedCount += 1

    return movedCount

def main(targetFolder):
    folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.heif'],
        'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.txt', '.md'],
        'Audio': ['.mp3', '.wav', '.m4a', '.flac', '.aac'],
        'Video': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    }

    #Convert extensions to lowercase for case-insensitive check
    for folder, extensions in folders.items():
        folders[folder] = [ext.lower() for ext in extensions]

    #Organize the directory and log the results
    movedFiles = organizeFolder(targetFolder, folders)
    logging.info(f"{movedFiles} files have been organized.")

if __name__ == "__main__":
    directoryToOrganize = input("Enter the path of the directory to organize (default is Downloads): ")

    if not directoryToOrganize:
        directoryToOrganize = os.path.expanduser("~/Downloads")
        
    main(directoryToOrganize)
