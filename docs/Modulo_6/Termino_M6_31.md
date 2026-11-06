# Write-Ahead Logging (WAL) / Write-Ahead Logging
**Definición formal:** 
Técnica empleada en sistemas de archivos y bases de datos transaccionales donde todas las modificaciones se registran secuencialmente en un diario antes de aplicarse a las estructuras de datos principales.

**Rol Operativo / Utilidad:** 
Es el pilar de la *seguridad* estructural frente a fallos. El *árbitro* difiere el *control de hardware* de las escrituras dispersas, transformándolas en escrituras secuenciales que mejoran drásticamente el *rendimiento* y proveen la *abstracción* de recuperación atómica (rollback) tras un corte eléctrico.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)