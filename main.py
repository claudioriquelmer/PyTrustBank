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


def login(rut):

    # 1. Pedimos la contraseña al usuario
    password = input("🔐 Ingresa tu contraseña (4 dígitos): ")

    # 2. Verificamos credenciales
    if rut in accounts and accounts[rut]["password"] == password:
        return True

    # 3. Mensaje de error si las credenciales fallan
    else:
        print("\n❌ Credenciales incorrectas. Intenta nuevamente.\n")
        return False

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
            rut = input("🪪 Ingresa tu RUT chileno: ")

            if rut in accounts and login(rut):
                total_balance = 0
                total_balance += accounts[rut]['accounts']['corriente']['balance']
                total_balance += accounts[rut]['accounts']['vista']['balance']
                total_balance += accounts[rut]['accounts']['ahorro']['balance']

                print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                print(f"🏦 Bienvenido RUN: {rut}")
                print(f"💰 Saldo total: {total_balance} CLP")
                print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                print("Seleccione la cuenta con la que desea operar:\n")
                print("1. Corriente")
                print("2. Vista")
                print("3. Ahorro")
                print("4. Cerrar sesión")

                account_option = input("\nSelecciona un tipo de cuenta (1/2/3/4): ")

                if account_option in ["1", "2", "3"]:
                    account_type = ["corriente", "vista", "ahorro"][int(account_option) - 1]
                    print(f"\n✅ Has seleccionado tu cuenta {account_type}. (Aquí continuará en la Parte V)\n")

                elif account_option == "4":
                    print("\n🔒 Has cerrado sesión correctamente. Volviendo al menú principal...\n")

                else:
                    print("❌ Opción inválida para cuenta. Volviendo al menú principal.\n")

            else:
                print("❌ No se pudo iniciar sesión. Volviendo al menú principal.\n")

        elif choice == "2":
            rut = input("🪪 Ingresa tu RUT chileno: ")
            create_account(rut)

        elif choice == "3":
            print("\n👋🏻 Gracias por preferir PyTrustBank International ™. ¡Hasta la próxima!\n")
            break

        else:
            print("\n❌ Opción inválida. Por favor, elige una opción válida.\n")


main()

