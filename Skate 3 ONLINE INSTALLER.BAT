@echo off
color 0A
title Skate 3 Online Installer by Kewsito

:menu
cls
echo ================================
echo      SKATE 3 ONLINE INSTALLER
echo            by Kewsito
echo      
echo      SELECCIONAR REGION
echo ================================
echo 1 - Europa
echo 2 - Latam
echo 3 - Salir
echo ================================
echo ================================
echo 
echo NOTA: Este instalador requiere conexion a internet.
echo Asegurese de excluir la carpeta del antivirus de Windows Defender.
set /p opcion="Ingrese una opcion: "

if "%opcion%"=="1" goto europa
if "%opcion%"=="2" goto latam
if "%opcion%"=="3" exit
echo Opcion invalida. Intente nuevamente.
pause
goto menu

:europa
echo Usted selecciono REGION EUROPA.
echo Descargando archivo...
set nombre=Skate3_EU.7z
curl -L -o "%nombre%" "https://download1326.mediafire.com/o8df6rigw68gemg3R0kGwExYWc2OBf_Mv2qy0--l9UPupA917dgObZzTLGjQRc2VNy-mUOTxrUE2hO9MvPfJWM-W9JQ2Gzhcon9TgqMCz2V7eQECUo9ZQR9owl78040e1DMnC37bqBfzuHlPOl8P-2f-OYVqHnxq3nbHzGkLp7xweA/g23mwmh8foxb80b/Skate+3+Online+EU+version.7z"
echo Descarga finalizada.
goto Firmware
goto 7zip
echo Descomprimiendo archivo...
if not exist "Skate3_EU" mkdir "Skate3_EU"
7zr x "%nombre%.7z" -o"Skate3_EU"
pause
goto menu

:latam
echo Usted selecciono REGION LATAM.
echo Descargando archivo...
set nombre=Skate3_LATAM.7z
curl -L -o "%nombre%" "https://download1339.mediafire.com/fh3vhcuuu3dg1Nl-_iFyu5qXpxCgbBdXO1fORKqiDLuE2WzBYl7IKV7tx4tn6tsqEKeFjpgTqkBji5F0C4ZB7_7C13gHHStCg3mb8TXp1iCXA5rYYyzcf84xoKjY2yPOJumGa32IdZr0W5rRuOB3Z-HQkiU425XGhilFR9kMqdF2WQ/lsl6t6zuikavrgw/Skate+3+Online.7z"
echo Descarga finalizada.
goto Firmware
goto 7zip
echo Descomprimiendo archivo...
if not exist "Skate3_LATAM" mkdir "Skate3_LATAM"
7zr x "%nombre%.7z" -o"Skate3_LATAM"
pause

:Firmware
echo ================================
echo      Descargando Firmware
echo           para RPCS3
echo ================================
curl -L -o "Firmware_ps3.PUP" "http://dmx01.ps3.update.playstation.net/update/ps3/image/mx/2025_0305_c179ad173bbc08b55431d30947725a4b/PS3UPDAT.PUP"
pause

:7zip
echo ================================
echo      Instalando 7-Zip
echo ================================
curl -L -o "7z.exe" "https://www.7-zip.org/a/7zr.exe"
if not exist "7z.exe" (
    echo Error al descargar 7-Zip. Asegurese de tener conexion a internet.
    pause
    exit /b
)
goto menu

