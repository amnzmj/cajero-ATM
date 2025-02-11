from tkinter import *
import subprocess

# Diccionario que contiene las cuentas de los usuarios, su nombre, saldo y PIN.
cuentas = {
    "12345678": {"nombre": "diego", "saldo": 5000, "pin": "1234"},
    "87654321": {"nombre": "dani", "saldo": 3000, "pin": "8888"},
}

def abrir_menu():
    """
    Función que abre el menú del cajero automático después de verificar el número de cuenta
    y el PIN ingresados.

    valida si el número de cuenta y el PIN coinciden 
    datos almacenados en el diccionario `cuentas`.
    
    :return: None
    """
    numero_cuenta = entrada_cuenta.get()
    pin = entrada_PIN.get()

    # Validar cuenta y PIN
    if numero_cuenta in cuentas and cuentas[numero_cuenta]["pin"] == pin:
        main_window.quit()
        subprocess.Popen(["python", "menu.py"])  # Abre el menú si los datos son correctos
    else:
        etiqueta_error.config(text="Cuenta o PIN incorrectos", fg="white")

# Ventana del ingreso de cuenta
main_window = Tk()
main_window.title("ATM")
main_window.geometry("800x500")
main_window.configure(bg='#0074D9')

Label(main_window, text="Ingresa Cuenta y PIN", font=("Arial", 20, "bold"), fg="white", bg="#0056A0").pack(pady=10)

Label(main_window, text="Número de Cuenta:", font=("Arial", 20), fg="white", bg="#0056A0").pack(pady=10)
entrada_cuenta = Entry(main_window, font=("Arial", 14))
entrada_cuenta.pack(pady=10)

Label(main_window, text="PIN:", font=("Arial", 20), fg="white", bg="#0056A0").pack(pady=10)
entrada_PIN = Entry(main_window, font=("Arial", 14), show="*")
entrada_PIN.pack(pady=10)

boton_ingresar_cuenta = Button(main_window, text="INGRESAR", font=("Arial", 20), width=20, command=abrir_menu)
boton_ingresar_cuenta.pack(pady=10)

# Etiqueta para mostrar errores
etiqueta_error = Label(main_window, text="", font=("Arial", 14), fg="red", bg="#0074D9")
etiqueta_error.pack(pady=10)

# Mantiene la ventana abierta
main_window.mainloop()