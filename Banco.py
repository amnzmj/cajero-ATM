from cuenta import Cuenta

class Banco:
    def __init__(self):
        self.__cuentas = {}

    def agregar_cuenta(self, cuenta):
        self.__cuentas[cuenta.obtener_numero_cuenta()] = cuenta

    def obtener_cuenta(self, numero_cuenta):
        return self.__cuentas.get(numero_cuenta)
