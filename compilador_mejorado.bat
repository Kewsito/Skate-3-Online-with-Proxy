@echo off
echo Compilando Skate 3 ONLINE INSTALLER con PyInstaller...
echo.

:: Limpiar directorios anteriores
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"

:: Compilar con PyInstaller incluyendo imports ocultos necesarios
pyinstaller --onefile ^--name="Skate 3 ONLINE INSTALLER v2.1" ^--icon=skate3.ico ^--add-data=".env;." ^--hidden-import=googleapiclient ^--hidden-import=googleapiclient.discovery ^--hidden-import=googleapiclient.http ^--hidden-import=google.oauth2 ^--hidden-import=google.oauth2.service_account ^--hidden-import=google.auth ^--hidden-import=requests ^--hidden-import=urllib3 ^--hidden-import=json ^--hidden-import=io ^--hidden-import=re ^--hidden-import=os ^--hidden-import=subprocess ^--hidden-import=time ^--hidden-import=sys ^--collect-all=googleapiclient ^--collect-all=google ^main.py

echo.
echo Compilación completada!
echo El ejecutable se encuentra en: dist\"Skate 3 ONLINE INSTALLER v2.1.exe"
pause