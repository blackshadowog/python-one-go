import os

# Specify the directory path (leave empty to list the current directory)
directory_path = "/" 

# List all files and folders in the specified directory
contents = os.listdir(directory_path)

print("Contents of the directory:")
for item in contents:
    print(item)
