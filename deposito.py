from tkinter import *
import subprocess

def confirmar():
    deposito_window.destroy()
    subprocess.Popen(["python","completado.py"])

def volver_menu():
    deposito_window.destroy()  # Cierra esta ventana
    subprocess.Popen(["python", "menu.py"])  # Abre el menú

deposito_window = Tk()
deposito_window.title("Cajero - Deposito de dinero")
deposito_window.geometry("800x500")
deposito_window.configure(bg="#0056A0")

Label(deposito_window, text="Ingresa el monto a depositar", font=("Arial",20), fg="white", bg="#0056A0").pack(pady=20)
monto_deposito = Entry(deposito_window, font=("Arial",20)).pack(pady=10)
boton_confirmar_deposito = Button(deposito_window, text="Confirmar", font=("Arial",14), command=confirmar).pack(pady=20)
boton_volver = Button(deposito_window, text="Menu principal", font=("Arial",14), command= volver_menu).pack(pady=20)

# Mantiene la ventana abierta
deposito_window.mainloop()