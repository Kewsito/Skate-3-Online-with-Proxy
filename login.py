import os
import json

def crear_login_json(email,password,psn_name):
    # Ruta relativa desde donde estás ubicado
    ruta_relativa = os.path.join("Skate3", "Skate 3 Online","Skate 3 RPCS3 Proxy")
    
    # Ruta absoluta (basada en donde se ejecuta el script)
    ruta_absoluta = os.path.abspath(ruta_relativa)

    # Asegurarse de que la carpeta existe
    if not os.path.exists(ruta_absoluta):
        print(f"❌ La carpeta no existe: {ruta_absoluta}")
        return

    # Ruta completa del archivo JSON
    ruta_archivo = os.path.join(ruta_absoluta, "login.json")

    # Estructura del JSON
    datos = {
        "email": email,
        "password": password,
        "psnName": psn_name
    }

    # Guardar archivo
    with open(ruta_archivo, "w") as f:
        json.dump(datos, f, indent=2)

    print(f"\n✅ login.json creado en:\n{ruta_archivo}")
    input("Presione enter para continuar")
    

# Ejecutar la función
def login():
    print("Vamos a logearte!")
    print("Recorda que tu cuenta de EA y PSN debe estar enlazada previamente !")
    estado = input("Tus cuentas estan enlazadas? (S/N)")
    if estado.capitalize()=="S":        
        email=input("Ingrese su email de EA \n")
        password =input("Ingrese su contraseña de EA \n")
        psn_name =input("Ingresa tu ID de Play Station Network \n")
        os.system("cls")
        print("Email:",email)
        print("Contraseña:",password)
        print("ID PlayStation:",psn_name)
        
        e=input("Sus datos son correctos? (S/N)\n")
        if e.lower()=='s':
            crear_login_json(email,password,psn_name)
        else:
            login()
    else:
        print("Ingresa a EA, y selecciona tu cuenta de PSN")
        print("https://myaccount.ea.com/am/ui/connected-accounts")
        input("Presione enter para continuar")
        login()
    return

