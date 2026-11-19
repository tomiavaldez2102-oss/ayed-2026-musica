# Informe Tecnico - Entrega 1
Grupo : Valdez Tomas - Carola Maidana
Tema : Musica
## 1. Justificacion del Tema
Hemos seleccionado el tema de **Biblioteca musical** por que permite modelar de forma natural entidades del mundo real(como canciones y artistas) utilizando la Programacion Orientada a Objetos, preparandose para integrar estructuras de datos avanzadas en las siguientes etapas.
## 2. Conceptos Teoricos: Mutabilidad en Python
- **Elementos mutables:** Sus valores pueden modificarse tras su creacion sin alterar su identidad en memoria(ej. listas, diccionarios).
- **Elementos Inmutables:** Su contenido no puede alterarse una vez inicializados; cualquier cambio crea un objeto nuevo(ej. cadenas de texto, numeros, tuplas)
## 2. Modelo (E1)

La entidad central del dominio es la clase *Cancion* (src/dominio/cancion.py), que representa cada pista musical del catálogo con 7 atributos tipados:

* *Identificador (id: int):* Inmutable una vez instanciado el objeto; actúa como clave única tanto en la búsqueda en memoria como para calcular su índice ordinal (0-based) en el archivo binario de registros fijos.
* *Atributos descriptivos y mutables (titulo: str, artista: str):* Pueden modificarse en tiempo de ejecución desde la operación ABM (6b), actualizándose en simultáneo en RAM, en el registro correspondiente de data/canciones.bin mediante acceso directo (seek) y en data/canciones.txt.
* *Metadatos adicionales (album: str, genero: str, anio: int, duracion_seg: int):* Completan la ficha técnica de cada canción y mantienen sus tipos y anchos fijos para la serialización binaria (<I 30s 25s 30s 12s 2H = 105 bytes).

*Relación entre las estructuras del sistema:*
* *Catálogo principal (ListaEnlazada):* Almacena la colección maestra de canciones cargadas desde disco (67 registros iniciales) y sirve como fuente única de verdad para listar, buscar, ordenar y persistir.
* *Playlist (ListaEnlazada con tope = 3):* Subcolección acotada que referencia canciones existentes del catálogo; al intentar superar los 3 elementos lanza ColeccionLlenaError.
* *Historial de reproducción (Pila LIFO):* Registra las canciones ya escuchadas para permitir volver a la última reproducida (desapilar()).
* *Cola de reproducción (Cola FIFO):* Administra las próximas canciones pendientes en orden estricto de llegada (encolar() / desencolar()).

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


## 4. TADs (E3)

| TAD | Operaciones implementadas | Invariante de representación | Dónde se usa en el sistema |
| :--- | :--- | :--- | :--- |
| *ListaEnlazada* (src/tads/lista_enlazada.py) | insertar_al_final(dato), eliminar(posicion), obtener(posicion), tamanio(), esta_vacia(), __iter__() | Los nodos están encadenados secuencialmente desde cabeza hasta None sin ciclos; el contador cantidad coincide siempre con la cantidad real de nodos enlazados; la playlist tiene además un tope máximo estricto (cantidad <= 3). | *Catálogo principal* de 67 canciones (carga desde .txt/.bin, listado con iterador, búsquedas, ordenamientos y ABM persistente) y *Playlist* con tope máximo de 3 canciones (opción 6d). |
| *Pila* (src/tads/pila.py) | apilar(dato), desapilar(), ver_tope(), esta_vacia(), tamanio() | Política LIFO (Last-In, First-Out): el acceso, inserción y extracción ocurren únicamente por el tope; nunca hay huecos intermedios y si esta_vacia() es verdadero, desapilar() y ver_tope() lanzan PilaVaciaError. | *Historial de reproducción* (opción 7): registra las últimas canciones reproducidas para permitir volver a la canción anterior en orden inverso. |
| *Cola* (src/tads/cola.py) | encolar(dato), desencolar(), ver_frente(), esta_vacia(), tamanio() | Política FIFO (First-In, First-Out): toda inserción se realiza por el final (fondo) y toda extracción por el principio (frente), preservando el orden estricto de llegada; si está vacía, desencolar() lanza ColaVaciaError. | *Cola de reproducción* (opción 8): gestiona las próximas canciones pendientes por reproducirse en orden de encolado. |



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

## 6. Persistencia (E5)

* **Texto simple (`.txt`):** Implementado en `src/persistencia/texto.py` mediante `cargar_texto` y `guardar_texto`. Lee secuencialmente el archivo CSV con encabezado (`id,titulo,artista,album,genero,anio,duracion_seg`), valida que cada fila tenga exactamente 7 campos y reconstruye los objetos `Cancion` en una `ListaEnlazada`.
* **Layout del registro binario:** `struct.Struct('<I 30s 25s 30s 12s 2H')` = **105 bytes** por registro:
  * `id` (`I`, 4 bytes)
  * `titulo` (`30s`, 30 bytes)
  * `artista` (`25s`, 25 bytes)
  * `album` (`30s`, 30 bytes)
  * `genero` (`12s`, 12 bytes)
  * `anio` (`H`, 2 bytes) y `duracion_seg` (`H`, 2 bytes)
  * Las cadenas se codifican en UTF-8 recortando al ancho máximo y rellenando con bytes nulos (`\x00`).
* **Header:** `struct.Struct('<4s 1s I')` = **9 bytes**: magia `b'AYED'` (4 B), tema `b'M'` (1 B) y cantidad total $N$ de registros (4 B).
* **Actualización por posición (`O(1)`):** `actualizar_registro` abre el archivo en modo `'r+b'`, calcula `HEADER.size + (posicion * FORMATO.size)` (`9 + posicion * 105`), salta con `seek` y sobrescribe únicamente ese registro sin reescribir el resto del archivo. El alta (`alta_binario`) realiza un *append* al final (`seek(0, 2)`) y actualiza el contador del header (`seek(0)`). La baja (`baja_binario`) compacta el archivo reescribiéndolo sin el registro eliminado.


## 7. Reparto de trabajo (E6)

| Integrante | Usuario GitHub | Tareas realizadas (E1–E6) | Archivos que defiende en el examen oral |
| *Tomás Agustín Valdez* * Maidana Carola *| tomiavaldez2102-oss | Modelado de dominio (Cancion) y excepciones propias (E1); recursión de versiones derivadas sobre versiones.txt (E2); TADs ListaEnlazada con iterador, Pila y Cola (E3); búsqueda lineal/binaria y ordenamientos por selección e inserción (E4); persistencia en .txt y .bin de longitud fija con struct y acceso directo $\mathcal{O}(1)$ con seek (E5); integración del CLI de 10 opciones y protocolo de regresión P01–P15 (E6). | src/main.py, src/persistencia/binario.py, src/persistencia/texto.py, src/tads/lista_enlazada.py, src/tads/pila.py, src/tads/cola.py |