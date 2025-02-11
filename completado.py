from tkinter import *
import subprocess  

def volver_menu():
    """
    cierra la ventana actual y vuelve al menú principal.

    cierra la ventana de "Operación Exitosa"
    :return: None
    """
    confirmar_window.destroy()  
    subprocess.Popen(["python", "menu.py"])  

# Ventana de confirmación de operación exitosa
confirmar_window = Tk()
confirmar_window.title("Cajero - Operación Exitosa")
confirmar_window.geometry("400x300")
confirmar_window.configure(bg="#0056A0")

Label(confirmar_window, text="✅ Operación Exitosa", font=("Arial", 20, "bold"), fg="white", bg="#0056A0").pack(pady=40)
Label(confirmar_window, text="Redirigiendo al menú principal...", font=("Arial", 14), fg="yellow", bg="#0056A0").pack()

# Espera 3 segundos y vuelve al menú
confirmar_window.after(3000, volver_menu)

# Mantiene la ventana abierta
confirmar_window.mainloop()
