#-*- coding: utf-8 -*-
from src.dominio.biblioteca import Biblioteca
from src.dominio.cancion import Cancion

#la funcion tiene un parametro biblio
#este parametro va a ser una caja 
#en la que guardare cosas
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

    while True:
        print('\n1. Listar catalogo')
        print('2. Buscar versiones derivadas (Recursion)')
        print('3. Salir')
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
            break
if __name__ == '__main__':
    main()




















