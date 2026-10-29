from src.tads.lista_enlazada import ListaEnlazada

class Biblioteca:
    def __init__(self):
        self.catalogo = ListaEnlazada()
        self.relaciones = ListaEnlazada()

    def agregar_cancion(self, nueva_cancion):
        if nueva_cancion is None:
            return 'Error: no se recibio ninguna cancion'
        self.catalogo.insertar_al_final(nueva_cancion)
        return'Exito: Cancion guardada en la biblioteca'

    def cargar_version(self, cancion_id, version_de_id, tipo):
         relacion = {
              'id_derivada': cancion_id,
              'id_original': version_de_id,
              'tipo': tipo
    }
         self.relaciones.insertar_al_final(relacion)

    def versiones_directas(self, id_cancion):
        # Prepara una lista vacía para los hijos directos
        derivadas =ListaEnlazada()
        # Recorre todas las relaciones guardadas
        for rel in self.relaciones:
            # Si el ID original de la relación coincide con el que buscamos...
            if rel["id_original"] == id_cancion:
                # ...agrega el ID del cover a nuestra lista
                derivadas.insertar_al_final(rel["id_derivada"])
        return derivadas
    def versiones_de(self, id_cancion):
        directas = self.versiones_directas(id_cancion)
        if directas.esta_vacia():
            return ListaEnlazada()
        
        resultado = ListaEnlazada()

        for d in directas:
            resultado.insertar_al_final(d)

        for d in directas:
            sub_versiones = self.versiones_de(d)
            for sub in sub_versiones:
                resultado.insertar_al_final(sub)

        return resultado
     




