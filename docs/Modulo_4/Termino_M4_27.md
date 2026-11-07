# Rutina de Fallo de Página / Page Fault Handler
**Definición formal:** 
Código del núcleo del sistema operativo que maneja la interrupción provocada por un fallo de página, localizando el bloque en almacenamiento secundario y cargándolo en la memoria física[cite: 3].

**Rol Operativo / Utilidad:** 
Mantiene la ilusión de la *abstracción* de memoria virtual continua. El núcleo, como *árbitro*, detiene el proceso, ejerce *control de hardware* sobre el disco de intercambio y actualiza las tablas con un impacto temporal en el *rendimiento* que preserva la *seguridad* de ejecución[cite: 4].

**Cita Bibliográfica formal:** Stallings, W. (2017). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson. Capítulo 5-6.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 4](../Índice%20Módulo%204.md)
