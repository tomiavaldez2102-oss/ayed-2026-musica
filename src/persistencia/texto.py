from pathlib import Path
from src.excepciones import ArchivoInvalidoError

# Anclamos la ruta a la raíz del repositorio subiendo 3 niveles desde este archivo
# _file_ = src/persistencia/texto.py
# parents[0] = persistencia, parents[1] = src, parents[2] = Raíz del repo
RAIZ = Path(__file__).resolve().parents[2]
DATA = RAIZ / "data"

def cargar_texto(ruta):
    """Lee un .txt secuencial y devuelve una LISTA DE DICTS, uno por registro.
    La primera línea es el encabezado; cada línea siguiente es un registro
    con campos separados por coma. Si el archivo no existe o una línea
    tiene más/menos campos que el encabezado, lanza ArchivoInvalidoError."""
    ruta = Path(ruta)

    if not ruta.exists():
        raise ArchivoInvalidoError(f'No existe el archivo: {ruta}')
    filas = []
    with ruta.open('r', encoding='utf-8') as archivo:
        encabezado_linea = archivo.readline()
        if not encabezado_linea:
            raise ArchivoInvalidoError('El archivo esta completamente vacio')
        encabezado = encabezado_linea.strip().split(',')

        for numero_linea, linea in enumerate(archivo, start=2):
            linea = linea.strip()
            if not linea:
                continue
            valores = linea.split(',')
            if len(valores) != len(encabezado):
                raise ArchivoInvalidoError(f"Línea {numero_linea} inválida: se esperaban {len(encabezado)} campos pero se encontraron {len(valores)}.")
            fila_dict =  dict(zip(encabezado, valores))
            filas.append(fila_dict)
    return filas
def guardar_texto(ruta, filas,encabezados):
    ruta = Path(ruta)
    with ruta.open('w', encoding='utf-8', newline='') as archivo:
        archivo.write(','.join(encabezados) + '\n')
        for fila in filas:
            linea_campos = [str(fila[clave]) for clave in encabezados]
            archivo.write(','.join(linea_campos)+'\n')