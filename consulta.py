from tkinter import *
import subprocess

def volver_menu():
    saldo_window.destroy()  # Cierra esta ventana
    subprocess.Popen(["python", "menu.py"])  # Abre el menú

saldo_window = Tk()
saldo_window.title("Cajero - Consulta de dinero")
saldo_window.geometry("800x500")
saldo_window.configure(bg="#0056A0")

Label(saldo_window,text="saldo disponible", font=("Arial",16), fg="white", bg="#0056A0").pack(pady=20)

saldo_Label = Label(saldo_window, text="$XXXX.XX", font=("Arial",20,"bold"), fg="yellow", bg="#0056A0")
saldo_Label.pack(pady=10)

Button(saldo_window, text="Menu principal", font=("Arial",20), command=volver_menu).pack(pady=20)

# Mantiene la ventana abierta
saldo_window.mainloop()
