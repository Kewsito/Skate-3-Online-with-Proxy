
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
import io
import os
import json
import re

# Credenciales de Google Drive - CONFIGURAR EN VARIABLES DE ENTORNO
# Para uso local, crear un archivo .env con las credenciales
# Para PyInstaller, las credenciales deben estar en el archivo .env incluido
def get_gdrive_credentials():
    """Obtiene las credenciales de Google Drive desde variables de entorno o archivo .env"""
    import os
    
    # Intentar cargar desde archivo .env si existe
    env_file = '.env'
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value.strip('"\'')
    
    # Construir diccionario de credenciales desde variables de entorno
    return {
        "type": "service_account",
        "project_id": os.getenv('GOOGLE_PROJECT_ID', 'skate3onlineinstaller'),
        "private_key_id": os.getenv('GOOGLE_PRIVATE_KEY_ID', ''),
        "private_key": os.getenv('GOOGLE_PRIVATE_KEY', '').replace('\\n', '\n'),
        "client_email": os.getenv('GOOGLE_CLIENT_EMAIL', ''),
        "client_id": os.getenv('GOOGLE_CLIENT_ID', ''),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/{os.getenv('GOOGLE_CLIENT_EMAIL', '').replace('@', '%40')}",
        "universe_domain": "googleapis.com"
    }

# Leer credenciales desde variable de entorno
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def authenticate_drive_api():
    creds_dict = get_gdrive_credentials()
    if not creds_dict or not creds_dict.get('private_key'):
        raise EnvironmentError("Las credenciales de Google Drive no están definidas. Verifica el archivo .env")
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