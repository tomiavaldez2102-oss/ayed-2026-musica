#-*- coding: utf-8 -*-
from src.dominio.biblioteca import Biblioteca
from src.dominio.cancion import Cancion
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError
from src.dominio.biblioteca import Biblioteca
from src.dominio.cancion import Cancion
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion
from pathlib import Path
from src.persistencia.texto import cargar_texto, guardar_texto
from src.persistencia.binario import guardar_binario, cargar_binario, actualizar_registro, alta_binario, baja_binario
from src.excepciones import ArchivoInvalidoError
RAIZ = Path(__file__).resolve().parents[1]
DATA = RAIZ / 'data'
RUTA_TXT = DATA / 'canciones.txt'
RUTA_BIN = DATA / 'canciones.bin'
RUTA_VERSIONES = DATA / 'versiones.txt'
ENCABEZADOS = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]
def armar_catalogo_desde_txt(ruta):
    catalogo = ListaEnlazada()
    filas = cargar_texto(ruta)
    for f in filas:
        cancion = Cancion(
            id_cancion=int(f['id']),
            titulo =f['titulo'],
            artista=f['artista']
        )
        cancion.album = f.get('album', 'Desconocido')
        cancion.genero = f.get('genero', 'Varios')
        cancion.anio = int(f.get('anio', 2000))
        cancion.duracion_seg = int(f.get('duracion_seg',180))
        catalogo.insertar_al_final(cancion)
    return catalogo
def filas_del_catalogo(catalogo):
    filas = []
    for c in catalogo:
        filas.append({
            'id': c.id,
            'titulo': c.titulo,
            'artista': c.artista,
            'album': getattr(c, 'album','Desconocido'),
            'genero': getattr(c,'genero','Varios'),
            'anio': getattr(c, 'anio',2000),
            'duracion_seg' : getattr(c, 'duracion_seg',180)
        })
    return filas

def posicion_del_id(catalogo, id_buscado):
    for posicion, cancion in enumerate(catalogo):
        if cancion.id == id_buscado:
            return posicion
    return -1

def guardar_todo(catalogo):
    guardar_texto(RUTA_TXT, filas_del_catalogo(catalogo), ENCABEZADOS)
    guardar_binario(RUTA_BIN, catalogo)

def inicializar_biblioteca():
    biblio = Biblioteca()
    try:
        biblio.catalogo = armar_catalogo_desde_txt(RUTA_TXT)
        if not RUTA_BIN.exists():
            guardar_binario(RUTA_BIN, biblio.catalogo)
    except ArchivoInvalidoError as e:
        print(f'Aviso al iniciar: {e}')
    if RUTA_VERSIONES.exists():
        try:
            for fila in cargar_texto(RUTA_VERSIONES):
                biblio.cargar_version(
                    cancion_id=int(fila['cancion_id']),
                    version_de_id = int(fila['version_de_id']),
                    tipo = fila.get('tipo', 'version'),
                )
        except ArchivoInvalidoError:
            pass
    return biblio


class Playlist:
    def __init__(self, tope =3):
        self._canciones = ListaEnlazada()
        self._tope = tope
    def agregar(self, cancion):
        if self._canciones.tamanio() >= self._tope:
            raise ColeccionLlenaError(f'La playlist esta llena(maximo{self._tope}).')
        self._canciones.insertar_al_final(cancion)
    def listar(self):
        for c in self._canciones:
            print(f'-{c.titulo}({c.artista})')


def main():
    mi_biblio = inicializar_biblioteca()
    mi_playlist = Playlist(tope=3)
    historial = Pila()
    cola_reproduccion = Cola()
    ordenado_por = None

    while True:
        print('\n--- SPOTIFY UNaB ---') 
        print('1. Listar catalogo (Iterador)')
        print('2. Ver detalle de una cancion.')
        print('3. Buscar cancion (Lineal / Binaria)')
        print('4. Ordenar Catalogo (Seleccion/Insercion)')
        print('5. Buscar versiones derivadas (Recursion E2)')
        print('6. ABM Catalogo (Persistente) y Playlist (Tope)') 
        print('7. Historial de reproduccion (Pila LIFO)')
        print('8. Cola de reproduccion (Cola FIFO)')
        print('9. Guardar / cargar archivos (.txt y .bin)')
        print('0. Salir')
        opcion = input('Elije una opcion: ').strip()

        if opcion =='1':
            print('\n-- CATALOGO DE CANCIONES ---')
            for c in mi_biblio.catalogo:
                print(f'{c.id}. {c.titulo} - {c.artista}')
        elif opcion == '2':
            try:
                id_ver = int(input('Ingrese el ID de la cancion a inspeccionar: ').strip())
                encontrada = None
                for c in mi_biblio.catalogo:
                    if c.id == id_ver:
                        encontrada = c
                        break
                if encontrada:
                    print(f"\nID: {encontrada.id}")
                    print(f"Título: {encontrada.titulo}")
                    print(f"Artista: {encontrada.artista}")
                    print(f"Álbum: {getattr(encontrada, 'album', 'Desconocido')}")
                    print(f"Género: {getattr(encontrada, 'genero', 'Varios')}")
                    print(f"Año: {getattr(encontrada, 'anio', 2000)}")
                    print(f"Duración: {getattr(encontrada, 'duracion_seg', 180)} seg")
                else:
                    print('No existe ninguna cancion con ese ID.')
            except ValueError:
                print('Error: Ingrese un numero entero valido.')
        elif opcion == '3':
            print("\n--- BÚSQUEDA EN CATÁLOGO ---")
            print("1. Búsqueda Lineal")
            print("2. Búsqueda Binaria (requiere catalogo ordenado por titulo)")
            sub_op = input("Elige método de búsqueda: ").strip()
            clave_buscada = input('Ingrese el titulo exacto a buscar: ').strip()

            if sub_op == '1':
                resultado = busqueda_lineal(
                    mi_biblio.catalogo, clave_buscada, obtener_clave=lambda c: c.titulo
                )
                if resultado:
                    print(f'!Encontrado!: {resultado.id}. {resultado.titulo} - {resultado.artista}')
                else:
                    print('Cancion no encontrada (Lineal).')
            elif sub_op == '2':
                if ordenado_por != 'titulo':
                    print('Aviso: El catalogo no esta ordenado por titulo. Ordenelo primero en la Opcion 4.')
                else:
                    resultado = busqueda_binaria(
                        mi_biblio.catalogo, clave_buscada, obtener_clave=lambda c: c.titulo
                    )
                    if resultado:
                        print(f'!Encontrado!: {resultado.id}. {resultado.titulo} - {resultado.artista}')
                    else:
                        print('Cancion no encontrada (Binaria).')
            else:
                print('Subopcion invalida.')
                
        elif opcion == '4':
            print('\n --- ORDENAR CATALOGO ---')
            print('Criterio: 1) Por titulo 2) Por ID')
            crit_op = input('Elije criterio: ').strip()
            if crit_op == '2':
                obtener_clave_func = lambda c: c.id
                criterio_nombre = 'id'
            else:
                obtener_clave_func = lambda c: c.titulo
                criterio_nombre = 'titulo'

            print('Algoritmo: 1) Seleccion  2) Insercion')
            alg_op = input('Elige algoritmo: ').strip()
            if alg_op == '2':
                ordenar_insercion(mi_biblio.catalogo, obtener_clave_func)
            else:
                ordenar_seleccion(mi_biblio.catalogo, obtener_clave_func)

            ordenado_por = criterio_nombre
            guardar_todo(mi_biblio.catalogo)
            print(f'Catalogo ordenado por {criterio_nombre} y guardado en disco.')

           
        elif opcion == '5':
            try:
                id_buscar = int(input('Ingrese el ID de la cancion original: ').strip())
                derivadas = mi_biblio.versiones_de(id_buscar)
                if derivadas and not derivadas.esta_vacia():
                    ids_list = [str(d) for d in derivadas]
                    print(f"Versiones derivadas encontradas (IDs): {', '.join(ids_list)}")
                else:
                    print('Esta cancion no tiene versiones derivadas (Caso base).')
            except ValueError:
                print('Error: Ingrese un numero valido.')
                
        elif opcion == '6':
            print('\n--- ABM PERSISTENTE Y PLAYLIST ---')
            print('a) Alta de nueva cancion al catalogo(Persistente)')
            print('b) Modificar cancion existente por ID (Acceso directo O(1))')
            print('c) Baja de cancion del catalogo por ID (Persistente)')
            print('d) Agregar cancion a la Playlist (Tope 3)')
            sub_abm = input('Subopcion > ').strip().lower()

            if sub_abm == 'a':
                try:
                    nuevo_id = int(input('Nuevo ID: ').strip())
                    if posicion_del_id(mi_biblio.catalogo, nuevo_id) != -1:
                        print('Error: Ya existe una cancion con ese ID.')
                    else:
                        titulo = input('Titulo: ').strip()
                        artista = input('Artista: ').strip()
                        album = input('Album: ').strip() or 'Desconocido'
                        genero = input('Genero: ').strip() or 'Varios'
                        anio = int(input('Año: ').strip() or '2020')
                        duracion = int(input('Duracion (seg): ').strip() or '180')

                        nueva = Cancion(nuevo_id, titulo, artista)
                        nueva.album = album
                        nueva.genero = genero
                        nueva.anio = anio
                        nueva.duracion_seg = duracion

                        mi_biblio.catalogo.insertar_al_final(nueva)
                        ordenado_por = None
                        if not RUTA_BIN.exists():
                            guardar_binario(RUTA_BIN, mi_biblio.catalogo)
                        else:
                            alta_binario(RUTA_BIN, nueva)
                        guardar_texto(RUTA_TXT, filas_del_catalogo(mi_biblio.catalogo), ENCABEZADOS)
                        print('Cancion dada de alta en RAM, .bin y .txt.')
                except ValueError:
                    print('Error: ID, año y duracion deben ser numeros.')
            elif sub_abm == 'b':
                try:
                    id_mod = int(input('ID de la cancion a buscar a modificar: ').strip())
                    pos = posicion_del_id(mi_biblio.catalogo, id_mod)
                    if pos == -1:
                        print('No se encontro ninguna cancion con ese ID.')
                    else:
                        cancion_obj = None
                        for c in mi_biblio.catalogo:
                            if c.id == id_mod:
                                cancion_obj = c
                                break
                        print(f'Editanto: {cancion_obj.titulo} - {cancion_obj.artista}')
                        nuevo_titulo = input('Nuevo titulo (Enter para mantener): ').strip()
                        nuevo_artista = input('Nuevo artista (Enter para mantener): ').strip()
                        if nuevo_titulo:
                            cancion_obj.titulo = nuevo_titulo
                        if nuevo_artista:
                            cancion_obj.artista = nuevo_artista
                        ordenado_por = None
                        if RUTA_BIN.exists():
                            actualizar_registro(RUTA_BIN, pos, cancion_obj)
                        else:
                            guardar_binario(RUTA_BIN, mi_biblio.catalogo)
                        guardar_texto(RUTA_TXT, filas_del_catalogo(mi_biblio.catalogo), ENCABEZADOS)
                        print(f'Registro {pos} actualizado con accesp directo O(1) en .bin y .txt.')
                except ValueError:
                    print('Error: Ingrese un ID numerico valido.')
            elif sub_abm == 'c':
                try:
                    id_del = int(input('ID de la cancion a dar a baja: ').strip())
                    pos = posicion_del_id(mi_biblio.catalogo, id_del)
                    if pos == -1:
                        print('No se encontro ninguna cancion con ese ID.')
                    else:
                        nueva_lista = ListaEnlazada()
                        for c in mi_biblio.catalogo:
                            if c.id != id_del:
                                nueva_lista.insertar_al_final(c)
                        mi_biblio.catalogo = nueva_lista

                        if RUTA_BIN.exists():
                            baja_binario(RUTA_BIN, pos)
                        else:
                            guardar_binario(RUTA_BIN, mi_biblio.catalogo)
                        guardar_texto(RUTA_TXT, filas_del_catalogo(mi_biblio.catalogo), ENCABEZADOS)
                        print('Cancion eliminada y archivo binario compactado.')
                except ValueError:
                    print('Error: Ingrese un ID numerico valido.')
            elif sub_abm == 'd':
                try:
                    id_agregar = int(input('Ingrese un ID de la cancion para la Playlist: ').strip())
                    cancion_encontrada = None
                    for c in mi_biblio.catalogo:
                        if c.id == id_agregar:
                            cancion_encontrada = c
                            break
                    if cancion_encontrada:
                        mi_playlist.agregar(cancion_encontrada)
                        cola_reproduccion.encolar(cancion_encontrada)
                        print(f'Agregada a Playlist y Cola: {cancion_encontrada.titulo}')
                    else:
                        print('Cancion no encontrada.')
                except ValueError:
                    print('Error: Ingrese un ID numerico.')
                except ColeccionLlenaError as e:
                    print(f'ERROR: {e}')

        elif opcion == '7':
            try:
                cancion_borrada = historial.desapilar()
                print(f'Se quito "{cancion_borrada.titulo}" del historial (Pop Pila).')
            except PilaVaciaError as e:
                print(f'ERROR: {e}')        
        elif opcion == '8':
            try:
                cancion_sonando = cola_reproduccion.desencolar()
                print(f'Reproduciendo ahora: {cancion_sonando.titulo}')
                historial.apilar(cancion_sonando)
            except ColaVaciaError as e:
                print(f'ERROR: {e}')
        elif opcion == '9':
            print('\n --- PERSISTENCIA EN ARCHIVOS ---')
            print(' a) Cargar catalogo desde .txt')
            print(' b) Guardar catalogo en .txt')
            print(' c) Guardar el catalogo en binario (.bin)')
            print(' d) Cargar catalogo desde binario (.bin)')
            sub = input('  Subopcion > ').strip().lower()
            try:
                if sub == 'a':
                    mi_biblio.catalogo = armar_catalogo_desde_txt(RUTA_TXT)
                    ordenado_por = None
                    print(f'Catalogo cargado desde .txt: {mi_biblio.catalogo.tamanio()} canciones.')
                elif sub == 'b':
                    guardar_texto(RUTA_TXT,filas_del_catalogo(mi_biblio.catalogo), ENCABEZADOS)
                    print(f'Catalogo guardado en .txt.')
                elif sub == 'c':
                    guardar_binario(RUTA_BIN, mi_biblio.catalogo)
                    print(f'Catalogo guardado en .bin.')
                elif sub == 'd':
                    mi_biblio.catalogo = cargar_binario(RUTA_BIN)
                    ordenado_por = None
                    print(f'Catalogo cargado desde .bin: {mi_biblio.catalogo.tamanio()} items.')
                else:
                    print('Subopcion invalida')
            except ArchivoInvalidoError as error:
                print(f'Archivo invalido: {error}')
        elif opcion == '0':
            print('! Hasta luego!')
            break
        else:
            print('Opcion invalida: Elije un numero del 0 al 9.')



if __name__ == '__main__':
    main()















