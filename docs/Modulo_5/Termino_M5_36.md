# Caché de Página / Page Cache
**Definición formal:** 
Región de la memoria principal (RAM) transparente al usuario utilizada por el núcleo del sistema operativo para almacenar temporalmente bloques de datos recientemente leídos o escritos desde el almacenamiento secundario[cite: 3].

**Rol Operativo / Utilidad:** 
Mejora radicalmente el *rendimiento* general de E/S. El *árbitro* intercepta las solicitudes de *control de hardware* al disco físico, sirviendo la información desde esta *abstracción* volátil para minimizar los retrasos mecánicos, manteniendo la *seguridad* mediante sincronizaciones periódicas (flushing)[cite: 4].

**Cita Bibliográfica formal:** Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). *Operating Systems: Three Easy Pieces*. Arpaci-Dusseau Books. Capítulo 15-16.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 5](../Índice%20Módulo%205.md)