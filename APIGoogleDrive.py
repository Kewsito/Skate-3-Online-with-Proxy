
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
import io
import os
import json
import re
from dotenv import load_dotenv
load_dotenv()
# Leer credenciales desde variable de entorno
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def authenticate_drive_api():
    creds_json = os.environ.get('GDRIVE_CREDS')
    if not creds_json:
        raise EnvironmentError("La variable de entorno GDRIVE_CREDS no está definida.")
    creds_dict = json.loads(creds_json)
    creds = service_account.Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)
    return service

def download_file(service, file_id, destination):
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(destination, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        if status:
            print(f"Descargando {int(status.progress() * 100)}%")
    print(f"✅ Archivo descargado en: {destination}")

def extraer_id_drive(url):
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
    return match.group(1) if match else None

def iniciarAPI(nombre_archivo,url):
    if not os.path.exists(nombre_archivo):
            
        file_id = extraer_id_drive(url)
        service = authenticate_drive_api()
        if service and file_id:
            print(f"Descargando {nombre_archivo}")
            download_file(service, file_id, nombre_archivo)
        else:
            print("❌ Error al autenticar o extraer el ID del archivo. Verifica la URL y las credenciales.")
            exit(1)
    else:
        return