# Problema del Año 2038 / Year 2038 Problem
**Definición formal:** 
Limitación arquitectónica en sistemas UNIX legados donde el contador de tiempo almacenado como un entero de 32 bits con signo se desbordará, provocando que los sistemas interpreten fechas futuras como el año 1901.

**Rol Operativo / Utilidad:** 
Representa el colapso de una *abstracción* matemática sobre el *control de hardware* (reloj RTC). Obliga al *árbitro* moderno a migrar a registros de 64 bits para garantizar la *seguridad* criptográfica (certificados) y el *rendimiento* en las tareas planificadas futuras.

**Cita Bibliográfica formal:** Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Capítulo 3-4.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)
