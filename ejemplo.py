from pathlib import Path

# Definimos la variable 'p' asignándole la ruta del directorio actual
p = Path.cwd()

def frase_binaria():
    frase = input('Ingrese una frase: ')
    with open(p/'frase.bin','wb') as f:
        f.write(frase.encode('utf-8'))

    with open(p/'frase.bin','rb') as g:
        contenido_bytes = g.read()

    bits_texto = ' '.join(f'{byte:08b}' for byte in contenido_bytes)

    print('Contenido en binario: ',bits_texto)
    print('Contenido leido(bytes): ', contenido_bytes)
    print('Frase decodificada: ', contenido_bytes.decode('utf-8'))

frase_binaria()