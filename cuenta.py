class Cuenta:
    def __init__(self, numero_cuenta, pin, saldo=0):
        self.__numero_cuenta = numero_cuenta
        self.__pin = pin
        self.__saldo = saldo

    def verificar_pin(self, pin):
        return self.__pin == pin

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            return False  # Fondos insuficientes
        self.__saldo -= cantidad
        return True

    def obtener_saldo(self):
        return self.__saldo

    def transferir(self, cuenta_destino, cantidad):
        if self.retirar(cantidad):
            cuenta_destino.depositar(cantidad)
            return True
        return False

    def obtener_numero_cuenta(self):
        return self.__numero_cuenta
