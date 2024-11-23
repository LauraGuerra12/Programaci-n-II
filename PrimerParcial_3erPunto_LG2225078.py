#Valor de las resistencias
L_colors_resist = {
    "negro": 0,
    "marron": 1,
    "rojo": 2,
    "naranja": 3,
    "amarillo": 4,
    "verde": 5,
    "azul": 6,
    "violeta": 7,
    "gris": 8,
    "blanco": 9
}


def lv_calcular_resist(g_color_1, g_color_2, g_color_3):
    
    v_val_1 = L_colors_resist[g_color_1.lower()]
    v_val_2 = L_colors_resist[g_color_2.lower()]
    va_multipli = 10 ** L_colors_resist[g_color_3.lower()]
    

    va_valor_resist = (v_val_1 * 10 + v_val_2) * va_multipli
    return va_valor_resist


g_color_1 = input("Ingrese el primer color: ")
g_color_2 = input("Ingrese el segundo color: ")
g_color_3 = input("Ingrese el tercer color (multiplicador): ")

Lau_resistencia = lv_calcular_resist(g_color_1, g_color_2, g_color_3)
print(f"El valor de la resistencia es: {Lau_resistencia} ohmios")
