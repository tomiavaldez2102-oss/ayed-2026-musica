from tads.lista_enlazada import ListaEnlazada

# Creamos la lista y agregamos elementos
mi_lista = ListaEnlazada()
mi_lista.insertar_inicio("De Musica Ligera")
mi_lista.insertar_final("Persiana Americana")

# Comprobamos que el iterador funciona
print("Las canciones en la lista son:")
for cancion in mi_lista:
    print("-", cancion)

