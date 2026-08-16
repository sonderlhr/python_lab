import tkinter as tk
from calculadora import calcular

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("320x450")
janela.configure(bg="#121212")

visor = tk.Entry(
    janela,
    font=("Arial", 24),
    justify="right",
    bg="#1C1C1C",
    fg="white",
    bd=0
)

visor.pack(fill="x", padx=10, pady=15)

def adicionar(valor):
    visor.insert(tk.END, valor)

linha1 = tk.Frame(janela, bg="#121212")
linha1.pack()

tk.Button(linha1, text="7", width=5, height=2,
        font=("Arial", 18),
        bg="#333333",
        fg="white",
        activebackground="#444444",
        activeforeground="white",
        command=lambda: adicionar("7")).pack(side="left", padx=4, pady=4)

tk.Button(linha1, text="8", width=5, height=2,
        font=("Arial", 18),
        bg="#333333",
        fg="white",
        activebackground="#444444",
        activeforeground="white",
        command=lambda: adicionar("8")).pack(side="left", padx=4, pady=4)

tk.Button(linha1, text="9", width=5, height=2,
        font=("Arial", 18),
        bg="#333333",
        fg="white",
        activebackground="#444444",
        activeforeground="white",
        command=lambda: adicionar("9")).pack(side="left", padx=4, pady=4)

tk.Button(linha1, text="+", width=5, height=2,
          font=("Arial", 18),
          bg="#FF9500",
          fg="white",
          activebackground="#CC7700",
          activeforeground="white",
          command=lambda: adicionar("+")).pack(side="left", padx=4, pady=4)

linha2 = tk.Frame(janela, bg="#121212")
linha2.pack()

tk.Button(linha2, text="4", width=5, height=2,
          font=("Arial", 18),
          bg="#333333",
          fg="white",
          activebackground="#444444",
          activeforeground="white",
          command=lambda: adicionar("4")).pack(side="left", padx=4, pady=4)

tk.Button(linha2, text="5", width=5, height=2,
          font=("Arial", 18),
          bg="#333333",
          fg="white",
          activebackground="#444444",
          activeforeground="white",
          command=lambda: adicionar("5")).pack(side="left", padx=4, pady=4)

tk.Button(linha2, text="6", width=5, height=2,
          font=("Arial", 18),
          bg="#333333",
          fg="white",
          activebackground="#444444",
          activeforeground="white",
          command=lambda: adicionar("6")).pack(side="left", padx=4, pady=4)

tk.Button(linha2, text="-", width=5, height=2,
          font=("Arial", 18),
          bg="#FF9500",
          fg="white",
          activebackground="#CC7700",
          activeforeground="white",
          command=lambda: adicionar("-")).pack(side="left", padx=4, pady=4)

linha3 = tk.Frame(janela, bg="#121212")
linha3.pack()

tk.Button(linha3, text="1", width=5, height=2,
          font=("Arial", 18),
          bg="#333333",
          fg="white",
          activebackground="#444444",
          activeforeground="white",
          command=lambda: adicionar("1")).pack(side="left", padx=4, pady=4)

tk.Button(linha3, text="2", width=5, height=2,
          font=("Arial", 18),
          bg="#333333",
          fg="white",
          activebackground="#444444",
          activeforeground="white",
          command=lambda: adicionar("2")).pack(side="left", padx=4, pady=4)

tk.Button(linha3, text="3", width=5, height=2,
          font=("Arial", 18),
          bg="#333333",
          fg="white",
          activebackground="#444444",
          activeforeground="white",
          command=lambda: adicionar("3")).pack(side="left", padx=4, pady=4)

tk.Button(linha3, text="*", width=5, height=2,
          font=("Arial", 18),
          bg="#FF9500",
          fg="white",
          activebackground="#CC7700",
          activeforeground="white",
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
            n1, n2 = expressao.split("-")
            r = calcular(float(n1), float(n2), "-")

        elif "*" in expressao:
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
        visor.insert(0, "Erro")

linha4 = tk.Frame(janela, bg="#121212")
linha4.pack()

tk.Button(linha4, text="C", width=5, height=2,
          font=("Arial", 18),
          bg="#D9534F",
          fg="white",
          activebackground="#B52B27",
          activeforeground="white",
          command=limpar).pack(side="left", padx=4, pady=4)

tk.Button(linha4, text="0", width=5, height=2,
          font=("Arial", 18),
          bg="#333333",
          fg="white",
          activebackground="#444444",
          activeforeground="white",
          command=lambda: adicionar("0")).pack(side="left", padx=4, pady=4)

tk.Button(linha4, text="=", width=5, height=2,
          font=("Arial", 18),
          bg="#28A745",
          fg="white",
          activebackground="#1E7E34",
          activeforeground="white",
          command=resultado).pack(side="left", padx=4, pady=4)

tk.Button(linha4, text="/", width=5, height=2,
          font=("Arial", 18),
          bg="#FF9500",
          fg="white",
          activebackground="#CC7700",
          activeforeground="white",
          command=lambda: adicionar("/")).pack(side="left", padx=4, pady=4)

tk.Button(linha4, text="=", width=5, height=2,
          font=("Arial", 18),
          bg="#28A745",
          fg="white",
          activebackground="#1E7E34",
          activeforeground="white",
          command=resultado).pack(side="left", padx=4, pady=4)



janela.mainloop()