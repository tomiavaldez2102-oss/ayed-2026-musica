from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError
class Pila:
    def __init__(self):
        self._items = ListaEnlazada()
    def apilar(self, items):
        self._items.insertar_al_inicio(items)
    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError('La pila de historial esta vacia')
        return self._items.eliminar_inicio()
    def esta_vacia(self):
        return self._items.esta_vacia()