from src.tads.lista_enlazada import ListaEnlazada

def ordenar_seleccion(coleccion, obtener_clave):
    elementos = list(coleccion)
    n = len(elementos)
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if obtener_clave(elementos[j]) < obtener_clave(elementos[pos_min]):
                pos_min = j
        elementos[i], elementos[pos_min] = elementos[pos_min], elementos[i]
    while not coleccion.esta_vacia():
         coleccion.eliminar(coleccion._cabeza.dato)
    for elem in elementos:
         coleccion.insertar_al_final(elem)
    return coleccion
def ordenar_insercion(coleccion, obtener_clave):
    elementos = list(coleccion)
    for i in range(1,len(elementos)):
        actual = elementos[i]
        j = i - 1
        while j >= 0 and obtener_clave(elementos[j]) > obtener_clave(actual):
                elementos[j+1] = elementos[j]
                j -=1
        elementos[j+1] = actual
        
    while not coleccion.esta_vacia():
         coleccion.eliminar(coleccion._cabeza.dato)
    for elem in elementos:
         coleccion.insertar_al_final(elem)
    return coleccion
