import os
import sys
import time
from rich import print
from rich.panel import Panel

import zipfile





def unzip_with_password(zip_file_path, extract_path):
    zip_password = input("Enter The Zip password: ")
    print("[bold green]Please Wait Files Are Extracting ...([italic blue]it will take 15min)[bold green] Take a Coffe break")
    
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)
    else:
        print("Directory already exists. Changing working directory.")
        os.system("cd .spy/.spy")
    
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        try:
            zip_ref.extractall(extract_path, pwd=zip_password.encode('utf-8'))
            print("Extraction successful!")
        except zipfile.BadZipFile:
            print("Invalid ZIP file or incorrect password.")

if __name__ == "__main__":
    zip_file_path = "ind.zip"
    extract_path = ".spy/"
    unzip_with_password(zip_file_path, extract_path)
