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
            print("\n📄 Funcionalidad de registro aún no implementada.\n")
        elif choice == "3":
            print("\n👋🏻 Gracias por preferir PyTrustBank International ™. ¡Hasta la próxima!\n")
            break
        else:
            print("\n❌ Opción inválida. Por favor, elige una opción válida.\n")


main()

