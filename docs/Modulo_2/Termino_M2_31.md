# Hilos de Usuario (ULT - User-Level Threads) / User-Level Threads
**Definición formal:** 
Hilos gestionados íntegramente mediante bibliotecas en el espacio de usuario, sin intervención directa del núcleo del sistema operativo.

**Rol Operativo / Utilidad:** 
Actúan como una capa de *abstracción* de concurrencia que ofrece alto *rendimiento* en la creación y conmutación de hilos al evitar los costosos cambios de modo hacia el núcleo, aunque comprometen el control si un hilo bloquea accidentalmente todo el proceso.

**Cita Bibliográfica formal:** Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson. Capítulo 2-3.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 2](../Índice%20Módulo%202.md)