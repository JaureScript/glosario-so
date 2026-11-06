# Caché de Escritura Diferida / Write-Back Cache
**Definición formal:** 
Política de almacenamiento en caché donde las modificaciones de datos se realizan inicialmente solo en la memoria rápida, actualizando el almacenamiento secundario físico en un momento posterior y asíncrono (flushing).

**Rol Operativo / Utilidad:** 
Multiplica el *rendimiento* de las operaciones de E/S. El *árbitro* *abstrae* la alta latencia del disco, pero asume un riesgo temporal de *seguridad* de datos, obligando al sistema a gestionar sincronizaciones periódicas del *control de hardware* para consolidar la información.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)