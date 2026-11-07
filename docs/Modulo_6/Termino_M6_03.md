# Variable de Condición (Condition Variable) / Condition Variable
**Definición formal:** 
Primitiva de sincronización que permite a los hilos suspender su ejecución y liberar el bloqueo de un mutex hasta que una condición específica compartida cambie de estado[cite: 3].

**Rol Operativo / Utilidad:** 
Optimiza el *rendimiento* concurrente evitando la espera activa. El *árbitro* retira el *control de hardware* (CPU) al hilo bloqueado, manteniéndolo en espera con total *seguridad* hasta que se notifique el cambio de estado en la *abstracción* de memoria compartida[cite: 4].

**Cita Bibliográfica formal:** Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Capítulo 3-4.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)
