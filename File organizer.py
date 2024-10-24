import os
import shutil

def organize_files():
    # Get the path to the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Define file types and their corresponding folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.tar', '.rar']
    }
    
    # Create subfolders on the desktop if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(desktop_path, folder)
         if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files from the desktop to the corresponding folder
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)
        if os.path.isfile(file_path):
            moved = False
            print(f"Checking file: {filename}")  # Debugging output
            for folder, extensions in file_types.items():
                if filename.lower().endswith(tuple(extensions)):
                    shutil.move(file_path, os.path.join(desktop_path, folder, filename))
                    print(f"Moved {filename} to {folder}")  # Debugging output
                    moved = True
                    break
            # Optional: If file type doesn't match, move to 'Others' folder
            if not moved:
                others_folder = os.path.join(desktop_path, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))
                print(f"Moved {filename} to Others")  # Debugging output

# Run the function
organize_files()
