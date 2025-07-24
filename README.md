# 🛠️ Skate 3 Online Installer por Kewsito

Un instalador automatizado para configurar Skate 3 Online de forma rápida y sin complicaciones en el emulador RPCS3. Soporta las regiones de Europa (EU) y Latinoamérica (LATAM), automatizando todo el proceso de descarga y configuración.

## 🎮 Funcionalidades Principales
-   **📦 Descarga del Juego:** Descarga automáticamente la versión completa del juego para tu región seleccionada (Europa o Latinoamérica), incluyendo el emulador RPCS3.
-   **🧩 Descarga de Firmware:** Obtiene el firmware oficial de PS3 necesario para que RPCS3 funcione correctamente.
-   **🎮 DLC y Extras:** Incluye opciones para descargar los DLCs oficiales y el popular "Skate 3 Native Menu".
-   **🧰 Instalación Automática:** Instala la herramienta de línea de comandos de 7-Zip (`7zr.exe`) si no está presente y descomprime todos los archivos necesarios.
-   **🔑 Configuración de Proxy:** Te guía para crear el archivo `login.json` con tus credenciales de EA y PSN, un paso crucial para jugar online.
-   **🔄 Actualizador Automático:** El script puede verificar si hay una nueva versión del instalador y actualizarse automáticamente.

## 🚀 Instalación y Uso (Método Recomendado)
1.  Ve a la sección de **[Releases](https://github.com/Kewsito/Skate-3-Online-with-Proxy/releases)** de este repositorio.
2.  Descarga el archivo `.exe` más reciente.
    -   *Nota: Tu navegador o Windows pueden mostrar una advertencia de seguridad. Es un falso positivo, puedes ignorarlo y descargar el archivo.*
3.  Ejecuta el archivo `.exe` que descargaste.
4.  Sigue las instrucciones del menú para seleccionar tu región e iniciar la instalación. El programa se encargará del resto.

## ⚠️ Requisitos
-   Sistema Operativo Windows.
-   Conexión a internet estable.
-   Espacio en disco suficiente para el juego y el emulador (aproximadamente 10 GB).
-   Se recomienda encarecidamente añadir una exclusión en tu antivirus para la carpeta donde ejecutes el script.

## ⚙️ Configuración Final para Jugar Online
Una vez que el instalador termine, debes completar los siguientes pasos en el emulador para poder jugar online:

#### 1. Instalar el Firmware
-   Abre el emulador RPCS3.
-   Ve al menú `File > Install Firmware`.
-   Busca y selecciona el archivo `PS3UPDAT.PUP` que fue descargado por el instalador.

#### 2. Configurar las Credenciales del Proxy
-   El instalador te pedirá tu email de EA, contraseña de EA y tu PSN ID para crear automáticamente el archivo `login.json`.
-   **¡IMPORTANTE!** Tu cuenta de EA y tu cuenta de PSN deben estar **vinculadas previamente**. Puedes hacerlo en la [página de Cuentas Conectadas de EA](https://myaccount.ea.com/am/ui/connected-accounts).

#### 3. Configurar RPCN en el Emulador
-   Dentro del emulador RPCS3, ve a `Configuration > RPCN`.
-   Introduce los datos de tu cuenta de RPCN. Si no tienes una, puedes crearla en la [web oficial de RPCN](https://rpcn.net/).

## 🛡️ Cómo Excluir la Carpeta del Antivirus
Para evitar que Windows Defender u otro antivirus interrumpa la instalación:
1.  Abre **Seguridad de Windows**.
2.  Ve a **Protección contra virus y amenazas**.
3.  En "Configuración de antivirus y protección contra amenazas", haz clic en **Administrar la configuración**.
4.  Busca la sección "Exclusiones" y haz clic en **Agregar o quitar exclusiones**.
5.  Haz clic en **Agregar una exclusión**, selecciona **Carpeta** y elige la carpeta donde guardaste el instalador.

## 🙌 Créditos
-   Script creado por **Kewsito**.
-   Hecho posible gracias a las comunidades de **RPCN** y **RPCS3**.
-   Únete al Discord: [https://discord.gg/EyTvqHVybG](https://discord.gg/EyTvqHVybG)
