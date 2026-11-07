# TLB Miss (Fallo de TLB) / TLB Miss
**Definición formal:** 
Evento de hardware que ocurre cuando la traducción de una dirección virtual solicitada no se encuentra en la memoria caché TLB, requiriendo un recorrido completo por la tabla de páginas en RAM[cite: 3].

**Rol Operativo / Utilidad:** 
Provoca una degradación inmediata del *rendimiento* al requerir múltiples ciclos de *control de hardware* hacia la memoria principal, obligando al *árbitro* (mediante el núcleo o la MMU) a cargar la nueva traducción para mantener la *abstracción* y la *seguridad* del direccionamiento[cite: 4].

**Cita Bibliográfica formal:** Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson. Capítulo 2-3.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 5](../Índice%20Módulo%205.md)
