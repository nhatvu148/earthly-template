import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
FILE_NAME = os.getenv("FILE_NAME")
PARENT_ID = os.getenv("PARENT_ID")


def search_file(headers, file_name, parent_id):
    """Search for a file by name and parent ID."""
    search_url = "https://www.googleapis.com/drive/v3/files"
    search_params = {
        'q': f"name='{file_name}' and '{parent_id}' in parents and trashed=false",
        'fields': 'files(id, name)'}
    response = requests.get(search_url, headers=headers, params=search_params)
    files = response.json().get('files', [])
    return files


def delete_file(headers, file_id):
    """Delete a file by ID."""
    delete_url = f"https://www.googleapis.com/drive/v3/files/{file_id}"
    response = requests.delete(delete_url, headers=headers)
    return response.status_code


def upload_file(headers, file_path, file_metadata):
    """Upload a file to Google Drive."""
    files = {
        "data": (
            "metadata",
            json.dumps(file_metadata),
            "application/json; charset=utf-8"),
        "file": (
            "file",
            open(
                file_path,
                "rb"),
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
    upload_url = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"
    response = requests.post(upload_url, headers=headers, files=files)
    files['file'][1].close()  # Close the file after uploading
    return response


def main():
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    file_path = f"/app/data/{FILE_NAME}"

    # Search and delete the file if it exists
    files = search_file(headers, FILE_NAME, PARENT_ID)
    if files:
        file_id = files[0]['id']
        status_code = delete_file(headers, file_id)
        print(f"Deleted file ID: {file_id}, Status Code: {status_code}")
    else:
        print("No file found to delete.")

    # Upload the file
    file_metadata = {"name": FILE_NAME, "parents": [PARENT_ID]}
    response = upload_file(headers, file_path, file_metadata)
    print(f"Upload Status Code: {response.status_code}")
    print(f"Response: {response.text}")


if __name__ == "__main__":
    main()
