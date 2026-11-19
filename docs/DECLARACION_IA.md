# Declaracion de Uso de Inteligencia Artificial
- **Herramienta utilizada:** Asistente de IA(Gemini)
-**Alcance del uso:** Se empleo de manera colaborativa para comprender la estructura modular del paquete en Python en Python, resolver errores de importacion y guiar la redaccion tecnica. Todo el codigo analizado y adaptado manualmente por el grupo.
# Declaración de uso de IA
Asistencia para comprender y estructurar la separación en módulos y la implementación de la recursión. Se utilizó como apoyo para comprender la organización del código, la separación entre módulos y el funcionamiento de la recursión aplicada a las versiones de canciones. Las sugerencias fueron adaptadas al proyecto de Biblioteca Musical y revisadas antes de incorporarlas.

| *E1* | 2026-09-15 | Gemini | Revisión del diseño inicial de la clase Cancion, menú CLI y jerarquía de excepciones propias. | Estructura base de clases de dominio y captura de excepciones en main.py. | Se adaptaron todos los atributos y validaciones al dataset canciones.txt y se probaron entradas inválidas en consola. | Tomás Agustín Valdez | Carola Maidana
| *E2* | 2026-09-29 | Gemini | Consulta sobre diseño de la función recursiva de versiones derivadas y armado de la traza de ejecución. | Idea de recorrido recursivo sobre diccionario de adyacencia cargado desde versiones.txt. | Se verificó la condición de corte (caso base) y se trazó manualmente con los IDs reales del catálogo (1 -> 62). | Tomás Agustín Valdez | Carola Maidana


- Entrega | Herramienta | Uso / Justificación |
- | E3 | Gemini | Asistencia para la estructuración de la ListaEnlazada desde cero con Nodos, implementación de Pila y Cola, manejo de excepciones (try/except) y corrección de sintaxis en la función recursiva. |
- | Fecha | Herramienta | Para qué se usó | Qué hicieron | Quién |
| :--- | :--- | :--- | :--- | :--- |
- | 01/11/2026 | Asistente IA (Gemini) | Tutoría de programación, diseño de algoritmos propios y estructuración de la  documentación. | Se implementó y validó la lógica de búsqueda lineal/binaria, ordenamiento por inserción, solución de dependencias de módulos y redacción de la sección de complejidad del informe. | Tomás Agustín Valdez | Carola Maidana |

| *E4* | 2026-10-27 | Gemini | Verificación de invariantes de ordenamiento por Selección e Inserción y precondición de búsqueda binaria. | Lógica de bandera ordenado_por para bloquear la búsqueda binaria si el catálogo no está ordenado por título. | Se realizaron las mediciones de tiempo con time.perf_counter y se comprobó la estabilidad y el ordenamiento por título e ID. | Tomás Agustín Valdez | Maidana Carola


| E5 | 2026-11-15 | Gemini | Diseño de layout struct para tema Música, cálculo de offset para seek y manejo de excepciones ArchivoInvalidoError | src/persistencia/texto.py, src/persistencia/binario.py e integración en src/main.py | Definí anchos de campo (105 bytes), implementé el ABM persistente y ejecuté las pruebas P13–P15 | Tomás Agustín Valdez | Carola Maidana

| *E6* | 2026-11-16 | Gemini | Revisión integral de documentación (INFORME.md, README.md, PROTOCOLO_PRUEBAS.md) y checklist de cierre. | Estructura de tablas de TADs, protocolo de regresión y guía de verificación de entrega. | Se ejecutaron manualmente los 15 casos de prueba (P01–P15) sobre el catálogo limpio de 67 canciones y se verificó el funcionamiento completo. | Tomás Agustín Valdez | Carola Maidana