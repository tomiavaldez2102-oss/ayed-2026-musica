class PilaVaciaError(Exception):
    """Excepción lanzada cuando se intenta desapilar de una pila vacía."""
    pass

class ColaVaciaError(Exception):
    """Excepción lanzada cuando se intenta desencolar de una cola vacía."""
    pass

class ColeccionLlenaError(Exception):
    """Excepción lanzada cuando se intenta agregar elementos a una colección que alcanzó su tope."""
    pass