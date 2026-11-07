# Asignador por Zonas / Zone Allocator
**Definición formal:** 
Componente del gestor de memoria de Linux que divide la memoria física en zonas lógicas (ej. DMA, Normal, HighMem) para abordar las limitaciones de direccionamiento de diferentes arquitecturas y buses heredados.

**Rol Operativo / Utilidad:** 
Ejerce una *abstracción* organizativa sobre el mapa físico de RAM. El *árbitro* segmenta el *control de hardware* para garantizar la *seguridad* y *rendimiento* de periféricos antiguos (que requieren la zona DMA baja) sin afectar a los procesos modernos.

**Cita Bibliográfica formal:** Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Capítulo 3-4.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)
