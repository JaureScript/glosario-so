# Núcleo Monolítico / Monolithic Kernel
**Definición formal:** 
Arquitectura de sistema operativo en la cual la totalidad de los servicios esenciales del núcleo (gestión de memoria, controladores, sistema de archivos) se ejecutan juntos en un único espacio de direcciones privilegiado (Ring 0)[cite: 3].

**Rol Operativo / Utilidad:** 
Maximiza el *rendimiento* de las llamadas al sistema y el *control de hardware*[cite: 4] eliminando los cambios de contexto internos, aunque compromete parcialmente la *seguridad* arquitectónica ya que un fallo fatal en cualquier controlador (driver) puede provocar un colapso total (Kernel Panic).

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 3](../Índice%20Módulo%203.md)
