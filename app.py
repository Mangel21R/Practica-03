from src.procesador import Analizador

def main():
    archivo = "datos/sri_ventas_2024.csv"
    analizador = Analizador(archivo)

    print("Ventas totales por provincia:")
    resumen = analizador.ventas_totales_por_provincia()
    for prov, total in resumen.items():
        print(f"\t{prov}: ${total:.2f}")

    print("\nVentas para una provincia")
    provincia = input("\tIngrese el nombre de una provincia: ")
    ventas = analizador.ventas_por_provincia(provincia)
    print(f"\tVentas de {provincia}: ${ventas:,.2f}")

    # ---- Estadística adicional (literal d) ----
    provincia_imp = analizador.provincia_mayor_importacion()
    print("\nEstadística adicional")
    print(f"\tProvincia con mayor volumen de importaciones: {provincia_imp}")

if __name__ == "__main__":
    main()