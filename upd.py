import requests
import os
import sys
import time

USUARIO = "Kewsito"
REPO = "Skate-3-Online-with-Proxy"
URL_API = f"https://api.github.com/repos/{USUARIO}/{REPO}/releases/latest"

# Versión local de tu programa
def version_a_tupla(version):
    version = version.lstrip("v")
    return tuple(map(int, version.split(".")))

def verificar_actualizacion(MI_VERSION):
    os.system("cls")
    try:
        response = requests.get(URL_API, timeout=10)
        response.raise_for_status()
        data = response.json()

        ultima_version = data["tag_name"]
        print(f"Última versión disponible: {ultima_version}")
        print(f"Tu versión actual: {MI_VERSION}")
        ultima_version = version_a_tupla(ultima_version)
        MI_VERSION = version_a_tupla(MI_VERSION)
        if ultima_version >= MI_VERSION:
            print("¡Hay una nueva versión disponible!")
            res = input("Actualizar Instalador? (S/N)")
            if res.lower() != "s":
                print("Actualización cancelada.")
                return
            for asset in data.get("assets", []):
                if asset["name"].endswith(".exe"):  # Ajusta según lo que publicás
                    url_descarga = asset["browser_download_url"]
                    descargar_actualizacion(url_descarga, asset["name"])
                    break
            else:
                print("No se encontró el instalador en los assets.")
        else:
            print("Tu programa ya está actualizado.")
            time.sleep(2)

    except Exception as e:
        print(f"Error verificando actualizaciones: {e}")

def descargar_actualizacion(url, nombre_archivo):
    print(f"Descargando {nombre_archivo} desde {url}...")
    r = requests.get(url, stream=True)
    with open(nombre_archivo, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print("Descarga completa.")

    # Opcional: Ejecutar el instalador y salir del programa
    os.startfile(nombre_archivo)
    sys.exit()