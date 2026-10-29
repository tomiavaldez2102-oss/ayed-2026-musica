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








