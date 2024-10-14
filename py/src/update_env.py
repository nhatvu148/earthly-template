import os
import glob
import os
import json
from dotenv import load_dotenv

load_dotenv()

FILE_DIR = os.getenv("FILE_DIR")

def read_env_file(env_path):
    """
    Read the .env file and return its contents as a list of lines.
    """
    if not os.path.exists(env_path):
        print("The .env file does not exist.")
        return None
    with open(env_path, 'r') as file:
        lines = file.readlines()
    return lines

def write_env_file(env_path, lines):
    """
    Write the given lines back to the .env file.
    """
    with open(env_path, 'w') as file:
        file.writelines(lines)

def update_env_variable(env_path, variable_name, new_value):
    """
    Generic function to update a specific variable in the .env file.
    """
    lines = read_env_file(env_path)
    if lines is None:
        return  # File not found, read_env_file already printed an error

    updated = False
    for i, line in enumerate(lines):
        if line.startswith(f'{variable_name}='):
            lines[i] = f'{variable_name}="{new_value}"\n'
            updated = True
            break

    if not updated:  # Append the variable if not found
        lines.append(f'{variable_name}="{new_value}"\n')

    write_env_file(env_path, lines)
    print(f"Updated {variable_name} in .env to {new_value}")

def update_access_token_from_json(env_path, json_path):
    """
    Update the ACCESS_TOKEN field in the .env file using the access_token from the specified JSON file.
    """
    if not os.path.exists(json_path):
        print("The JSON file does not exist.")
        return

    with open(json_path, 'r') as file:
        data = json.load(file)
        access_token = data.get('access_token')
        if not access_token:
            print("Access token not found in the JSON file.")
            return

    update_env_variable(env_path, 'ACCESS_TOKEN', access_token)

def update_file_name_in_env(env_path, new_file_name):
    """
    Update the FILE_NAME field in the .env file.
    """
    update_env_variable(env_path, 'FILE_NAME', new_file_name)

def find_latest_xlsx(source_dir):
    """
    Find the most recently created .xlsx file in the source_dir and copy it to dest_dir.
    """
    # List all .xlsx files in the source directory
    files = glob.glob(os.path.join(source_dir, "*.xlsx"))
    
    # Check if there are any .xlsx files found
    if not files:
        print("No .xlsx files found in the source directory.")
        return

    # Find the latest file by creation time
    latest_file_path = max(files, key=os.path.getctime)

    # Extract the filename from the path
    latest_file_name = os.path.basename(latest_file_path)
    return latest_file_name

def main():
    env_path = "./.env"
    json_file_path = "./refresh_token_response.json"
    latest_file = find_latest_xlsx(FILE_DIR)
    update_access_token_from_json(env_path, json_file_path)
    update_file_name_in_env(env_path=env_path, new_file_name=latest_file)

if __name__ == "__main__":
    main()