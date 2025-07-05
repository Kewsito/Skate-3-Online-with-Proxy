import requests
from bs4 import BeautifulSoup
import os
import subprocess
import time
import upd as updater
# Constantes
VERSION_LOCAL="v1.4"
url_LATAM = "https://www.mediafire.com/file/lsl6t6zuikavrgw/Skate_3_Online.7z/file"
url_EU = (
    "https://www.mediafire.com/file/g23mwmh8foxb80b/Skate_3_Online_EU_version.7z/file"
)
Skate3_EU = "https://www.mediafire.com/file/jl7fj99cm22ro54/Skate_3_BLES.7z/file"
Skate3_LATAM = "https://www.mediafire.com/file/tr6vez5ujecm89t/Skate_3_BLUS.7z/file"

# DLC's
DLC_EU = "https://www.mediafire.com/file/5pphq45o6qcqrvn/Skate_3_BLES_DLC_for_RPCS3&PS3.7z/file"
DLC_LATAM = "https://www.mediafire.com/file/db9inenrfz3ixet/Skate_3_BLUS_DLC_for_RPCS3%2526PS3.7z/file"

# Mod Menu
Native_Menu = "https://www.mediafire.com/file/3tel1wo0sarzo5u/S3Native.exe/file"
headers = {"User-Agent": "Mozilla/5.0"}

def get_url(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    boton = soup.find("a", {"aria-label": "Download file"})

    if boton and boton.has_attr("href"):
        return boton["href"]
    else:
        print("No se pudo encontrar el enlace de descarga.")
        time.sleep(2)
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
    if not os.path.exists("7zr.exe"):
        print("7-Zip no está instalado. Instalando...")
        instalar_7zip()
    if not os.path.exists(nombre_archivo):
        print(f"El archivo {nombre_archivo} no existe. Asegúrate de descargarlo primero.")
        exit(1)
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
        print("1 - Descargar e Instalar Skate 3 ONLINE + Emulador + Firmware")
        print("2 - Descargar Firmware para RPCS3")
        print("3 - Descargar Skate 3 EUROPE / LATAM")
        print("4 - Descargar DLC's Skate 3 EUROPE / LATAM")
        print("5 - Descargar Skate 3 Native Menu")
        print("6 - Actualizar Instalador")
        print("0 - Salir")
        print("===============================")
        print("NOTA: Este instalador requiere conexión a internet.")
        print("Excluí la carpeta en Windows Defender para evitar problemas.")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            menuSkateNuevo()
            break
        elif opcion == "2":
            descargar_firmware()
            break
        elif opcion == "3":
            menuSkateImagen()
            break
        elif opcion == "4":
            clear_screen()
            print("===============================")
            print("     SELECCIONAR REGIÓN")
            print("===============================")
            print("1 - Europa")
            print("2 - Latam")
            print("3 - Salir")
            print("===============================")
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                url = get_url(DLC_EU)
                if url:
                    descargar_archivo("DLC_Skate3_EU.7z", url)
                    descomprimir("DLC_Skate3_EU.7z")
                else:
                    print("No se pudo obtener el enlace de descarga para la región Europa.")
                    time.sleep(2)
            elif opcion == "2":
                url = get_url(DLC_LATAM)
                if url:
                    descargar_archivo("DLC_Skate3_LATAM.7z", url)
                    descomprimir("DLC_Skate3_LATAM.7z")
                else:
                    print("No se pudo obtener el enlace de descarga para la región LATAM.")
                    time.sleep(2)
            elif opcion == "3":
                print("Saliendo...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
                time.sleep(2)
        elif opcion == "5":
            clear_screen()
            print("===============================")
            print("     DESCARGAR NATIVE MENU")
            print("===============================")
            url = get_url(Native_Menu)
            if url:
                descargar_archivo("Native_Menu.exe", url)
                print("Descarga completa.")
                time.sleep(2)
            else:
                print("No se pudo obtener el enlace de descarga para el Native Menu.")
                time.sleep(2)
        elif opcion == "6":
            updater.verificar_actualizacion(VERSION_LOCAL)
            time.sleep(2)
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            time.sleep(2)


def menuSkateImagen():
    while True:
        clear_screen()
        print("===============================")
        print("     SELECCIONAR REGIÓN")
        print("===============================")
        print("1 - Europa")
        print("2 - Latam")
        print("3 - Salir")
        print("===============================")
        print("NOTA: Este instalador requiere conexión a internet.")
        print("Excluí la carpeta en Windows Defender para evitar problemas.")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            url = get_url(Skate3_EU)
            if url:
                descargar_archivo("Skate3_EU.7z", url)
                clear_screen()
                res = input("Descarga completa. Descomprimir archivo? (S/N)")
                if res.lower() == "s":
                    descomprimir("Skate3_EU.7z")
                else:
                    print("Descompresión omitida.")
            else:
                print("No se pudo obtener el enlace de descarga para la región Europa.")
                time.sleep(2)
            break
        elif opcion == "2":
            url = get_url(Skate3_LATAM)
            if url:
                descargar_archivo("Skate3_LATAM.7z", url)
                clear_screen()
                res = input("Descarga completa. Descomprimir archivo? (S/N)")
                if res.lower() == "s":
                    descomprimir("Skate3_EU.7z")
                else:
                    print("Descompresión omitida.")
                break
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


def menuSkateNuevo():
    while True:
        clear_screen()
        print("===============================")
        print("     SELECCIONAR REGIÓN")
        print("===============================")
        print("1 - Europa")
        print("2 - Latam")
        print("3 - Salir")
        print("===============================")
        print("NOTA: Este instalador requiere conexión a internet.")
        print("Excluí la carpeta en Windows Defender para evitar problemas.")
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
    # menu()
