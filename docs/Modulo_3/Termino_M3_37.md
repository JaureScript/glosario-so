# Operación sem_wait / sem_wait Operation (Wait)
**Definición formal:** 
Operación atómica sobre un semáforo (también llamada operación P o wait) que decrementa el valor del semáforo; si el valor es menor que cero, suspende la ejecución del hilo invocador[cite: 3].

**Rol Operativo / Utilidad:** 
Garantiza la *seguridad* estricta en la exclusión mutua; obliga al *árbitro* del núcleo a suspender hilos para evitar condiciones de carrera sobre el *hardware* o los datos compartidos, penalizando levemente el *rendimiento* temporal a cambio de asegurar la integridad absoluta[cite: 4].

**Cita Bibliográfica formal:** Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). *Operating Systems: Three Easy Pieces*. Arpaci-Dusseau Books. Capítulo 15-16.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 3](../Índice%20Módulo%203.md)