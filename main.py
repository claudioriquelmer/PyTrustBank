# 🏦 Estructura de Datos de Usuarios en Memoria
accounts = {
    '20123123-K': {
        'password': '1234',
        'accounts': {
            'corriente': {'balance': 10000},
            'vista': {'balance': 25000},
            'ahorro': {'balance': 30000}
        }
    },
    '12345678-9': {
        'password': '1234',
        'accounts': {
            'corriente': {'balance': 0},
            'vista': {'balance': 0},
            'ahorro': {'balance': 0}
        }
    }
}

# 🧩 Registrar nuevos usuarios
def create_account(rut):
    if rut in accounts:
        print("\n⚠️ Este RUT ya fue registrado. Por favor, intenta con otro.\n")
        return

    password = input("🔑 Ingresa una contraseña de 4 dígitos: ")
    accounts[rut] = {
        "password": password,
        "accounts": {
            "corriente": {"balance": 0},
            "vista": {"balance": 0},
            "ahorro": {"balance": 0}
        }
    }
    print("\n✅ Cuenta creada exitosamente. Ya puedes iniciar sesión.\n")

# 🔐 Función de login
def login(rut):
    password = input("🔐 Ingresa tu contraseña (4 dígitos): ")
    if rut in accounts and accounts[rut]["password"] == password:
        return True
    else:
        print("\n❌ Credenciales incorrectas. Intenta nuevamente.\n")
        return False

# 💰 Función de depósito
def deposit(rut, account_type):
    amount = float(input("💰 Ingresa el monto a depositar (CLP): "))
    accounts[rut]["accounts"][account_type]["balance"] += amount
    nuevo_saldo = accounts[rut]["accounts"][account_type]["balance"]
    print(f"\n✅ Depósito exitoso. Nuevo saldo: {nuevo_saldo} CLP\n")

# 💸 Función de retiro
def withdraw(rut, account_type):
    amount = float(input("💸 Ingresa el monto a retirar (CLP): "))
    current_balance = accounts[rut]["accounts"][account_type]["balance"]

    if amount <= current_balance:
        accounts[rut]["accounts"][account_type]["balance"] -= amount
        nuevo_saldo = accounts[rut]["accounts"][account_type]["balance"]
        print(f"\n✅ Retiro exitoso. Nuevo saldo: {nuevo_saldo} CLP\n")
    else:
        print("\n❌ Saldo insuficiente para realizar esta operación.\n")

# 🎯 Menú principal del cajero
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

                while True:
                    print("Seleccione la cuenta con la que desea operar:\n")
                    print("1. Corriente")
                    print("2. Vista")
                    print("3. Ahorro")
                    print("4. Cerrar sesión")

                    account_option = input("\nSelecciona un tipo de cuenta (1/2/3/4): ")

                    if account_option in ["1", "2", "3"]:
                        account_type = ["corriente", "vista", "ahorro"][int(account_option) - 1]
                        print(f"\n✅ Has seleccionado tu cuenta {account_type}.\n")

                        # Menú de operaciones bancarias dentro de la cuenta seleccionada
                        while True:
                            print("\n🔧 ¿Qué deseas hacer con tu cuenta?\n")
                            print("1. Consultar saldo")
                            print("2. Realizar depósito")
                            print("3. Realizar retiro")
                            print("4. Cambiar de cuenta")
                            print("5. Cerrar sesión")

                            action = input("\nSelecciona una opción: ")

                            if action == "1":
                                saldo = accounts[rut]["accounts"][account_type]["balance"]
                                print(f"\n💳 Saldo actual de tu cuenta {account_type}: {saldo} CLP\n")

                            elif action == "2":
                                deposit(rut, account_type)

                            elif action == "3":
                                withdraw(rut, account_type)

                            elif action == "4":
                                print("\n🔁 Volviendo al selector de cuentas...\n")
                                break  # Volver al selector de cuenta

                            elif action == "5":
                                print("\n🔒 Has cerrado sesión correctamente.\n")
                                break  # Cierra sesión y vuelve al menú principal

                            else:
                                print("❌ Opción inválida. Intenta nuevamente.\n")

                    elif account_option == "4":
                        print("\n🔒 Has cerrado sesión correctamente. Volviendo al menú principal...\n")
                        break  # Cierra sesión

                    else:
                        print("❌ Opción inválida para cuenta. Intenta nuevamente.\n")

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

# 🚀 Ejecutar el sistema
main()


