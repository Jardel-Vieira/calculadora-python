import tkinter as tk

# Função para inserir números/operações no visor
def inserir_numero(numero):
    atual = visor.get()
    visor.delete(0, tk.END)
    visor.insert(0, atual + str(numero))

# Função para calcular o resultado
def calcular():
    try:
        expressao = visor.get()
        resultado = eval(expressao)  # Avalia a expressão matemática
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except Exception as e:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

# Função para limpar o visor
def limpar():
    visor.delete(0, tk.END)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x600")
janela.resizable(False, False)  # Impede redimensionamento

# Visor (campo de entrada)
visor = tk.Entry(janela, font=("Arial", 24), justify="right", bd=10, bg="#f0f0f0")
visor.pack(pady=20, padx=10, fill="x")

# Frame para os botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack()

# Botões numéricos (0-9) e ponto decimal
botoes_numericos = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
    ("0", 3, 0), (".", 3, 1)
]

for (texto, linha, coluna) in botoes_numericos:
    botao = tk.Button(
        frame_botoes, text=texto, font=("Arial", 18), width=5, height=2,
        bg="#e0e0e0", command=lambda t=texto: inserir_numero(t)
    )
    botao.grid(row=linha, column=coluna, padx=5, pady=5)

# Botões de operações (+, -, *, /)
botoes_operacoes = [
    ("+", 0, 3), ("-", 1, 3),
    ("*", 2, 3), ("/", 3, 3)
]

for (texto, linha, coluna) in botoes_operacoes:
    botao = tk.Button(
        frame_botoes, text=texto, font=("Arial", 18), width=5, height=2,
        bg="#ff9900", fg="white", command=lambda t=texto: inserir_numero(t)
    )
    botao.grid(row=linha, column=coluna, padx=5, pady=5)

# Botão de igual (=)
botao_igual = tk.Button(
    frame_botoes, text="=", font=("Arial", 18), width=5, height=2,
    bg="#4CAF50", fg="white", command=calcular
)
botao_igual.grid(row=3, column=2, padx=5, pady=5)

# Botão de limpar (C)
botao_limpar = tk.Button(
    frame_botoes, text="C", font=("Arial", 18), width=12, height=2,
    bg="#f44336", fg="white", command=limpar
)
botao_limpar.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="we")

# Botão de saída (opcional)
botao_sair = tk.Button(
    frame_botoes, text="Sair", font=("Arial", 18), width=5, height=2,
    bg="#333333", fg="white", command=janela.quit
)
botao_sair.grid(row=4, column=3, padx=5, pady=5)

# Mantém a janela aberta
janela.mainloop()