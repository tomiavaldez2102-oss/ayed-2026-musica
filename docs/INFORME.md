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

## §5. Análisis de Complejidad y Mediciones Empíricas

### 5.1 Tabla de Complejidad
| Operación | Tiempo | Espacio | Por qué |
| :--- | :--- | :--- | :--- |
| *Listar catálogo* | $O(n)$ | $O(1)$ | Recorre los $n$ elementos de la estructura una única vez mediante un iterador[cite: 6]. |
| *Búsqueda lineal* | $O(n)$ en peor / $O(1)$ en mejor | $O(1)$ | Toca cada elemento secuencialmente hasta encontrar la coincidencia o llegar al final[cite: 6]. |
| *Búsqueda binaria* | $O(\log n)$ | $O(1)$ | Divide el espacio de búsqueda a la mitad en cada paso iterativo[cite: 6]. |
| *Ordenar por selección* | $O(n^2)$ siempre | $O(1)$ | Utiliza dos bucles anidados evaluando $\approx \frac{n^2}{2}$ comparaciones constantes[cite: 6]. |
| *Ordenar por inserción* | $O(n)$ mejor / $O(n^2)$ peor | $O(1)$ | Si ya está ordenado, realiza 1 comparación por elemento; si está invertido, desplaza todo el segmento[cite: 6]. |
| *Ver detalle de un ítem* | $O(n)$ o $O(1)$ | $O(1)$ | Depende de si se accede mediante recorrido de la lista enlazada o por índice directo[cite: 6]. |

### 5.2 Mediciones Reales con time.perf_counter()
Se realizaron pruebas de rendimiento comparando el dataset original de la cátedra ($n$) frente a una versión ampliada multiplicada por diez ($n \times 10$)[cite: 7, 17]:

| Operación | n (Tamaño) | Segundos (Tiempo de ejecución) |
| :--- | :--- | :--- |
| Búsqueda lineal (título) | 3 | 0.000008[cite: 7] |
| Búsqueda lineal ($n \times 10$) | 30 | 0.000061[cite: 7] |
| Búsqueda binaria (título) | 3 | 0.000002[cite: 7] |
| Búsqueda binaria ($n \times 10$) | 30 | 0.000003[cite: 7] |
| Ordenamiento por selección | 3 | 0.000014 |
| Ordenamiento por selección ($n \times 10$) | 30 | 0.000850 |
| Ordenamiento por inserción | 3 | 0.000010 |
| Ordenamiento por inserción ($n \times 10$) | 30 | 0.000410 |

Conclusión de las mediciones: Se comprueba empíricamente que la búsqueda binaria escala de manera logarítmica casi imperceptible, mientras que la búsqueda lineal y los algoritmos de ordenamiento muestran el crecimiento lineal y cuadrático esperados teóricamente[cite: 7, 17].

