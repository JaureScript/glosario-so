# Inversión de Prioridades / Priority Inversion
**Definición formal:** 
Anomalía de planificación en la cual un proceso de alta prioridad se ve indirectamente bloqueado a la espera de un recurso retenido por un proceso de baja prioridad, el cual a su vez es desbancado por procesos de prioridad media.

**Rol Operativo / Utilidad:** 
Afecta negativamente el *rendimiento* determinista de los sistemas en tiempo real, obligando al planificador y al *árbitro* de sincronización del núcleo a implementar protocolos avanzados (como la herencia de prioridades) para asegurar la estabilidad operativa.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 2](../Índice%20Módulo%202.md)