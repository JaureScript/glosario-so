# Barrera de Escritura / Write Barrier
**Definición formal:** 
Directiva a nivel de sistema de archivos que prohíbe explícitamente al controlador del disco y a sus cachés reordenar operaciones de escritura de bloques físicos a través de dicho límite temporal.

**Rol Operativo / Utilidad:** 
Garantiza la *seguridad* transaccional forzando un *control de hardware* estricto y ordenado. El *árbitro* sacrifica una fracción mínima de *rendimiento* en E/S para sostener la *abstracción* de persistencia atómica ante fallas eléctricas repentinas.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)