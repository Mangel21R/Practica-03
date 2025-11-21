import csv

class Analizador:
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        self.datos = self.leer_csv()

    def leer_csv(self):
        datos = []
        with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter='|')
            for fila in lector:
                datos.append(fila)
        return datos

    def ventas_totales_por_provincia(self):
        totales = {}
        for fila in self.datos:
            provincia = fila["PROVINCIA"].lower().strip()
            total = float(fila["TOTAL_VENTAS"])
            totales[provincia] = totales.get(provincia, 0) + total
        return totales

    def ventas_por_provincia(self, nombre):
        nombre = nombre.lower().strip()
        totales = self.ventas_totales_por_provincia()
        if nombre not in totales:
            raise KeyError("Provincia no encontrada")
        return totales[nombre]