# ZFS Intent Log (ZIL) / ZFS Intent Log
**Definición formal:** 
Área de registro especializada en el sistema de archivos ZFS, frecuentemente ubicada en unidades SSD ultrarrápidas (SLOG), destinada a registrar transacciones síncronas antes de consolidarlas en el grupo de almacenamiento principal.

**Rol Operativo / Utilidad:** 
*Abstrae* y oculta la latencia de las escrituras obligatorias. El *árbitro* redirige el *control de hardware* hacia este registro flash para acelerar el *rendimiento* de las bases de datos, manteniendo una *seguridad* estricta e infalible frente a corrupciones por cortes eléctricos.

**Cita Bibliográfica formal:** Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). *Operating Systems: Three Easy Pieces*. Arpaci-Dusseau Books. Capítulo 15-16.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)
