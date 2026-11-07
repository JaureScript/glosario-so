# Bandwidth Control (Control de Ancho de Banda de CPU) / CFS Bandwidth Control
**Definición formal:** 
Extensión del planificador Completely Fair Scheduler que permite establecer un límite máximo (techo) de tiempo de procesamiento que un grupo de procesos puede consumir durante un periodo determinado[cite: 3].

**Rol Operativo / Utilidad:** 
Ejerce un *control de hardware* restrictivo a nivel de CPU. El *árbitro* lo utiliza para garantizar la *seguridad* del sistema evitando el monopolio de ciclos de reloj, forzando pausas temporales (throttling) que estabilizan el *rendimiento* general de las cargas de trabajo concurrentes[cite: 4].

**Cita Bibliográfica formal:** Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). *Operating Systems: Three Easy Pieces*. Arpaci-Dusseau Books. Capítulo 15-16.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 5](../Índice%20Módulo%205.md)