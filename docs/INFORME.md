# Informe Tecnico - Entrega 1

## 1. Justificacion del Tema
Hemos seleccionado el tema de **Biblioteca musical** por que permite modelar de forma natural entidades del mundo real(como canciones y artistas) utilizando la Programacion Orientada a Objetos, preparandose para integrar estructuras de datos avanzadas en las siguientes etapas.
## 2. Conceptos Teoricos: Mutabilidad en Python
- **Elementos mutables:** Sus valores pueden modificarse tras su creacion sin alterar su identidad en memoria(ej. listas, diccionarios).
- **Elementos Inmutables:** Su contenido no puede alterarse una vez inicializados; cualquier cambio crea un objeto nuevo(ej. cadenas de texto, numeros, tuplas)

## Función: versiones_de(id_cancion)
- **Caso base:** Si la canción no tiene versiones directas, devolver lista vacía [].
- **Caso recursivo:** Devuelve las versiones directas + versiones_de(hijos).
- **Traza para la Canción Original (ID 12):**

- **Llamada 1:** versiones_de(12) -> Encuentra versión directa (13).

Devuelve: [13] + versiones_de(13)

- **Llamada 2:** versiones_de(13) -> Encuentra versión directa (99).

Devuelve: [99] + versiones_de(99)

- **Llamada 3:** versiones_de(99) -> NO tiene versiones directas (Caso base).

Devuelve: []
- **Resultado Final:** [13] + [99] + [] = [13, 99]



