import polars as pl

# 1. Crear un DataFrame básico
datos = {
    "producto": ["A", "C", "Am", "Cf", "H"],
    "precio": [100.5, 200.0, 150.2, 300.8, 250.0],
    "ventas": [10, 5, 12, 3, 8]
}
df = pl.DataFrame(datos)

# 2. Transformación de datos usando evaluación perezosa (LazyFrame)
resultado = (
    df.lazy()
    .filter(pl.col("ventas") > 4)
    .group_by("producto")
    .agg([
        (pl.col("precio") * pl.col("ventas")).sum().alias("total_ingresos"),
        pl.col("ventas").mean().alias("promedio_ventas")
    ])
    .sort("total_ingresos", descending=True)
    .collect()  # Ejecuta la consulta optimizada
)

print(resultado)