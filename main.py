import requests
from bs4 import BeautifulSoup
import os
import subprocess
import time

url_LATAM= "https://www.mediafire.com/file/lsl6t6zuikavrgw/Skate_3_Online.7z/file"
url_EU= "https://www.mediafire.com/file/g23mwmh8foxb80b/Skate_3_Online_EU_version.7z/file"
headers = {
    "User-Agent": "Mozilla/5.0"
}



def get_url(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    boton = soup.find('a', {'aria-label': 'Download file'})

    if boton and boton.has_attr('href'):
        print("Enlace de descarga:", boton['href'])
    
        return boton['href']
    else:
        print("No se pudo encontrar el enlace de descarga.")
        return None
    
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def descargar_archivo(nombre, url):
    if not os.path.exists(nombre):
        print(f"Descargando {nombre}...")
        subprocess.run(["curl", "-L", "-o", nombre, url])
    else:
        print(f"{nombre} ya existe. No se descargará nuevamente.")

def instalar_7zip():
    print("Instalando 7-Zip...")
    url = "https://www.7-zip.org/a/7zr.exe"
    descargar_archivo("7zr.exe", url)

def descomprimir(nombre_archivo):
    print(f"Descomprimiendo {nombre_archivo}...")
    result = subprocess.run(["7zr.exe", "x", nombre_archivo, "-oSkate3"])
    if result.returncode != 0:
        print("❌ Error al descomprimir. Verificá que 7-Zip esté instalado.")
        exit(1)
    else:
        print("✅ Archivo descomprimido con éxito.")

def descargar_firmware():
    clear_screen()
    print("Descargando Firmware para RPCS3...")
    firmware_url = "http://dmx01.ps3.update.playstation.net/update/ps3/image/mx/2025_0305_c179ad173bbc08b55431d30947725a4b/PS3UPDAT.PUP"
    descargar_archivo("Firmware_ps3.PUP", firmware_url)

def finalizar_instalacion():
    clear_screen()
    print("✅ Instalación finalizada")
    print("🔧 Instrucciones importantes:")
    print("- Ingresá tus datos en Proxy")
    print("- Configurá RPCN en el emulador")
    print("- Asegurate de instalar el firmware")
    print("\nGracias por usar el instalador de Skate 3 Online by Kewsito 🎮")
    print("Unite a nuestro Discord: https://discord.gg/EyTvqHVybG")
    input("\nPresioná Enter para salir.")

def instalar_region(nombre_archivo, url):
    clear_screen()
    print(f"Usted seleccionó: {nombre_archivo}")
    descargar_archivo(nombre_archivo, url)
    instalar_7zip()
    descomprimir(nombre_archivo)
    descargar_firmware()
    finalizar_instalacion()

def menu():
    while True:
        clear_screen()
        print("===============================")
        print("    SKATE 3 ONLINE INSTALLER")
        print("          by Kewsito")
        print("===============================")
        print("     SELECCIONAR REGIÓN")
        print("===============================")
        print("1 - Europa")
        print("2 - Latam")
        print("3 - Salir")
        print("===============================")
        print("NOTA: Este instalador requiere conexión a internet.")
        print("Excluí la carpeta en Windows Defender si es necesario.")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            url = get_url(url_EU)
            if url:
                instalar_region("Skate3_EU.7z", url)
            else:
                print("No se pudo obtener el enlace de descarga para la región Europa.")
                time.sleep(2)
            break
        elif opcion == "2":
            url = get_url(url_LATAM)
            if url:
                instalar_region("Skate3_LATAM.7z", url)
            else:
                print("No se pudo obtener el enlace de descarga para la región LATAM.")
                time.sleep(2)
            break
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            time.sleep(2)

if __name__ == "__main__":
    menu()