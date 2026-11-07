# mmap() y munmap() / mmap() and munmap()
**Definición formal:** 
Llamadas al sistema utilizadas para mapear archivos o dispositivos directamente dentro del espacio de direcciones virtuales de un proceso, o liberar dicho mapeo mediante munmap()[cite: 3].

**Rol Operativo / Utilidad:** 
Optimiza drásticamente el *rendimiento* de E/S[cite: 4]. *Abstrae* el acceso al almacenamiento físico al tratar los archivos como RAM, delegando el *control de hardware* directo a la MMU para acelerar las lecturas y escrituras de forma transparente.

**Cita Bibliográfica formal:** Stallings, W. (2017). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson. Capítulo 5-6.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 3](../Índice%20Módulo%203.md)