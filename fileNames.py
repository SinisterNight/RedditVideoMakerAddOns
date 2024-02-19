import os
import pyperclip

def get_newest_directory(directory):
    # Get a list of all directories in the specified directory
    directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    # Sort directories by modification time (newest first)
    directories.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
    # Get the name of the newest directory
    newest_directory = directories[0]
    print("Newest directory:", newest_directory)
    return os.path.join(directory, newest_directory)

def get_newest_file_name(directory):
    # Print directory contents
    print("Directory contents:")
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name)

    # Get a list of all files in the specified directory
    files = [entry.name for entry in os.scandir(directory) if entry.is_file()]
    print("Files in directory:", files)

    # Add full path to each file
    files = [os.path.join(directory, f) for f in files]
    print("Files with full path:", files)

    # Sort files based on modification time (newest last)
    files.sort(key=lambda x: os.path.getmtime(x) if os.path.exists(x) else 0)
    print("Sorted files:", files)

    # Retrieve the newest file name
    newest_file = files[-1] if files else None
    print("Newest file:", newest_file)

    # If a newest file exists, return its name without extension
    if newest_file:
        return os.path.splitext(os.path.basename(newest_file))[0]
    else:
        return None


def main():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    start_directory = os.path.join(script_dir, 'results')
    newest_directory = get_newest_directory(start_directory)
    print("Newest directory:", newest_directory)
    
    newest_file_name = get_newest_file_name(newest_directory)
    print("Newest file name:", newest_file_name)
    
    if newest_file_name:
        pyperclip.copy(newest_file_name)
        print("Copied to clipboard:", newest_file_name)
    else:
        print("No files found in the newest directory.")

if __name__ == "__main__":
    main()
