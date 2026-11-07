# Transición a Estado Zombie / Zombie State Transition
**Definición formal:** 
Fase final e inevitable en el ciclo de vida de un proceso UNIX, durante la cual el proceso libera todos sus recursos activos, conservando únicamente su estructura de control (PCB) hasta que su padre recoja el código de salida.

**Rol Operativo / Utilidad:** 
Representa la *abstracción* de terminación delegada. Permite al *árbitro* revocar instantáneamente el *control de hardware* (memoria y CPU) para liberar *rendimiento*, reteniendo únicamente la *seguridad* del código de estado para mantener la jerarquía estructural intacta.

**Cita Bibliográfica formal:** Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Capítulo 3-4.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)
