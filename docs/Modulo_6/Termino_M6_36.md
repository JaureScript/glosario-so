# Ceder CPU (Llamada sched_yield) / Yield
**Definición formal:** 
Llamada al sistema mediante la cual un proceso o hilo en ejecución renuncia voluntariamente a su fracción de tiempo de procesador (quántum) restante, cediendo su turno y reincorporándose a la cola de listos.

**Rol Operativo / Utilidad:** 
Facilita la *abstracción* cooperativa en la multitarea. Permite al *árbitro* redistribuir el *control de hardware* hacia hilos más críticos, optimizando el *rendimiento* al evitar bucles de espera activa (spinlocks) que desperdician ciclos sin aportar *seguridad* lógica.

**Cita Bibliográfica formal:** Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). *Operating Systems: Three Easy Pieces*. Arpaci-Dusseau Books. Capítulo 15-16.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)