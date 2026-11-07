# Futex (Fast Userspace Mutex) / Futex
**Definición formal:** 
Primitiva de sincronización del núcleo de Linux que proporciona un mecanismo ultrarrápido para bloqueos en el espacio de usuario, recurriendo a costosas llamadas al sistema (syscalls) únicamente cuando existe contención real por el recurso[cite: 3].

**Rol Operativo / Utilidad:** 
Optimiza radicalmente el *rendimiento* en aplicaciones multihilo. Abstrae la exclusión mutua permitiendo que el *hardware* resuelva la sincronización mediante operaciones atómicas en RAM, invocando al *árbitro* del núcleo solo como medida de *seguridad* cuando dos hilos colisionan[cite: 4].

**Cita Bibliográfica formal:** Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). *Operating Systems: Three Easy Pieces*. Arpaci-Dusseau Books. Capítulo 15-16.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 5](../Índice%20Módulo%205.md)
