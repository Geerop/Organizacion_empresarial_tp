import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("datos/ventas.csv")

# Calcular ventas totales
df["total"] = df["cantidad"] * df["precio"]

ventas_totales = df["total"].sum()

# Producto más vendido
producto_mas_vendido = (
    df.groupby("producto")["cantidad"]
    .sum()
    .idxmax()
)

# Ventas por producto
ventas_por_producto = (
    df.groupby("producto")["total"]
    .sum()
)

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Generar gráfico
ventas_por_producto.plot(kind="bar")

plt.title("Ventas por producto")
plt.ylabel("Monto")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")
