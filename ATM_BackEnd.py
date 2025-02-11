from banco import Banco
from cajero import CajeroAutomatico
from cuenta import Cuenta

# Crear el banco y agregar cuentas de prueba
banco = Banco()
banco.agregar_cuenta(Cuenta(1234, "5678", 10000))
banco.agregar_cuenta(Cuenta(4321, "1234", 5000))

# Crear el cajero automático
cajero = CajeroAutomatico(banco)

def autenticar_usuario(numero_cuenta, pin):
    return cajero.autenticar_usuario(numero_cuenta, pin)

def realizar_deposito(cantidad):
    return cajero.depositar(cantidad)

def realizar_retiro(cantidad):
    return cajero.retirar(cantidad)

def consultar_saldo():
    return cajero.consultar_saldo()

def realizar_transferencia(cuenta_destino, cantidad):
    return cajero.transferir(cuenta_destino, cantidad)
