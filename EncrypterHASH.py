import tkinter as tk
from tkinter import ttk

def simple_hash(input_string):
    hash_value = 0
    for character in input_string:
        hash_value += ord(character)
        hash_value = (hash_value * 17) % 1024
    return hash_value

def compute_hash():
    input_string = text_entry.get()
    hash_result = simple_hash(input_string)
    result_label.config(text=f"Hash: {hash_result}")

# Configuracoes da janela
root = tk.Tk()
root.title("Simple Hash Function")
root.geometry("350x200")
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12))

# Criando widgets
text_label = ttk.Label(root, text="Digite o texto:")
text_entry = ttk.Entry(root, width=30)

button = ttk.Button(root, text="Calcular Hash", command=compute_hash)
result_label = ttk.Label(root, text="Hash: ")

# Posicionando os widgets
text_label.pack(pady=5)
text_entry.pack(pady=5)
button.pack(pady=10)
result_label.pack(pady=5)

# Executando a aplicacao
root.mainloop()
