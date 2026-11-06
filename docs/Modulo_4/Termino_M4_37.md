# Semáforo Contador (sem_t) / Counting Semaphore
**Definición formal:** 
Primitiva de sincronización cuyo valor entero puede incrementarse o decrementarse para gestionar el acceso concurrente a un recurso limitado con múltiples instancias disponibles[cite: 3].

**Rol Operativo / Utilidad:** 
Es fundamental para la *abstracción* de recursos finitos (ej. un pool de conexiones o impresoras). El *árbitro* asegura el *rendimiento* ordenando los accesos y manteniendo la *seguridad* al bloquear hilos cuando el límite del *control de hardware* subyacente se alcanza[cite: 4].

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 4](../Índice%20Módulo%204.md)
