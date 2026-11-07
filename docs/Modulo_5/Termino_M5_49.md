# vDSO (Virtual Dynamically-linked Shared Object) / vDSO
**Definición formal:** 
Pequeña biblioteca compartida que el núcleo inyecta y mapea automáticamente en el espacio de direcciones de todos los procesos de usuario para acelerar la ejecución de llamadas al sistema altamente frecuentes (como obtener la hora)[cite: 3].

**Rol Operativo / Utilidad:** 
Es un atajo revolucionario para el *rendimiento*. *Abstrae* operaciones seguras directamente al espacio de usuario, evitando el gravísimo coste temporal (ciclos de *hardware*) de realizar un cambio de contexto formal hacia el *árbitro* central para funciones de solo lectura[cite: 4].

**Cita Bibliográfica formal:** Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson. Capítulo 2-3.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 5](../Índice%20Módulo%205.md)
