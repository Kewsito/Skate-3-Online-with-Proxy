import os,time

def crear_bat_en_escritorio():
    # Obtener ruta del escritorio del usuario
    escritorio = os.path.join(os.path.expanduser("~"), "Desktop")

    # Nombre del archivo .bat
    nombre_bat = "Iniciar Skate3 + Proxy.bat"
    ruta_bat = os.path.join(escritorio, nombre_bat)

    # Ruta relativa desde la ubicación del script a los ejecutables
    ruta_proxy = os.path.abspath(os.path.join("Skate3","Skate 3 Online", "Skate 3 RPCS3 Proxy", "Skate3RPCNProxy.exe"))
    ruta_emulador = os.path.abspath(os.path.join("RPCS3", "rpcs3.exe"))  # <-- Cambiá si usás otra ruta

    # Contenido del archivo .bat (ejecutar como administrador con PowerShell)
    contenido = f"""@echo off
echo Ejecutando Skate3RPCNProxy como administrador...
powershell -Command "Start-Process -Verb runAs '{ruta_proxy}'"

timeout /t 5

echo Iniciando RPCS3 como administrador...
powershell -Command "Start-Process -Verb runAs '{ruta_emulador}'"

exit
"""

    # Guardar el archivo
    with open(ruta_bat, "w") as f:
        f.write(contenido)

    print(f"✅ Archivo .bat creado en el escritorio:\n{ruta_bat}")
    time.sleep(5)


if __name__ == "__main__":
    crear_bat_en_escritorio()