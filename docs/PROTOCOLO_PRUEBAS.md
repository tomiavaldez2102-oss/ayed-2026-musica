- **ID** --> Acción / Qué probar --> Datos ingresados--> Resultado esperado
- *P01* Arrancar el programa y elegir "1. Listar catalogo" 1. Muestra la lista de canciones precargadas sin tirar error.
- **P02** Elegir "2. Buscar versiones" y buscar un ID que no existe 999 Muestra "Esta cancion no tiene versiones derivadas (Caso base)."
- **P03** Buscar una canción CON cadena de derivadas 12 Imprime la lista con los covers: [13, 99].
- **P04** Buscar una canción SIN derivadas (el final de la cadena) 99 Muestra "Esta cancion no tiene versiones derivadas (Caso base)."
- **P05** Ingresar texto en vez de un número al buscar ID hola El try/except lo ataja y muestra "Error: Ingresa un numero valido."
- **P06** En el menú principal, elegir una opción que no existe 8, No explota, simplemente vuelve a mostrar el menú principal.
- **P07** Presionar Enter sin escribir nada en el menú(vacío)El programa sigue corriendo y vuelve a preguntar la opción.
- **P08** Elegir la opción "3. Salir" 3 El bucle se rompe y el programa termina correctamente.

- | ID | Acción | Resultado esperado | Resultado |
- |----|--------|--------------------|-----------|
- | P05 | Agregar a la colección hasta el tope | el séptimo falla con excepción propia | pasa |
- | P06 | Desapilar historial vacío | excepción propia, menú sigue | pasa |
- | P07 | Desencolar cola vacía | excepción propia, menú sigue | pasa |
- | P08 | Listar colección con iterador | el orden coincide con las inserciones | pasa |

## Protocolo de Pruebas - Entrega 4

- | ID | Qué hacer en el CLI | Resultado esperado | Resultado |
- | :--- | :--- | :--- | :--- |
- | *P09* | Búsqueda lineal de un nombre que existe | Lo encuentra y lo muestra en pantalla[cite: 7]. | *Pasa*[cite: 7] |
- | *P10* | Búsqueda lineal de un nombre que no existe | Muestra "No encontrado", sin traceback, y el menú continúa[cite: 7]. | *Pasa*[cite: 7] |
- | *P11* | Búsqueda binaria con el catálogo desordenado | Avisa o reordena automáticamente; no da un falso "no encontrado"[cite: 7]. | *Pasa*[cite: 7] |
- | *P12* | Ordenar por un criterio y después por otro | El orden del catálogo cambia correctamente según el criterio seleccionado[cite: 7]. | *Pasa*[cite: 7] |

## Protocolo de Pruebas - Entrega 5

| P13 | E5 | Guardar catálogo en .txt (opción 9b), salir (0) y volver a entrar | Los cambios persisten al reiniciar el programa | Pasa |
| P14 | E5 | Guardar .bin (9c), modificar canción por ID (6b) y recargar .bin (9d) | actualizar_registro modifica en O(1) con seek y el cambio se refleja al recargar | Pasa |
| P15 | E5 | Cargar archivo binario inválido/basura en opción 9d | Lanza ArchivoInvalidoError con mensaje claro sin traceback y vuelve al menú | Pasa |



- **P01** E1 Arrancar y listar catálogo (dataset de la cátedra) - **pasa**
- **P02** E1 Ítem inexistente → mensaje claro, menú sigue - **pasa**
- **P03** E2 Recursión sobre un ítem con cadena  - **pasa**
- **P04** E2 Recursión sobre un ítem sin derivados (caso base) - **pasa**
- **P05** E3 Llenar la colección principal hasta el tope - **pasa**
- **P06** E3 Desapilar pila vacía → excepción propia - **pasa**
- **P07** E3 Desencolar cola vacía → excepción propia - **pasa**
- **P08** E3 Listar con el iterador, orden = inserciones - **pasa**
- **P09** E4 Búsqueda lineal de algo que existe - **pasa**
- **P10** E4 Búsqueda lineal de algo que no existe - **pasa**
- **P11** E4 Binaria con catálogo desordenado → avisa/reordena - **pasa**
- **P12** E4 Ordenar por un criterio y después por otro - **pasa**
- **P13** E5 Guardar .txt , salir, volver a entrar → sigue todo - **pasa**
- **P14** E5 Guardar binario, modificar por id, recargar → cambió - **pasa**
- **P15** E5 Archivo basura → ArchivoInvalidoError sin tracebacK - **pasa**