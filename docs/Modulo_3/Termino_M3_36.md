# Operación sem_post / sem_post Operation (Signal)
**Definición formal:** 
Operación atómica sobre un semáforo (también llamada operación V o signal) que incrementa el valor del semáforo y desbloquea a un hilo en espera si procede[cite: 3].

**Rol Operativo / Utilidad:** 
Facilita la *abstracción* del acceso concurrente y actúa como herramienta del *árbitro*[cite: 4], notificando de forma atómica al planificador que un recurso de *hardware* o sección de memoria ha sido liberado, mejorando así el *rendimiento* de la multiprogramación.

**Cita Bibliográfica formal:** Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Capítulo 3-4.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 3](../Índice%20Módulo%203.md)
