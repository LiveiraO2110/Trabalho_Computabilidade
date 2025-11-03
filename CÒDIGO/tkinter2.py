import tkinter as tk
from tkinter import messagebox

def caminhos(indice):
    try:
        estadosstr = estados_var.get()
        total_estados = int(estadosstr)
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido de estados!")
        return

    if indice >= total_estados:
        messagebox.showinfo("Concluído", "Todos os caminhos foram preenchidos!")
        retornarDados()

    proximo(indice)

def proximo(indice):
    janela = tk.Toplevel(root)
    janela.title(f"Caminhos - q{indice}")
    janela.geometry("300x200")

    frame = tk.Frame(janela)
    frame.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

    janela.columnconfigure(0, weight=1)
    janela.rowconfigure(0, weight=1)

    entrada_var = tk.StringVar()

    tk.Label(frame, text=f"Digite o(s) caminho(s) a partir de q{indice}:").grid(
        row=0, column=0, sticky="w", padx=5, pady=5
    )
    tk.Entry(frame, textvariable=entrada_var).grid(
        row=1, column=0, sticky="ew", padx=5, pady=5
    )

    def avancar():
        valor = entrada_var.get()
        valores = valor.split(",")

        for simbolo in valores:
            caminhosVet.append(f"q{indice},{simbolo}")

        print(f"q{indice} -> {valor}")
        janela.destroy()
        caminhos(indice + 1)

    tk.Button(frame, text="Próximo", command=avancar).grid(
        column=0, row=2, sticky="e", padx=5, pady=10
    )


def retornarDados():    
    alfabeto = alfabeto_var.get()
    estadosstr = estados_var.get()
    estados = int(estadosstr)
    listaEstados = []
    listaAlfabeto = []

    if alfabeto and estados:
        alfabeto = alfabeto.split(",")

        for simbolo in alfabeto:
            simbolo = simbolo.strip()
            if simbolo not in listaAlfabeto:
                listaAlfabeto.append(simbolo)

        for i in range(estados):
            listaEstados.append(f"q{i}")

        mensagem = f"Alfabeto -> {listaAlfabeto}\nEstados -> {listaEstados}"
        messagebox.showinfo("Sucesso", mensagem)
        telaMatriz(listaAlfabeto, caminhosVet)

def telaMatriz(alfabeto, estados):
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Matriz de Transições")
    nova_janela.geometry("700x400")

    frame = tk.Frame(nova_janela, padx=10, pady=10)
    frame.pack(fill="both", expand=True)

    for i in range(len(alfabeto) + 1):
        frame.rowconfigure(i, weight=1)
    for j in range(len(estados) + 1):
        frame.columnconfigure(j, weight=1)

    tk.Label(frame, text="").grid(row=0, column=0)
    for j, estado in enumerate(estados, start=1):
        tk.Label(frame, text=estado, borderwidth=1, relief="ridge").grid(
            row=0, column=j, sticky="nsew", padx=2, pady=2
        )

    entradas = {}
    for i, simbolo in enumerate(alfabeto, start=1):
        tk.Label(frame, text=simbolo, borderwidth=1, relief="ridge").grid(
            row=i, column=0, sticky="nsew", padx=2, pady=2
        )
        for j, estado in enumerate(estados, start=1):
            entry = tk.Entry(frame, justify="center")
            entry.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
            entradas[(simbolo, estado)] = entry

    return frame

root = tk.Tk()
root.title("Autômato com Pilha")
root.geometry("500x200")

alfabeto_var = tk.StringVar()
estados_var = tk.StringVar()
caminhosVet = []

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

tk.Label(frame, text="Digite o alfabeto de entrada").grid(row=0, column=0, sticky="w")
tk.Entry(frame, textvariable=alfabeto_var).grid(row=0, column=1, sticky="ew")

tk.Label(frame, text="Digite o número de estados").grid(row=1, column=0, sticky="w")
tk.Entry(frame, textvariable=estados_var).grid(row=1, column=1, sticky="ew")

tk.Button(frame, text="Próximo", command=lambda: caminhos(1)).grid(
    column=1, row=2, sticky="e", padx=5, pady=10
)

root.mainloop()