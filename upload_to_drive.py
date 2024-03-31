import os
from time import sleep
import warnings
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import json 

warnings.simplefilter('ignore', category=UserWarning)

# Define a global scheduler
import json

# Load the JSON file
with open('cred.json') as f:
    credentials = json.load(f)




def find_data_files(directory):
    data_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                full_path = os.path.join(root, file)
                data_files.append(full_path)
    return data_files

def uploading_script(credentials):
    
    
    home_directory = os.path.expanduser("~")
    directory = os.path.join(home_directory, 'Desktop','Mohammed')
                            #   'inventory','data')

    print(f"Uploading this file{directory} to drive")
    data_files = find_data_files(directory)
    print(f'files are {data_files}')
    # Initialize the Drive API client
    credentials = Credentials.from_service_account_info(credentials,
                                                        scopes=["https://www.googleapis.com/auth/drive"])
    service = build('drive', 'v3', credentials=credentials)

    for data_file in data_files:
        # if file_name in data_file:
            file_metadata = {
                'name': os.path.basename(data_file),
                # If you want to change the parent file, where the files will be uploaded, look for the last element on the link of file in drive
                'parents': ['1qPFE509-0DruZS2mrhSUYgCi5_JJ_JQ7'],
                'mimeType': 'application/pdf'
            }
# If you want to change the type of folde please refer to this link https://developers.google.com/drive/api/guides/ref-export-formats
            mime_type = 'application/pdf'
            media = MediaFileUpload(data_file, mimetype=mime_type)
            request = service.files().create(media_body=media, body=file_metadata, supportsAllDrives=True)
            request.execute()
            print('data uploaded !!!')
            # success_popup()
    return 
           
uploading_script(credentials)
