# Reclamación de Zonas / Zone Reclamation
**Definición formal:** 
Mecanismo del gestor de memoria, crítico en arquitecturas NUMA, que fuerza la recuperación de páginas limpias (caché de disco) dentro de un nodo local antes de solicitar asignación de RAM a nodos remotos.

**Rol Operativo / Utilidad:** 
Maximiza el *rendimiento* del procesador respetando la topología física del *control de hardware*. El *árbitro* destruye temporalmente la *abstracción* de la caché para mantener la *seguridad* temporal y la latencia baja en la ejecución de hilos hiper-locales.

**Cita Bibliográfica formal:** Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). *Operating Systems: Three Easy Pieces*. Arpaci-Dusseau Books. Capítulo 15-16.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)
