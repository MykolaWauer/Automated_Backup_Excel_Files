# Import necessary libraries for file system monitoring
import os 
import shutil 
import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 

# Define a custom event handler for file system events
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event): # method, which is called when a file or directory is modified
        if event.is_directory:
            # Ignore events related to directories
            return
        if not event.src_path.endswith('~$'):
            try:
                # Print a message when a file is modified and update the destination folder
                print(f'File {event.src_path} has been modified. Updating Test_2 folder...')
                copy_files(source_folder, destination_folder)
            except Exception as e:
                # Handle errors during the update process
                print(f"Error: {e}")

def copy_files(source_folder, destination_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"The source folder '{source_folder}' does not exist.")
        return

    # Check if the destination folder exists, create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"The destination folder '{destination_folder}' has been created.")

    try:
        # Copy the entire directory structure from the source to destination
        shutil.rmtree(destination_folder)  # Remove existing destination folder
        shutil.copytree(source_folder, destination_folder)
        print(f"Contents of '{source_folder}' copied to '{destination_folder}'.")
    except Exception as e: # Raise an exception if an error occurs during the copy process
        raise e

if __name__ == "__main__":
    # Define source and destination folders
    source_folder = "C:\\Users\\wauer_m\\Desktop\\Test"
    destination_folder = "C:\\Users\\wauer_m\\Desktop\\Test_2"

    # Initial copy of files from source to destination
    copy_files(source_folder, destination_folder)

    # Set up watchdog observer to monitor file system events
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=source_folder, recursive=True)
    observer.start()

    # Keep the script running to continuously monitor file system events
    try:
        while True:
            time.sleep(1)
    # Stop the observer when a keyboard interrupt (Ctrl+C) is received
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
