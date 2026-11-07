# Vector de Interrupciones / Interrupt Vector
**Definición formal:** 
Dirección de memoria estática contenida en una tabla estructurada (IVT/IDT) que apunta a la rutina específica del núcleo que debe manejar una interrupción de hardware o excepción de software particular.

**Rol Operativo / Utilidad:** 
Es el mapa de navegación del *control de hardware*. El *árbitro* usa esta *abstracción* para reaccionar en nanosegundos, salvaguardando el *rendimiento* de la CPU y la *seguridad* del sistema al atrapar fallas de ejecución antes de un colapso fatal.

**Cita Bibliográfica formal:** Stallings, W. (2017). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson. Capítulo 5-6.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)