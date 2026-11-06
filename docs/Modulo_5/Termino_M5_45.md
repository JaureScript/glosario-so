# NUMA (Non-Uniform Memory Access) / NUMA
**Definición formal:** 
Arquitectura de sistemas multiprocesador donde el tiempo y la latencia requeridos por un núcleo de CPU para acceder a la memoria física dependen de la proximidad topológica del banco de memoria a dicho procesador[cite: 3].

**Rol Operativo / Utilidad:** 
Desafía la *abstracción* tradicional de memoria homogénea. Obliga al *árbitro* (planificador) a aplicar estrictas políticas de afinidad de *control de hardware*, despachando hilos únicamente a los nodos locales para mantener un alto *rendimiento* y evitar la saturación del bus de interconexión[cite: 4].

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 5](../Índice%20Módulo%205.md)