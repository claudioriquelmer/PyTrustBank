# 🏦 Estructura de Datos de Usuarios en Memoria
accounts = {

    # Un ejemplo de usuario con RUT '20123123-K'
    '20123123-K': {
        'password': '1234',
        'accounts': {
            'corriente': {'balance': 0},
            'vista': {'balance': 0},
            'ahorro': {'balance': 0}
        }
    }

}

# 🧩 Creamos una Función para Registrar Nuevos Clientes
def create_account(rut):

    # 1. Verificamos si el RUT ya existe
    if rut in accounts:
        print("\n⚠️ Este RUT ya fue registrado. Por favor, intenta con otro.\n")
        return

    # 2. Pedimos una contraseña
    password = input("🔑 Ingresa una contraseña de 4 dígitos: ")

    # 3. Creamos la estructura completa del nuevo cliente
    accounts[rut] = {
        "password": password,
        "accounts": {
            "corriente": {"balance": 0},
            "vista": {"balance": 0},
            "ahorro": {"balance": 0}
        }
    }

    # 4. Confirmamos que todo salió bien
    print("\n✅ Cuenta creada exitosamente. Ya puedes iniciar sesión.\n")

def main():
    while True:
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print('Bienvenido al Cajero ATM de "PyTrustBank International ™"')
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
        print("Seleccione el número indicado en la acción que desea realizar:\n")
        print("1. Iniciar sesión")
        print("2. Crear una cuenta nueva")
        print("3. Salir")

        choice = input("\nSelecciona una opción: ")

        if choice == "1":
            print("\n🔐 Funcionalidad de inicio de sesión aún no implementada.\n")
        elif choice == "2":
            rut = input("🪪 Ingresa tu RUT chileno: ")
            create_account(rut)
        elif choice == "3":
            print("\n👋🏻 Gracias por preferir PyTrustBank International ™. ¡Hasta la próxima!\n")
            break
        else:
            print("\n❌ Opción inválida. Por favor, elige una opción válida.\n")


main()

