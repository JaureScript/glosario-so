# Mach IPC / Mach IPC
**Definición formal:** 
Mecanismo de comunicación entre procesos basado en el paso de mensajes altamente estructurado, fundamental en la arquitectura del micronúcleo Mach y heredado directamente por sistemas como macOS (XNU).

**Rol Operativo / Utilidad:** 
Es la *abstracción* central de sincronización del núcleo. Garantiza una *seguridad* extrema mediante puertos protegidos, delegando el *control de hardware* a servicios periféricos modulares, a costa de una ligera sobrecarga en el *rendimiento* debido al copiado y validación de mensajes.

**Cita Bibliográfica formal:** Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). *Operating Systems: Three Easy Pieces*. Arpaci-Dusseau Books. Capítulo 15-16.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)
