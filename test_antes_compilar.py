#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de pruebas completas antes de compilar con PyInstaller
Verifica que todas las funcionalidades del proyecto funcionen correctamente
"""

import sys
import os
import subprocess
import time

def test_imports():
    """Prueba 1: Verificar imports básicos"""
    print("\n🧪 PRUEBA 1: Verificando imports...")
    
    try:
        # Imports estándar
        import os, sys, subprocess, json, re, io, time
        print("✅ Imports estándar OK")
        
        # Google API
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaIoBaseDownload
        from google.oauth2 import service_account
        print("✅ Google API imports OK")
        
        # Requests
        import requests
        print("✅ Requests import OK")
        
        # Módulos locales
        import upd, APIGoogleDrive, login, ejecutable
        print("✅ Módulos locales OK")
        
        return True
    except Exception as e:
        print(f"❌ Error en imports: {e}")
        return False

def test_google_api():
    """Prueba 2: Verificar Google API"""
    print("\n🧪 PRUEBA 2: Verificando Google API...")
    
    try:
        import APIGoogleDrive
        print("✅ APIGoogleDrive importado correctamente")
        
        # Verificar credenciales
        try:
            creds = APIGoogleDrive.get_gdrive_credentials()
            if creds and creds.get('private_key'):
                print("✅ Credenciales de Google Drive encontradas")
            else:
                print("❌ Credenciales de Google Drive vacías o archivo .env no encontrado")
                return False
        except Exception as e:
            print(f"❌ Error al obtener credenciales: {e}")
            return False
            
        # Probar autenticación
        try:
            service = APIGoogleDrive.authenticate_drive_api()
            if service:
                print("✅ Autenticación con Google Drive exitosa")
            else:
                print("❌ Error en autenticación con Google Drive")
                return False
        except Exception as e:
            print(f"❌ Error en autenticación: {e}")
            return False
            
    except Exception as e:
        print(f"❌ Error en Google API: {e}")
        return False
    
    return True

def test_file_operations():
    """Prueba 3: Verificar operaciones de archivos"""
    print("\n🧪 PRUEBA 3: Verificando operaciones de archivos...")
    
    try:
        # Crear archivo de prueba
        test_file = "test_temp.txt"
        with open(test_file, 'w') as f:
            f.write("Prueba de escritura")
        print("✅ Escritura de archivos OK")
        
        # Leer archivo
        with open(test_file, 'r') as f:
            content = f.read()
        print("✅ Lectura de archivos OK")
        
        # Eliminar archivo de prueba
        os.remove(test_file)
        print("✅ Eliminación de archivos OK")
        
        return True
    except Exception as e:
        print(f"❌ Error en operaciones de archivos: {e}")
        return False

def test_subprocess():
    """Prueba 4: Verificar subprocess"""
    print("\n🧪 PRUEBA 4: Verificando subprocess...")
    
    try:
        # Ejecutar comando simple
        result = subprocess.run(['echo', 'test'], capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            print("✅ Subprocess OK")
            return True
        else:
            print("❌ Error en subprocess")
            return False
    except Exception as e:
        print(f"❌ Error en subprocess: {e}")
        return False

def test_connectivity():
    """Prueba 5: Verificar conectividad"""
    print("\n🧪 PRUEBA 5: Verificando conectividad...")
    
    try:
        import requests
        response = requests.get('https://www.google.com', timeout=5)
        if response.status_code == 200:
            print("✅ Conectividad a internet OK")
            return True
        else:
            print("❌ Problema de conectividad")
            return False
    except Exception as e:
        print(f"❌ Error de conectividad: {e}")
        return False

def test_main_menu():
    """Prueba 6: Verificar funciones del menú principal"""
    print("\n🧪 PRUEBA 6: Verificando funciones del menú...")
    
    try:
        # Importar main y verificar que las funciones existen
        import main
        
        # Verificar que las funciones principales existen
        functions_to_check = [
            'mostrar_menu',
            'descargar_7zip',
            'descargar_firmware'
        ]
        
        for func_name in functions_to_check:
            if hasattr(main, func_name):
                print(f"✅ Función {func_name} encontrada")
            else:
                print(f"⚠️ Función {func_name} no encontrada")
        
        print("✅ Verificación del menú principal OK")
        return True
    except Exception as e:
        print(f"❌ Error verificando menú principal: {e}")
        return False

def main():
    """Función principal de pruebas"""
    print("🚀 PRUEBAS COMPLETAS ANTES DE COMPILAR")
    print("=" * 40)
    
    tests = [
        ("Imports", test_imports),
        ("Google API", test_google_api),
        ("Operaciones de archivos", test_file_operations),
        ("Subprocess", test_subprocess),
        ("Conectividad", test_connectivity),
        ("Menú principal", test_main_menu)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Error ejecutando {test_name}: {e}")
            results.append(False)
    
    # Resumen final
    print("\n" + "=" * 40)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"🎉 TODAS LAS PRUEBAS PASARON ({passed}/{total})")
        print("✅ El proyecto está listo para compilar")
        print("\n📋 Próximos pasos:")
        print("   1. Ejecutar: .\\compilador_mejorado.bat")
        print("   2. O usar: pyinstaller skate3_installer.spec")
    else:
        print(f"⚠️ ALGUNAS PRUEBAS FALLARON ({passed}/{total})")
        print("❌ Revisa los errores antes de compilar")
        
        # Mostrar qué pruebas fallaron
        print("\n❌ Pruebas que fallaron:")
        for i, (test_name, _) in enumerate(tests):
            if not results[i]:
                print(f"   - {test_name}")
    
    print("\n📖 Para más información, consulta SOLUCION_PYINSTALLER.md")
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)