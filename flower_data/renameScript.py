import os
import json
def rename_files(folder_path, flower_types):
    # Change the current working directory to the specified folder
    os.chdir(folder_path)

    # List all files in the folder
    files = os.listdir()

    # Rename each file to the new name
    for file_name in files:
        # Construct the new file name
        if file_name != '.DS_Store' and file_name.isdigit():
            new_file_path = os.path.join(folder_path, flower_types[file_name])
            os.rename(file_name, flower_types[file_name])

        
if __name__ == "__main__":
    # Replace this value with the actual path to your "Test" folder
    folder_path = "valid"
    with open('cat_to_name.json', 'r') as flower_cat:
        data = flower_cat.read()
    flower_types = json.loads(data)
    rename_files(folder_path, flower_types)
