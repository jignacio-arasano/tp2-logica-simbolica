import math

# Solicitar el valor de t al usuario
t = float(input("Ingrese el valor de t (0 ≤ t ≤ 10): "))

# Calcular el valor de T(t)
T = 320 + 200 * math.sin(0.2 * math.pi * t)

# Calcular el valor de P(t)
P = 2.1 * ((320 + 200 * math.sin(0.2 * math.pi * t)) / (300 + 0.8 * t))

# Calcular el valor de X
if T < 450:
    X = "O"
else:
    X = "C"

# Calcular el valor de Y
if P < 3.2:
    Y = "B"
elif 3.2 < P < 3.5:
    Y = "M"
else:
    Y = "A"

# Imprimir los resultados numéricos y los valores de X e Y
print("El valor numérico de T(t) es:", T)
print("El valor numérico de P(t) es:", P)
print("El valor de X es:", X)
print("El valor de Y es:", Y)




