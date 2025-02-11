from banco import Banco

class CajeroAutomatico:
    def __init__(self, banco):
        self.__banco = banco
        self.__cuenta_actual = None

    def autenticar_usuario(self, numero_cuenta, pin):
        cuenta = self.__banco.obtener_cuenta(numero_cuenta)
        if cuenta and cuenta.verificar_pin(pin):
            self.__cuenta_actual = cuenta
            return True
        return False

    def depositar(self, cantidad):
        if self.__cuenta_actual:
            self.__cuenta_actual.depositar(cantidad)
            return f"Depósito de ${cantidad} exitoso."
        return "Error: No hay cuenta autenticada."

    def retirar(self, cantidad):
        if self.__cuenta_actual:
            if self.__cuenta_actual.retirar(cantidad):
                return f"Retiro de ${cantidad} exitoso."
            return "Fondos insuficientes."
        return "Error: No hay cuenta autenticada."

    def consultar_saldo(self):
        if self.__cuenta_actual:
            return f"Saldo actual: ${self.__cuenta_actual.obtener_saldo()}."
        return "Error: No hay cuenta autenticada."

    def transferir(self, numero_cuenta_destino, cantidad):
        if self.__cuenta_actual:
            cuenta_destino = self.__banco.obtener_cuenta(numero_cuenta_destino)
            if cuenta_destino:
                if self.__cuenta_actual.transferir(cuenta_destino, cantidad):
                    return f"Transferencia de ${cantidad} exitosa."
                return "Fondos insuficientes."
            return "Cuenta destino no encontrada."
        return "Error: No hay cuenta autenticada."
