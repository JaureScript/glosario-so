# PID Namespace / PID Namespace
**Definición formal:** 
Espacio de nombres de Linux que aísla el árbol de identificadores de procesos (PIDs), permitiendo que un contenedor tenga su propio proceso con PID 1 independiente del sistema anfitrión[cite: 3].

**Rol Operativo / Utilidad:** 
Es vital para la *seguridad* y *abstracción* en contenedores. Oculta la topología de procesos del *hardware* anfitrión, asegurando que un proceso comprometido no pueda enviar señales letales al *árbitro* principal del sistema base, aislando los fallos[cite: 4].

**Cita Bibliográfica formal:** Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson. Capítulo 2-3.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 3](../Índice%20Módulo%203.md)