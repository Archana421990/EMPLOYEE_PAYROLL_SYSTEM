from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
#gauth.LoadClientConfigFile(os.path.join(os.getcwd(), "employee_payroll_system", "client_secrets.json"))

def authenticate_drive():
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile("client_secrets.json")  # Ensure this file exists
    gauth.LocalWebserverAuth()  # Opens browser for authentication
    return GoogleDrive(gauth)

drive = authenticate_drive()

def upload_csv_to_drive():
    file_path = "employee_payroll_report.csv"  # Ensure this file exists
    upload_file = drive.CreateFile({"title": "employee_payroll_report.csv"})
    upload_file.SetContentFile(file_path)
    upload_file.Upload()

    print("CSV file uploaded successfully to Google Drive!")

    # Get the Google Drive file link
    file_id = upload_file['id']
    #drive_link = f"https://drive.google.com/file/d/{file_id}/view"
    drive_link = f"https://drive.google.com/file/d/12tJ7MzxYTzfdDSU3uL-_uVI_vfcKC7XC/view?usp=drive_link"
    print(f"File Link: {drive_link}")

    return drive_link

import webbrowser

def open_csv_in_browser():
    file_link = upload_csv_to_drive()  # Uploads and gets file link
    webbrowser.open(file_link)  # Opens CSV in browser
