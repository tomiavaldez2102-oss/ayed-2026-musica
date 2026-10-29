from src.excepciones import ColaVaciaError
class Cola:
    def __init__(self):
        self._items = []
    def encolar(self, item):
        self._items.append(item)
    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError('La cola de reproduccion esta vacia.')
        return self._items.pop(0)
    def esta_vacia(self):
        return len(self._items)==0