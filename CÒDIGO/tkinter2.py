import tkinter as tk
from tkinter import messagebox

def caminhos(indice):
    try:
        total_estados = int(estados_var.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido de estados!")
        return

    if indice >= total_estados:
        messagebox.showinfo("Concluído", "Todos os caminhos foram preenchidos!")
        retornarDados()
        return

    proximo(indice)

def proximo(indice):
    janela = tk.Toplevel(root)
    janela.title(f"Caminhos - q{indice}")
    janela.geometry("300x200")

    frame = tk.Frame(janela)
    frame.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

    entrada_var = tk.StringVar()

    tk.Label(frame, text=f"Digite o(s) caminho(s) a partir de q{indice}:").grid(
        row=0, column=0, sticky="ew", padx=5, pady=5
    )
    tk.Entry(frame, textvariable=entrada_var).grid(
        row=1, column=0, sticky="ew", padx=5, pady=5
    )

    def avancar():
        valor = entrada_var.get().strip()
        if not valor:
            messagebox.showwarning("Aviso", "Digite ao menos um caminho.")
            return

        valores = [v.strip() for v in valor.split(",") if v.strip()]
        for simbolo in valores:
            caminhosVet.append(f"q{indice},{simbolo}")

        print(f"q{indice} -> {valores}")
        janela.destroy()
        caminhos(indice + 1)

    tk.Button(frame, text="Próximo", command=avancar).grid(
        column=0, row=2, sticky="e", padx=5, pady=10
    )

def retornarDados():    
    alfabeto = alfabeto_var.get()
    try:
        estados = int(estados_var.get())
    except ValueError:
        messagebox.showerror("Erro", "Número de estados inválido!")
        return

    listaEstados = [f"q{i}" for i in range(1, estados + 1)]
    listaAlfabeto = [s.strip() for s in alfabeto.split(",") if s.strip()]

    mensagem = f"Alfabeto -> {listaAlfabeto}\nEstados -> {listaEstados}"
    messagebox.showinfo("Sucesso", mensagem)
    telaLista(caminhosVet)

def telaLista(caminhos):
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Valores das Transições")
    nova_janela.geometry("400x200")

    frame = tk.Frame(nova_janela, padx=10, pady=10)
    frame.pack(fill="both", expand=True)

    entradas = {}

    for j, estado in enumerate(caminhos):
        tk.Label(frame, text=estado, borderwidth=1, relief="ridge").grid(
            row=0, column=j, sticky="nsew", padx=2, pady=2
        )
        entry = tk.Entry(frame, justify="center")
        entry.grid(row=1, column=j, sticky="nsew", padx=2, pady=2)
        entradas[estado] = entry

    def guardar():
        dados = {estado: entry.get() for estado, entry in entradas.items()}
        saveEntrada(dados)
        nova_janela.destroy()

    tk.Button(frame, text="Guardar valores", command=guardar).grid(
        column=0, row=2, columnspan=len(caminhos), sticky="nsew", padx=5, pady=5
    )

def saveEntrada(entrada):
    print("Valores salvos:")
    for estado, valor in entrada.items():
        print(f"{estado} -> {valor}")

root = tk.Tk()
root.title("Autômato com Pilha")
root.geometry("500x200")

alfabeto_var = tk.StringVar()
estados_var = tk.StringVar()
caminhosVet = []

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

tk.Label(frame, text="Digite o alfabeto de entrada (ex: a,b,c)").grid(row=0, column=0, sticky="w")
tk.Entry(frame, textvariable=alfabeto_var).grid(row=0, column=1, sticky="ew")

tk.Label(frame, text="Digite o número de estados").grid(row=1, column=0, sticky="w")
tk.Entry(frame, textvariable=estados_var).grid(row=1, column=1, sticky="ew")

tk.Button(frame, text="Próximo", command=lambda: caminhos(1)).grid(
    column=1, row=2, sticky="e", padx=5, pady=10
)

root.mainloop()