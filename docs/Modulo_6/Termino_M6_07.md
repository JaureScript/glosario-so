# Dirty Pages / Páginas Sucias
**Definición formal:** 
Páginas alojadas en la memoria caché (RAM) cuyos datos han sido modificados por un proceso pero que aún no han sido sincronizados o escritos de vuelta en el disco de almacenamiento secundario[cite: 3].

**Rol Operativo / Utilidad:** 
Incrementan temporalmente el *rendimiento* al evitar el lento *control de hardware* del almacenamiento electromecánico. Supone un riesgo de *seguridad* estructural, obligando al *árbitro* (demonio de sincronización) a limpiarlas asíncronamente para consolidar la *abstracción* de persistencia[cite: 4].

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)