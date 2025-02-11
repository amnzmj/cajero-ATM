from tkinter import *
import subprocess

def confirmar():
    """
    confirma el retiro y abre la ventana de "completado".
    
    simula que el retiro
    ha sido realizado.

    :return: None
    """
    retiro_window.destroy()
    subprocess.Popen(["python","completado.py"])

def volver_menu():
    """
    cierra la ventana actual y vuelve al menú principal.


    :return: None
    """
    retiro_window.destroy()  # Cierra esta ventana
    subprocess.Popen(["python", "menu.py"])  # Abre el menú

# Ventana para el retiro de dinero
retiro_window = Tk()
retiro_window.title("Cajero - Retiro de Dinero")
retiro_window.geometry("800x500")
retiro_window.configure(bg="#0056A0")

Label(retiro_window, text="Ingresar el monto a retirar", font=("Arial",16), fg="white",bg="#0056A0").pack(pady=20)
monto_retiro = Entry(retiro_window, font=("Arial",16)).pack(pady=10)
boton_confirmar_retiro =Button(retiro_window, text="Confirmar", font=("Arial",14), command=confirmar).pack(pady=20)
boton_volver_menu = Button(retiro_window, text="Menu principal", font=("Arial",14), command=volver_menu).pack(pady=20)

# Mantiene la ventana abierta
retiro_window.mainloop()
