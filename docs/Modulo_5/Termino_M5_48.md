# Slab Allocator (Asignador Slab) / Slab Allocator
**Definición formal:** 
Mecanismo de gestión de memoria interna del núcleo diseñado para preasignar, almacenar y reutilizar cachés de objetos de tamaño fijo (como inodos o PCBs), eliminando las ineficiencias de inicialización constante[cite: 3].

**Rol Operativo / Utilidad:** 
Optimiza el *rendimiento* interno y el *control de hardware* del propio sistema operativo. El *árbitro* utiliza esta *abstracción* para erradicar la fragmentación interna, manteniendo la *seguridad* operativa al evitar agotar la RAM durante ráfagas masivas de creación de procesos[cite: 4].

**Cita Bibliográfica formal:** Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson. Capítulo 2-3.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 5](../Índice%20Módulo%205.md)