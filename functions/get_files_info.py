import os
from pathlib import Path

def get_files_info(working_directory, directory=None):
    if not os.isdir(directory):
        

    # print(f'Error: "{directory}" is not a directory')
    # check if directory is in working_directory (compare paths)
    
    path_working_directory = os.path.abspath(working_directory)
    list_working_directory = os.listdir(working_directory)
    for file in list_working_directory:
        # dir
        if os.path.isdir(file):
            get_files_info(working_directory, file)
        if file in 
        # file 

    print("list_wd: ", list_working_directory)
    # print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    # absolutePath = os.path.abspath()

    # file_name = 

    # print(f'{file_name}: file_size={file_size} bytes, is_dir={is_dir}')
get_files_info(".")
# os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# .startswith(): Check if a string starts with a substring
# os.path.isdir(): Check if a path is a directory
# os.path.listdir(): List the contents of a directory
# os.path.getsize(): Get the size of a file
# os.path.isfile(): Check if a path is a file
# .join(): Join a list of strings together with a separator