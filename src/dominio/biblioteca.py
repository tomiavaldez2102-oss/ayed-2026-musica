class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.relaciones = []

    def agregar_cancion(self, nueva_cancion):
        if nueva_cancion is None:
            return 'Error: no se recibio ninguna cancion'
        self.catalogo.append(nueva_cancion)
        return'Exito: Cancion guardada en la biblioteca'

    def cargar_version(self, cancion_id, version_de_id, tipo):
         relacion = {
              'id_derivada': cancion_id,
              'id_original': version_de_id,
              'tipo': tipo
    }
         self.relaciones.append(relacion)

    def versiones_directas(self, id_cancion):
        # Prepara una lista vacía para los hijos directos
        derivadas = []
        # Recorre todas las relaciones guardadas
        for rel in self.relaciones:
            # Si el ID original de la relación coincide con el que buscamos...
            if rel["id_original"] == id_cancion:
                # ...agrega el ID del cover a nuestra lista
                derivadas.append(rel["id_derivada"])
        return derivadas
    def versiones_de(self, id_cancion):
        directas = self.versiones_directas(id_cancion)
        if not directas:
            return []
        resultado = list(directas)

        for v in directas:
            resultado += self.versiones_de(v)
        return resultado
     




