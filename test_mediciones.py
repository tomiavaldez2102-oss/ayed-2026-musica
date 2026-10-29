import time
from src.dominio.biblioteca import Biblioteca
from src.dominio.cancion import Cancion
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion

def ejecutar_mediciones():
    biblio = Biblioteca()
    biblio.agregar_cancion(Cancion(12, "De Musica Ligera (Original)", "Soda Stereo"))
    biblio.agregar_cancion(Cancion(13, "De Musica Ligera (Live)", "Soda Stereo"))
    biblio.agregar_cancion(Cancion(62, "De Musica Ligera (Remix)", "DJ Zeta"))

    datos = list(biblio.catalogo)
    n = len(datos)
    if n ==0:
        print('El catalogo esta vacio. Agrega canciones para medir.')
        return 
    clave_busqueda = datos[0].titulo
    print(f"=== MEDICIONES CON N = {n} ===")
    inicio = time.perf_counter()
    _ = busqueda_lineal(datos, clave_busqueda, obtener_clave=lambda c: c.titulo)
    fin = time.perf_counter()
    tiempo_lineal_n = fin - inicio
    print(f"Búsqueda lineal (n={n}): {tiempo_lineal_n:.7f} s")

    #BUSQUEDA BINARIA(Data set original- Requiere orden previo)
    datos_ordenados = list(datos)
    ordenar_insercion(datos_ordenados, obtener_clave=lambda c: c.titulo)

    inicio = time.perf_counter()
    _ = busqueda_binaria(datos_ordenados, clave_busqueda, obtener_clave=lambda c: c.titulo)
    fin = time.perf_counter()
    tiempo_binaria_n = fin - inicio
    print(f'Busqueda binaria (n={n}): {tiempo_binaria_n:.7f} s')
    print("\n" + "="*40 + "\n")
    #2.AGRANDO EL DATA SET(n x 10)
    datos_grandes = datos * 10
    n_grande = len(datos_grandes)
    print(f"=== MEDICIONES CON N x 10 = {n_grande} ===")
    #BUSQUEDA LINEAL(Dataset agrandado)
    inicio = time.perf_counter()
    _ = busqueda_lineal(datos_grandes, clave_busqueda, obtener_clave=lambda c: c.titulo)
    fin = time.perf_counter()
    tiempo_lineal_10n = fin - inicio
    print(f"Búsqueda lineal (n x 10 = {n_grande}): {tiempo_lineal_10n:.7f} s")

    datos_grandes_ordenados = list(datos_grandes)
    ordenar_insercion(datos_grandes_ordenados, obtener_clave=lambda c: c.titulo)

    inicio = time.perf_counter()
    _ = busqueda_binaria(datos_grandes_ordenados, clave_busqueda, obtener_clave=lambda c: c.titulo)
    fin = time.perf_counter()
    tiempo_binaria_10n = fin - inicio
    print(f"Búsqueda binaria (n x 10 = {n_grande}): {tiempo_binaria_10n:.7f} s")

    # --- ORDENAMIENTO POR SELECCIÓN (Dataset Agrandado) ---
    datos_sel = list(datos_grandes)
    inicio = time.perf_counter()
    ordenar_seleccion(datos_sel, obtener_clave=lambda c: c.titulo)
    fin = time.perf_counter()
    print(f"Ordenamiento Selección (n x 10 = {n_grande}): {fin - inicio:.7f} s")

    # --- ORDENAMIENTO POR INSERCIÓN (Dataset Agrandado) ---
    datos_ins = list(datos_grandes)
    inicio = time.perf_counter()
    ordenar_insercion(datos_ins, obtener_clave=lambda c: c.titulo)
    fin = time.perf_counter()
    print(f"Ordenamiento Inserción (n x 10 = {n_grande}): {fin - inicio / 10:.7f} s")

if __name__ == "__main__":
    ejecutar_mediciones()