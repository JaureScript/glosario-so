# Hilos de Kernel (KLT - Kernel-Level Threads) / Kernel-Level Threads
**Definición formal:** 
Hilos gestionados y planificados directamente por el núcleo del sistema operativo a nivel de sistema.

**Rol Operativo / Utilidad:** 
Otorga al planificador un *control de hardware* absoluto sobre la ejecución. A diferencia de los hilos de usuario, si un KLT se bloquea por una operación de E/S, el *árbitro* puede despachar otro hilo del mismo proceso, manteniendo un alto *rendimiento*.

**Cita Bibliográfica formal:** Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson. Capítulo 2-3.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 2](../Índice%20Módulo%202.md)