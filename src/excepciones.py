class PilaVaciaError(Exception):
    """Excepción lanzada cuando se intenta desapilar de una pila vacía."""
    pass

class ColaVaciaError(Exception):
    """Excepción lanzada cuando se intenta desencolar de una cola vacía."""
    pass

class ColeccionLlenaError(Exception):
    """Excepción lanzada cuando se intenta agregar elementos a una colección que alcanzó su tope."""
    pass

class ArchivoInvalidoError(Exception):
    """Excepción lanzada cuando un archivo .txt o .bin está corrupto,
    truncado o no coincide con la firma / formato esperado por el programa."""
    pass