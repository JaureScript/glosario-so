# Límites de RAM (memory.max) / RAM Limits (memory.max)
**Definición formal:** 
Parámetro de control de recursos en cgroups v2 que establece el consumo estricto máximo de memoria física permitido para un grupo de procesos.

**Rol Operativo / Utilidad:** 
Ejerce el *control de hardware* preventivo y actúa como *árbitro* estricto de *seguridad* y *rendimiento*, forzando la finalización (vía OOM Killer) de aplicaciones que excedan su cuota para evitar la degradación total del sistema.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 3](../Índice%20Módulo%203.md)