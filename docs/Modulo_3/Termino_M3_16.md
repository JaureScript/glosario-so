# Memory Leak (Fuga de Memoria) / Memory Leak
**Definición formal:** 
Error de software en el cual un programa solicita bloques de memoria dinámica al sistema operativo pero omite liberarlos correctamente al dejar de utilizarlos, provocando un consumo progresivo e innecesario de memoria.

**Rol Operativo / Utilidad:** 
Constituye una amenaza directa al *rendimiento* del sistema, obligando al *árbitro* de memoria (el núcleo) a intervenir proactivamente. Requiere finalizar forzosamente el proceso anómalo para recuperar el *control de hardware* físico y evitar la inanición por agotamiento de RAM en todo el equipo.

**Cita Bibliográfica formal:** Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). *Operating Systems: Three Easy Pieces*. Arpaci-Dusseau Books. Capítulo 15-16.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 3](../Índice%20Módulo%203.md)