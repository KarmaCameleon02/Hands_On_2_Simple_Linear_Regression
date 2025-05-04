import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')
# DataSet del Caso Benetton de Sales & Advertising 
X = np.array([23, 26, 30, 34, 43, 48, 52, 57, 58])  # Advertising
Y = np.array([651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518])  # Sales

# Cantidad de registros
n = len(X)

# Cálculos 
sumX = np.sum(X)
sumY = np.sum(Y)
sumXY = np.sum(X * Y)
sumX2 = np.sum(X**2)

# Cálculo de B1 y B0
B1 = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX**2)
B0 = (sumY - B1 * sumX) / n

# Imprimir la ecuación de regresión
print(f"\nLa ecuación de regresión es: Sales = {B0:.2f} + {B1:.2f} * Advertising")

# Valores de Advertising para predicciones
valores_advertising = [25, 35, 45, 50, 60]

# Cálculo y muestra de predicciones
print("\nPredicciones de Sales aproximadas para valores de Advertising desconocidos:")
for x in valores_advertising:
    prediccion = B0 + B1 * x
    print(f"Advertising → {x}: Sales ≈ {prediccion:.2f}")