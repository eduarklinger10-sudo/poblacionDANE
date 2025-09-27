
import matplotlib.pyplot as plt

# Datos de población (en miles de habitantes)
datos = [
    {"año": 2018, "bogota": 7830, "antioquia": 6420, "valle": 4840},
    {"año": 2019, "bogota": 7900, "antioquia": 6480, "valle": 4900},
    {"año": 2020, "bogota": 7970, "antioquia": 6535, "valle": 4955},
    {"año": 2021, "bogota": 8050, "antioquia": 6590, "valle": 5020},
    {"año": 2022, "bogota": 8120, "antioquia": 6645, "valle": 5090},
]

# Función para calcular cuánto crece cada región por año
def tasa_crecimiento(region):
    inicial = datos[0][region]   # primer año
    final = datos[-1][region]    # último año
    años = datos[-1]["año"] - datos[0]["año"]  # cuántos años pasaron
    tasa = (final / inicial) ** (1 / años) - 1
    return tasa

# Función para proyectar la población en los próximos 5 años
def proyeccion(region):
    tasa = tasa_crecimiento(region)
    actual = datos[-1][region]   # último valor conocido
    año_base = datos[-1]["año"]  # último año
    resultado = []
    for i in range(1, 6):  # 5 años hacia adelante
        año = año_base + i
        poblacion = actual * ((1 + tasa) ** i)
        resultado.append({"año": año, region: int(poblacion)})
    return resultado

# Guardar las proyecciones
proy_bogota = proyeccion("bogota")
proy_antioquia = proyeccion("antioquia")
proy_valle = proyeccion("valle")

# Preparar datos históricos
años = [d["año"] for d in datos]
bogota_hist = [d["bogota"] for d in datos]
antioquia_hist = [d["antioquia"] for d in datos]
valle_hist = [d["valle"] for d in datos]

# Agregar proyecciones
años_ext = años + [p["año"] for p in proy_bogota]
bogota_ext = bogota_hist + [p["bogota"] for p in proy_bogota]
antioquia_ext = antioquia_hist + [p["antioquia"] for p in proy_antioquia]
valle_ext = valle_hist + [p["valle"] for p in proy_valle]

# Dibujar las gráficas
plt.plot(años, bogota_hist, "o-", label="Bogotá histórico")
plt.plot(años, antioquia_hist, "o-", label="Antioquia histórico")
plt.plot(años, valle_hist, "o-", label="Valle histórico")

plt.plot(años_ext[-5:], bogota_ext[-5:], "s--", label="Bogotá proyección")
plt.plot(años_ext[-5:], antioquia_ext[-5:], "s--", label="Antioquia proyección")
plt.plot(años_ext[-5:], valle_ext[-5:], "s--", label="Valle proyección")

plt.xlabel("Año")
plt.ylabel("Población (miles)")
plt.title("Proyección de población (2018-2027)")
plt.legend()
plt.grid(True)
plt.show()

# Mostrar resultados en pantalla
print("\n--- Tasas de Crecimiento y Proyecciones ---")
for region in ["bogota", "antioquia", "valle"]:
    tasa = tasa_crecimiento(region) * 100
    print(f"\n{region.capitalize()}:")
    print(f"Tasa de crecimiento anual: {tasa:.2f}%")
    for p in proyeccion(region):
        print(f"Año {p['año']}: {p[region]} mil habitantes")




# --- Graficar la población por región ---
años = [d["año"] for d in datos]
bogota = [d["bogota"] for d in datos]
antioquia = [d["antioquia"] for d in datos]
valle = [d["valle"] for d in datos]

plt.plot(años, bogota, marker="o", label="Bogotá")
plt.plot(años, antioquia, marker="o", label="Antioquia")
plt.plot(años, valle, marker="o", label="Valle")

plt.title("Crecimiento poblacional 2018 - 2022")
plt.xlabel("Año")
plt.ylabel("Población (miles de habitantes)")
plt.legend()
plt.grid(True)
plt.show()