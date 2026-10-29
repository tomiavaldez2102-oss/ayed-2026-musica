from src.excepciones import PilaVaciaError
class Pila:
    def __init__(self):
        self._items = []
    def apilar(self, items):
        self._items.append(items)
    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError('La pila de historial esta vacia')
        return self._items.pop()
    def esta_vacia(self):
        return len(self._items)==0