#-*- coding: utf-8 -*-
from config import TEMA
from dominio.cancion import listar_catalogo

def main():
    while True:
        print('\n1. Listar catalogo')
        print('\n2. Salir')
        opcion = input('Elige una opcion: ').strip()
        if opcion == '1':
            listar_catalogo()
        elif opcion == '2':
            break

if __name__ == '__main__':
    main()

























