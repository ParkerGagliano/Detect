import os
import time
import platform
platform.system()




# Set the path of the file you want to monitor
file_path = 'test.txt'

# Get the initial modification time of the file
last_modified = os.path.getmtime(file_path)

def push(title, message):
	plt = platform.system()

	if plt=='Darwin':
		command = f'''
		osascript -e 'display notification "{message}" with title "{title}"'
		'''
	if plt=='Linux':
		command = f'''
		notify-send "{title}" "{message}"
		'''
	else:
		return

	os.system(command)



while True:
    # Check if the file has been modified
    if os.path.getmtime(file_path) != last_modified:
        push('File Modified', 'File has been modified!')
        print('File has been modified!')
        # Update the last modification time
        last_modified = os.path.getmtime(file_path)
    # Wait for a short period of time before checking again
    time.sleep(10)


