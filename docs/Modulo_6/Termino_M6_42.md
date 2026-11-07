# Vnodo (Nodo Virtual) / Vnode
**Definición formal:** 
Estructura de datos abstracta utilizada por el VFS (Virtual File System) para representar un archivo o directorio genérico, independientemente del sistema de archivos físico subyacente.

**Rol Operativo / Utilidad:** 
Provee la máxima *abstracción* de almacenamiento. El *árbitro* intercepta estas estructuras y las redirige hacia el *control de hardware* específico del disco, unificando la *seguridad* (permisos globales) y el *rendimiento* sobre redes y discos de naturalezas dispares.

**Cita Bibliográfica formal:** Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Capítulo 3-4.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)