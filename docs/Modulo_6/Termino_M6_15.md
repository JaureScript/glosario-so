# Zero-Copy / Zero-Copy
**Definición formal:** 
Técnica de optimización de operaciones de entrada y salida en la que la CPU no realiza la tarea de copiar datos de una zona de memoria a otra, delegando la transferencia directa entre periféricos y búferes[cite: 3].

**Rol Operativo / Utilidad:** 
Maximiza el *rendimiento* del sistema reduciendo los cambios de contexto. El *árbitro* utiliza el *control de hardware* vía DMA para abstraer el flujo de datos, garantizando la *seguridad* de las transferencias a velocidades de red nativas sin saturar el procesador[cite: 4].

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)