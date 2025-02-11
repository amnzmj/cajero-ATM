from tkinter import *
import subprocess

def abrir_menu():
    main_window.quit()
    subprocess.Popen(["python", "menu.py"])

# Ventana del ingreso de cuenta
main_window = Tk()
main_window.title("ATM")
main_window.geometry("800x500")
main_window.configure(bg='#0074D9')

Label(main_window, text="Ingresa Cuenta y PIN", font=("Arial",20,"bold"), fg="white", bg="#0056A0").pack(pady=10)

Label(main_window, text="Numero de Cuenta:", font=("Arial", 20), fg="white", bg="#0056A0").pack(pady=10)
entrada_cuenta = Entry(main_window, font=("Arial",14)).pack(pady=20)

Label(main_window, text="PIN:", font=("Arial", 20), fg="white", bg="#0056A0").pack(pady=10)
entrada_PIN = Entry(main_window, font=("Arial",14), show="*").pack(pady=20)

boton_ingresar_cuenta = Button(main_window, text="INGRESAR", font=("Arial",20), width=20, command=abrir_menu).pack(pady=10)

# Mantiene la ventana abierta
main_window.mainloop()


