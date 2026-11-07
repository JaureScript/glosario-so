# Caché Adaptativa de Reemplazo (ARC) / Adaptive Replacement Cache (ARC)
**Definición formal:** 
Algoritmo avanzado de reemplazo de páginas empleado en ZFS que equilibra dinámicamente las páginas "usadas recientemente" con las "usadas frecuentemente" para optimizar la retención de datos en memoria.

**Rol Operativo / Utilidad:** 
Supera las limitaciones de *abstracción* del algoritmo LRU tradicional. El *árbitro* predice con máxima precisión los patrones de E/S, disparando el *rendimiento* del *control de hardware* de lectura y blindando la *seguridad* operativa contra escaneos secuenciales masivos.

**Cita Bibliográfica formal:** Stallings, W. (2017). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson. Capítulo 5-6.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)