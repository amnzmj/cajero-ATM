from tkinter import *
import subprocess

def abrir_retiro():
    menu_window.quit()
    subprocess.Popen(["python","retiro.py"])

def abrir_saldo():
    menu_window.quit()
    subprocess.Popen(["python","saldo.py"])

def abrir_deposito():
    menu_window.quit()
    subprocess.Popen(["python","deposito.py"])

# Ventana del menú del cajero
menu_window = Tk()
menu_window.title("Menu")
menu_window.geometry("800x500")
menu_window.configure(bg="#0056A0")

Label(menu_window, text="Bienvenido al Cajero", font=("Arial", 20, "bold"), fg="white", bg="#0056A0").pack(pady=20)

Button(menu_window, text="Retirar Dinero", font=("Arial", 14), width=20, command=abrir_retiro).pack(pady=10)
Button(menu_window, text="Consultar Saldo", font=("Arial", 14), width=20, command=abrir_saldo).pack(pady=10)
Button(menu_window, text="Depositar Dinero", font=("Arial", 14), width=20, command=abrir_deposito).pack(pady=10)
Button(menu_window, text="Salir", font=("Arial", 14), width=20, fg="white", bg="red", command=menu_window.quit).pack(pady=20)

menu_window.mainloop()
