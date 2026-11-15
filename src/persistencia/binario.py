import struct
from pathlib import Path
from src.excepciones import ArchivoInvalidoError
from src.tads.lista_enlazada import ListaEnlazada
from src.dominio.cancion import Cancion

FORMATO = struct.Struct('<I 30s 25s 30s 12s 2H')
HEADER = struct.Struct('<4s 1s I')
TEMA = b'M'
def _a_bytes(texto, ancho):
    if texto is None:
        texto =''
    texto_bytes = texto.encode('utf-8')[:ancho]
    return texto_bytes.ljust(ancho, b'\x00')
def _a_texto(datos_bytes):
    return datos_bytes.rstrip(b'\x00').decode('utf-8')
def _item_a_tupla(cancion):
    return (
        cancion.id,
        _a_bytes(cancion.titulo,30),
        _a_bytes(cancion.artista,25),
        _a_bytes(getattr(cancion,'album',''),30),
        _a_bytes(getattr(cancion,'genero',''),12),
        getattr(cancion,'anio',2000),
        getattr(cancion,'duracion_seg',180)
    )
def _tupla_a_item(tupla):
    c = Cancion(id_cancion=tupla[0], titulo=_a_texto(tupla[1]), artista=_a_texto(tupla[2]))
    c.album = _a_texto(tupla[3])
    c.genero = _a_texto(tupla[4])
    c.anio = tupla[5]
    c.duracion_seg = tupla[6]
    return c
def guardar_binario(ruta, catalogo):
    with open(ruta,'wb') as archivo:
        archivo.write(HEADER.pack(b'AYED', TEMA, catalogo.tamanio()))
        for cancion in catalogo:
            archivo.write(FORMATO.pack(*_item_a_tupla(cancion)))
def cargar_binario(ruta):
    ruta = Path(ruta)
    if not ruta.exists():
        raise ArchivoInvalidoError(f'No existe el archivo binario:{ruta}')
    with open(ruta,'rb') as archivo:
        cabecera = archivo.read(HEADER.size)
        if len(cabecera) < HEADER.size:
            raise ArchivoInvalidoError('Archivo binario invalido: Cabecera incompleta o truncada')
        magia, tema, cantidad = HEADER.unpack(cabecera)
        if magia != b'AYED':
            raise ArchivoInvalidoError(f'Magia incorrecta: {magia}. Se esperaba "AYED".')
        if tema != TEMA:
            raise ArchivoInvalidoError(f'Tema no coincidente: Se esperaba "M" (Musica), vino"{tema.decode()}".')

        catalogo = ListaEnlazada()
        for i in range(cantidad):
            datos = archivo.read(FORMATO.size)
            if len(datos) < FORMATO.size:
                raise ArchivoInvalidoError(f'Binario truncado: el header dice {cantidad} registros pero corto en el {i}')
            catalogo.insertar_al_final(_tupla_a_item(FORMATO.unpack(datos)))
        return catalogo
def actualizar_registro(ruta, posicion, cancion):
    with open(ruta, 'r+b') as archivo:
        #hace el calculo matematico del byte exacto de inicio
        byte_objetivo = HEADER.size + (posicion*FORMATO.size)
        archivo.seek(byte_objetivo)
        archivo.write(FORMATO.pack(*_item_a_tupla(cancion)))
def alta_binario(ruta, cancion):
    with open(ruta, 'r+b') as archivo:
        cabecera = archivo.read(HEADER.size)
        magia, tema, cantidad = HEADER.unpack(cabecera)
        archivo.seek(0,2)
        archivo.write(FORMATO.pack(*_item_a_tupla(cancion)))
        archivo.seek(0)
        archivo.write(HEADER.pack(magia, tema, cantidad+1))
def baja_binario(ruta, posicion):
    with open(ruta,'r+b') as archivo:
        cabecera = archivo.read(HEADER.size)
        magia, tema, cantidad = HEADER.unpack(cabecera)

        registros = [archivo.read(FORMATO.size) for _ in range(cantidad)]

        del registros[posicion]
        archivo.seek(0)
        archivo.truncate()
        archivo.write(HEADER.pack(magia, tema, len(registros)))
        for reg in registros:
            archivo.write(reg)