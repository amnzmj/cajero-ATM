import subprocess
import tkinter as tk
from atm_backend import autenticar_usuario, realizar_deposito, realizar_retiro, consultar_saldo, realizar_transferencia

def abrir_menu():
    numero_cuenta = entrada_cuenta.get()
    pin = entrada_PIN.get()
    if autenticar_usuario(int(numero_cuenta), pin):
        main_window.quit()
        subprocess.Popen(["python", "menu.py"])
    else:
        error_label.config(text="Cuenta o PIN incorrectos", fg="red")

main_window = tk.Tk()
main_window.title("ATM")
main_window.geometry("400x300")
main_window.configure(bg='#0074D9')

tk.Label(main_window, text="Número de Cuenta:", font=("Arial", 14), bg="#0074D9", fg="white").pack(pady=5)
entrada_cuenta = tk.Entry(main_window, font=("Arial", 14))
entrada_cuenta.pack()

tk.Label(main_window, text="PIN:", font=("Arial", 14), bg="#0074D9", fg="white").pack(pady=5)
entrada_PIN = tk.Entry(main_window, font=("Arial", 14), show="*")
entrada_PIN.pack()

error_label = tk.Label(main_window, text="", font=("Arial", 12), bg="#0074D9")
error_label.pack()

tk.Button(main_window, text="Ingresar", font=("Arial", 14), command=abrir_menu).pack(pady=10)

main_window.mainloop()
