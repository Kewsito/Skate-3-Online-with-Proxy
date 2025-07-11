import os
import subprocess
import time
import upd as updater
import APIGoogleDrive as API
import login
from dotenv import load_dotenv
import ejecutable as ej
load_dotenv()
# Constantes
VERSION_LOCAL="v2.0"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def descargar_archivo(nombre, url):
    if not os.path.exists(nombre):
        print(f"Descargando {nombre}...")
        subprocess.run(["curl", "-L", "-o", nombre, url])
    else:
        print(f"{nombre} ya existe. No se descargará nuevamente.")
    return


def instalar_7zip():
    print("Instalando 7-Zip...")
    url = "https://www.7-zip.org/a/7zr.exe"
    descargar_archivo("7zr.exe", url)

def descargar_firmware():
    clear_screen()
    print("Descargando Firmware para RPCS3...")
    firmware_url = "http://dmx01.ps3.update.playstation.net/update/ps3/image/mx/2025_0305_c179ad173bbc08b55431d30947725a4b/PS3UPDAT.PUP"
    descargar_archivo("Firmware_ps3.PUP", firmware_url)
    return


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



def finalizar_instalacion():
    clear_screen()
    print("✅ Instalación finalizada")
    print("🔧 Instrucciones importantes:")
    print("- Ingresá tus datos en Proxy")
    print("- Configurá RPCN en el emulador")
    print("\nGracias por usar el instalador de Skate 3 Online by Kewsito 🎮")
    print("Unite a nuestro Discord: https://discord.gg/EyTvqHVybG")
    input("\nPresioná Enter para salir.")


def instalar_region(nombre_archivo, url):
    clear_screen()
    API.iniciarAPI(nombre_archivo, url)
    print(f"Usted seleccionó: {nombre_archivo}")
    estado = input("Desea descomprimir el archivo? (S/N)")
    if estado.lower()=='s':
        instalar_7zip()
        descomprimir(nombre_archivo)
    login.login()
    #ej.crear_bat_en_escritorio()
    finalizar_instalacion()


def menu():
    while True:
        clear_screen()
        print("===============================")
        print("    SKATE 3 ONLINE INSTALLER")
        print("          by Kewsito")
        print("===============================")
        print("1 - Descargar e Instalar Skate 3 ONLINE + DLC's + Emulador")
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
            clear_screen()
            print("✅ Firmware descargado con éxito.")
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
                API.iniciarAPI("DLC_Skate3_EU.7z",os.environ.get('DLC_EU'))
                clear_screen()
                res = input("Descarga completa. Descomprimir archivo? (S/N)")
                if res.lower() == "s":
                    descomprimir("DLC_Skate3_EU.7z")
                else:
                    print("Descompresión omitida.")
                time.sleep(2)
            elif opcion == "2":
                API.iniciarAPI("DLC_Skate3_LATAM.7z",os.environ.get('DLC_LATAM'))
                clear_screen()
                res = input("Descarga completa. Descomprimir archivo? (S/N)")
                if res.lower() == "s":
                    descomprimir("DLC_Skate3_LATAM.7z")
                else:
                    print("Descompresión omitida.")
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
            API.iniciarAPI("Native_Menu.7z", os.environ.get('Native_Menu'))
            break
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
            instalar_region("Skate3_EU.7z",os.environ.get('Skate3_EU'))
            clear_screen()
            res = input("Descarga completa. Descomprimir archivo? (S/N)")
            if res.lower() == "s":
                    descomprimir("Skate3_EU.7z")
            else:
                    print("Descompresión omitida.")
            time.sleep(2)
            break
        elif opcion == "2":
            instalar_region("Skate3_LATAM.7z", os.environ.get('Skate3_LATAM'))
            clear_screen()
            res = input("Descarga completa. Descomprimir archivo? (S/N)")
            if res.lower() == "s":
                    descomprimir("Skate3_EU.7z")
            else:
                    print("Descompresión omitida.")
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
            instalar_region("Skate3_EU.7z",os.environ.get('url_EU'))
            
        elif opcion == "2":
            instalar_region("Skate3_LATAM.7z",os.environ.get('url_LATAM'))
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            time.sleep(2)


if __name__ == "__main__":
    menu()