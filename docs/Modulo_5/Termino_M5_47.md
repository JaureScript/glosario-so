# RCU / Read-Copy-Update
**Definición formal:** 
Mecanismo avanzado de sincronización del núcleo altamente escalable que permite a múltiples hilos lectores acceder concurrentemente a estructuras de datos compartidas sin usar bloqueos, difiriendo las actualizaciones y liberaciones de memoria[cite: 3].

**Rol Operativo / Utilidad:** 
Lleva el *rendimiento* de lectura en sistemas multiprocesador a su límite teórico. Sustituye la restrictiva *seguridad* de los semáforos por una *abstracción* donde el *árbitro* garantiza la coherencia del *hardware* clonando los datos, eliminando por completo los cuellos de botella por contención[cite: 4].

**Cita Bibliográfica formal:** Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson. Capítulo 2-3.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 5](../Índice%20Módulo%205.md)