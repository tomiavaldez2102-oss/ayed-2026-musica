from src.excepciones import ColaVaciaError
from src.tads.lista_enlazada import ListaEnlazada
class Cola:
    def __init__(self):
        self._items = ListaEnlazada()
    def encolar(self, item):
        self._items.insertar_al_final(item)
    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError('La cola de reproduccion esta vacia.')
        frente = self._items._cabeza.dato
        self._items.eliminar(frente)
        return frente
    def esta_vacia(self):
        return self._items.esta_vacia()