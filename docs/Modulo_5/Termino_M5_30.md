# Zswap (Memoria Comprimida) / Zswap
**Definición formal:** Subsistema del núcleo Linux que intercepta páginas de memoria descartadas, las comprime dinámicamente y las almacena en un bloque reservado de RAM (zpool) antes de enviarlas al disco de intercambio físico[cite: 3].

**Rol Operativo / Utilidad:** Sustituye el lento *control de hardware* electromecánico (disco) por ciclos de CPU, logrando una *abstracción* que dispara el *rendimiento* en equipos con recursos limitados. El *árbitro* asegura la estabilidad y *seguridad* contra la inanición evitando la latencia catastrófica del swapping tradicional[cite: 4].

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 5](../Índice%20Módulo%205.md)