import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la resistencia equivalente en serie
def resistencia_serie(LauA):
    return np.sum(LauA)

# Función para calcular la resistencia equivalente en paralelo
def resistencia_paralelo(LauA):
    return 1 / np.sum(1 / np.array(LauA))

# Función para validar las resistencias ingresadas
def validar_resistencias(entrada):
    try:
        LauA = [float(r) for r in entrada.split(',')]
        if not LauA:
            raise ValueError("Debe ingresar al menos una resistencia.")
        if any(r <= 0 for r in LauA):
            raise ValueError("Todas las resistencias deben ser mayores a 0.")
        return LauA
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")
        return None

# Función para calcular la resistencia equivalente según el tipo de conexión
def calcular_Lg_resistencia_equivalente():
    entrada = entrada_resistencias.get().strip()
    LauA = validar_resistencias(entrada)
    V_pedA = tipo.get()

    if LauA is None:
        return

    if V_pedA == "Serie":
        Lg_resistencia_eq = resistencia_serie(LauA)
    elif V_pedA == "Paralelo":
        Lg_resistencia_eq = resistencia_paralelo(LauA)
    else:
        messagebox.showerror("Error", "Seleccione el tipo de conexión.")
        return

    etiqueta_resultado.config(text=f"Resistencia Equivalente: {Lg_resistencia_eq:.2f} Ω")
    plot_resistencia_vs_num_resistencias(LauA, V_pedA)

# Función para graficar la resistencia equivalente vs número de resistencias
def plot_resistencia_vs_num_resistencias(LauA, V_pedA):
    resistencias_totales = []
    for i in range(1, len(LauA) + 1):
        if V_pedA == "Serie":
            Lv_res_eq = resistencia_serie(LauA[:i])
            L_color = 'blue'
        else:
            Lv_res_eq = resistencia_paralelo(LauA[:i])
            L_color = 'green'
        resistencias_totales.append(Lv_res_eq)

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(LauA) + 1), resistencias_totales, marker='o', L_color=L_color)
    plt.title(f"Resistencia Total vs Número de Resistencias ({V_pedA})")
    plt.xlabel("Número de Resistencias")
    plt.ylabel("Resistencia Equivalente (Ω)")
    plt.grid(True)
    plt.show()

# Función para limpiar la entrada y el resultado
def limpiar_formulario():
    entrada_resistencias.delete(0, tk.END)
    combo_tipo.set('')
    etiqueta_resultado.config(text="Resistencia Equivalente: ")

# Crear la interfaz de usuario con tkinter
ventana = tk.Tk()
ventana.title("Cálculo de Resistencia Equivalente")

# Entrada de resistencias
etiqueta_resistencias = ttk.Label(ventana, text="Ingresa las resistencias (separadas por coma):")
etiqueta_resistencias.grid(column=0, row=0, padx=10, pady=10)

entrada_resistencias = ttk.Entry(ventana)
entrada_resistencias.grid(column=1, row=0, padx=10, pady=10)

# Selección de tipo de conexión (serie o paralelo)
etiqueta_tipo = ttk.Label(ventana, text="Tipo de conexión:")
etiqueta_tipo.grid(column=0, row=1, padx=10, pady=10)

tipo = tk.StringVar()
combo_tipo = ttk.Combobox(ventana, textvariable=tipo, values=["Serie", "Paralelo"], state="readonly")
combo_tipo.grid(column=1, row=1, padx=10, pady=10)

# Botón para calcular resistencia equivalente
boton_calcular = ttk.Button(ventana, text="Calcular Resistencia Equivalente", command=calcular_Lg_resistencia_equivalente)
boton_calcular.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = ttk.Label(ventana, text="Resistencia Equivalente: ")
etiqueta_resultado.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Botón para limpiar el formulario
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar_formulario)
boton_limpiar.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Ejecutar la ventana de la aplicación
ventana.mainloop()
