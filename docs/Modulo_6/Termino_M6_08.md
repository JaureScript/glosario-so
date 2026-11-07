# PTE (Page Table Entry) / Page Table Entry
**Definición formal:** 
Registro individual dentro de una tabla de páginas que contiene la dirección física del marco correspondiente a una página virtual, junto con bits críticos de estado como presencia, lectura/escritura y privilegios[cite: 3].

**Rol Operativo / Utilidad:** 
Es el vector fundamental de *seguridad* y *abstracción* de memoria. A través del bit NX y descriptores de permisos, el *árbitro* dicta al *hardware* de la MMU qué accesos bloquear, optimizando el *rendimiento* de las validaciones en tiempo de ejecución[cite: 4].

**Cita Bibliográfica formal:** Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Capítulo 3-4.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)