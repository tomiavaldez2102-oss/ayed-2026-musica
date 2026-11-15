from pathlib import Path
# Definimos la variable 'p' asignándole la ruta del directorio actual
p = Path.cwd()

def frase_txt():
    frase = input('Ingrese una frase: (o "FiNaL-de-ArChIvO" para terminar): ').strip()
    with open(p/'frase.txt','a', encoding='utf-8') as f:
        while frase != 'FiNaL-de-ArChIvO':
            f.write(frase + '\n')
            frase= input('Ingrese otra frase: ').strip()
    print('archivo guardado con exito')

frase_txt()