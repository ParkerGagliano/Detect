import os
import time

# Set the path of the file you want to monitor
file_path = 'test.txt'

# Get the initial modification time of the file
last_modified = os.path.getmtime(file_path)

while True:
    # Check if the file has been modified
    if os.path.getmtime(file_path) != last_modified:
        print('File has been modified!')
        # Update the last modification time
        last_modified = os.path.getmtime(file_path)
    # Wait for a short period of time before checking again
    time.sleep(10)
