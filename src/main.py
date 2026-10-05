#-*- coding: utf-8 -*-
from src.dominio.biblioteca import Biblioteca
from src.dominio.cancion import Cancion
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError
from src.dominio.biblioteca import Biblioteca
from src.dominio.cancion import Cancion

#la funcion tiene un parametro biblio
#este parametro va a ser una caja 
#en la que guardare cosas

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

def cargar_datos_iniciales(biblio):
    biblio.agregar_cancion(Cancion(12, "De Musica Ligera (Original)", "Soda Stereo"))
    biblio.agregar_cancion(Cancion(13, "De Musica Ligera (Live)", "Soda Stereo"))
    biblio.agregar_cancion(Cancion(62, "De Musica Ligera (Remix)", "DJ Zeta"))
  # 2. Cargamos las relaciones basándonos en tu versiones.csv (13 es versión de 12)
    biblio.cargar_version(cancion_id=13, version_de_id=12, tipo="live")
    # Agregamos una relación inventada para probar que la recursión baje otro nivel
    biblio.cargar_version(cancion_id=99, version_de_id=13, tipo="remix")

def main():
    mi_biblio = Biblioteca()
    cargar_datos_iniciales(mi_biblio)

    mi_playlist = Playlist(tope=3)
    historial = Pila()
    cola_reproduccion = Cola()

    while True:
        print('\n--- SPOTIFY UNaB ---')
        print('1. Listar catalogo (Iterador)')
        print('2. Buscar versiones derivadas (Recursion E2)')
        print('3. Agregar cancion a Playlist (Tope)')
        print('4. Escuchar cancion (Cola y Pila)')
        print('5. Deshacer ultima escuchada (Pila)')
        print('6. Salir')
        opcion = input('Elije una opcion: ').strip()

        if opcion =='1':
            print('\n-- CATALOGO ---')
            for c in mi_biblio.catalogo:
                print(f'{c.id}. {c.titulo} -{c.artista}')
        elif opcion == '2':
            try:
                id_buscar = int(input('Ingrese el ID de la cancion original(ej.12): '))
                derivadas = mi_biblio.versiones_de(id_buscar)
                if derivadas:
                    print(f'Versiones encontradas: {derivadas}')
                else:
                    print('Esta cancion no tiene versiones derivadas(Caso base).')
            except ValueError:
                print('Error: Ingresa un numero valido.')
        elif opcion == '3':
            id_agregar = int(input('Ingrese ID de la cancion para la Playlist: '))

            cancion_encontrada = None
            for c in mi_biblio.catalogo:
                if c.id == id_agregar:
                    cancion_encontrada = c
                    break
            if cancion_encontrada:
                try:
                    mi_playlist.agregar(cancion_encontrada)
                    cola_reproduccion.encolar(cancion_encontrada)
                    print(f'Agregada:{cancion_encontrada.titulo}')
                except ColeccionLlenaError as e:
                    print(f'ERROR:{e}')
            else:
                print("Cancion no encontrada")
        elif opcion == '4':
            try:
                cancion_sonando = cola_reproduccion.desencolar()
                print(f'Reproduciendo ahora: {cancion_sonando.titulo}')
                historial.apilar(cancion_sonando)
            except ColaVaciaError as e:
                print(f'ERROR: {e}')
        elif opcion == '5':
            try:
                cancion_borrada = historial.desapilar()
                print(f"Se eliminó '{cancion_borrada.titulo}' del historial de reproduccion.")
            except PilaVaciaError as e:
                print(f'ERROR: {e}')
        elif opcion == '6':
            break

if __name__ == '__main__':
    main()















