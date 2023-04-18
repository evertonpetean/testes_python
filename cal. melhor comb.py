import tkinter as tk

def calcular_melhor_combustivel():
    try:
        c1 = float(etanol_entry.get().replace(',', '.'))
        c2 = float(gasolina_entry.get().replace(',', '.'))
        if c1 <= 0 or c2 <= 0:
            raise ValueError('Os preços dos combustíveis devem ser números positivos.')
        r = round(c1/c2, 1)
        if r >= 0.7:
            resultado_label.config(text=f"R = {r}\nCompensa abastecer com gasolina!")
        else:
            resultado_label.config(text=f"R = {r}\nCompensa abastecer com etanol!")
    except ValueError as e:
        resultado_label.config(text=f"Erro: {e}")

# Criar a janela principal
janela = tk.Tk()
janela.title('Melhor Opção')
janela.geometry('320x130')
# Criar os widgets
etanol_label = tk.Label(janela, text='Preço do Etanol:')
etanol_entry = tk.Entry(janela)
gasolina_label = tk.Label(janela, text='Preço da Gasolina:')
gasolina_entry = tk.Entry(janela)
calcular_button = tk.Button(janela, text='Calcular', command=calcular_melhor_combustivel)
resultado_label = tk.Label(janela, text='')

# Posicionar os widgets na janela
etanol_label.grid(row=0, column=0, sticky='NSEW', padx=10, pady=10)
etanol_entry.grid(row=0, column=1, sticky='NSEW', padx=10, pady=10)
gasolina_label.grid(row=1, column=0, sticky='NSEW', padx=10, pady=10)
gasolina_entry.grid(row=1, column=1, sticky='NSEW', padx=10, pady=10)
calcular_button.grid(row=2, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)
resultado_label.grid(row=3, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)

# Centralizar a janela
largura_janela = 300
altura_janela = 200
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2
janela.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

# Iniciar o loop de eventos da janela
janela.mainloop()
