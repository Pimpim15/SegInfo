import tkinter as tk
from tkinter import ttk

def calculate_keys(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return e, d, n

def encrypt_decrypt():
    try:
        p = int(p_entry.get())
        q = int(q_entry.get())
        e = int(e_entry.get())
        num = int(number_entry.get())
        mode = mode_var.get()

        e, d, n = calculate_keys(p, q, e)

        if mode == 0:  # Encrypt
            result = pow(num, e, n)
        else:  # Decrypt
            result = pow(num, d, n)

        result_label.config(text=f"Resultado: {result}")
    except ValueError:
        result_label.config(text="Erro: Verifique a entrada de dados")

# Configuracoes da janela
root = tk.Tk()
root.title("RSA Encrypt/Decrypt")
root.geometry("300x250")
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))
style.configure('TRadiobutton', font=('Helvetica', 12))

# Criando widgets
p_label = ttk.Label(root, text="Valor de p:")
p_entry = ttk.Entry(root)

q_label = ttk.Label(root, text="Valor de q:")
q_entry = ttk.Entry(root)

e_label = ttk.Label(root, text="Valor de e:")
e_entry = ttk.Entry(root)

number_label = ttk.Label(root, text="Numero:")
number_entry = ttk.Entry(root)

mode_var = tk.IntVar(value=0)
encrypt_rb = ttk.Radiobutton(root, text="Cifrar", variable=mode_var, value=0)
decrypt_rb = ttk.Radiobutton(root, text="Decifrar", variable=mode_var, value=1)

button = ttk.Button(root, text="Executar", command=encrypt_decrypt)
result_label = ttk.Label(root, text="Resultado: ")

# Posicionando os widgets
p_label.pack(pady=2)
p_entry.pack(pady=2)
q_label.pack(pady=2)
q_entry.pack(pady=2)
e_label.pack(pady=2)
e_entry.pack(pady=2)
number_label.pack(pady=2)
number_entry.pack(pady=2)
encrypt_rb.pack(pady=2)
decrypt_rb.pack(pady=2)
button.pack(pady=2)
result_label.pack(pady=2)

# Executando a aplicacao
root.mainloop()
