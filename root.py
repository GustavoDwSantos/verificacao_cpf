import tkinter as tk
from tkinter.messagebox import showinfo

from verificador_cpf import valida_cpf

root = tk.Tk()

root.title("Verificador de CPF")

altura_janela = 100
largura_janela = 200

root.geometry(f"{largura_janela}x{altura_janela}")

def clique_botao():
    if valida_cpf(cpf.get()) == True:
        showinfo(
            title= "Verificador de CPF",
            message="CPF Valido"
        )
    else: 
        showinfo(title="Verificador de CPF", message="CPF Invalido")
         


cpf = tk.StringVar()

caixa_texto = tk.Entry(root, textvariable=cpf)
caixa_texto.pack()



botao = tk.Button(root, text='Verificar CPF', command= clique_botao)
botao.pack()

root.mainloop()