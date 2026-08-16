import tkinter as tk
from calculadora import calcular

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("320x450")
janela.configure(bg="gray15")

visor = tk.Entry(
    janela,
    font=("Arial", 24),
    justify="right",
    bg="gray20",
    fg="white",
    bd=0
)

visor.pack(fill="x", padx=10, pady=15)

def adicionar(valor):
    visor.insert(tk.END, valor)
linha1 = tk.Frame(janela, bg="gray15")
linha1.pack()

tk.Button(linha1, text="7", width=5, height=2,
        font=("Arial", 18),
        command=lambda: adicionar("7")).pack(side="left", padx=4, pady=4)

tk.Button(linha1, text="8", width=5, height=2,
        font=("Arial", 18),
        command=lambda: adicionar("8")).pack(side="left", padx=4, pady=4)

tk.Button(linha1, text="9", width=5, height=2,
        font=("Arial", 18),
        command=lambda: adicionar("9")).pack(side="left", padx=4, pady=4)

tk.Button(linha1, text="+", width=5, height=2,
          font=("Arial", 18),
          command=lambda: adicionar("+")).pack(side="left", padx=4, pady=4)

linha2 = tk.Frame(janela, bg="gray15")
linha2.pack()

tk.Button(linha2, text="4", width=5, height=2,
          font=("Arial", 18),
          command=lambda: adicionar("4")).pack(side="left", padx=4, pady=4)

tk.Button(linha2, text="5", width=5, height=2,
          font=("Arial", 18),
          command=lambda: adicionar("5")).pack(side="left", padx=4, pady=4)

tk.Button(linha2, text="6", width=5, height=2,
          font=("Arial", 18),
          command=lambda: adicionar("6")).pack(side="left", padx=4, pady=4)

tk.Button(linha2, text="-", width=5, height=2,
          font=("Arial", 18),
          command=lambda: adicionar("-")).pack(side="left", padx=4, pady=4)

linha3 = tk.Frame(janela, bg="gray15")
linha3.pack()

tk.Button(linha3, text="1", width=5, height=2,
          font=("Arial", 18),
          command=lambda: adicionar("1")).pack(side="left", padx=4, pady=4)

tk.Button(linha3, text="2", width=5, height=2,
          font=("Arial", 18),
          command=lambda: adicionar("2")).pack(side="left", padx=4, pady=4)

tk.Button(linha3, text="3", width=5, height=2,
          font=("Arial", 18),
          command=lambda: adicionar("3")).pack(side="left", padx=4, pady=4) 

tk.Button(linha3, text= "*", width=5, height=2,
          font=("Arial", 18),
          command=lambda: adicionar("*")).pack(side="left", padx=4, pady=4)

def limpar():
    visor.delete(0, tk.END)

def resultado():
    try:
        expressao = visor.get()

        if "+" in expressao:
            n1, n2 = expressao.split("+")
            r = calcular(float(n1), float(n2), "+")

        elif "-" in expressao:
            n1, n2 = expressao.split("=")
            r =  calcular(float(n1), float(n2), "-")

        elif "*" in expressao:
            n1, n2 = expressao.split("*")
            r = calcular(float(n1), float(n2), "*")

        elif "/" in expressao: 
            n1, n2 = expressao.split("*")
            r = calcular(float(n1), float(n2), "*")

        elif "/" in expressao:
            n1, n2 = expressao.split("/")
            r = calcular(float(n1), float(n2), "/")

        else: 
            r = "Erro"

        visor.delete(0, tk.END)
        visor.insert(0, str(r))

    except:
        visor.delete(0, tk.END)
        visor.insert(0, )           

linha4 = tk.Frame(janela, bg="gray15")
linha4.pack()

tk.Button(linha4, text="C", width=5, height=2,
         font=("Arial", 18),
         command=limpar).pack(side="left", padx=4, pady=4)

tk.Button(linha4, text="0", width=5, height=2,
          font=("Arial", 18),
          command=lambda: adicionar("0")).pack(side="left", padx=4, pady=4)

tk.Button(linha4, text=".", width=5, height=2,
          font=("Arial", 18),
          command=lambda: adicionar(".")).pack(side="left", padx=4, pady=4)

tk.Button(linha4, text="=", width=5, height=2, 
          font=("Arial", 18), 
          command=resultado).pack(side="left", padx=4, pady=4)


janela.mainloop()