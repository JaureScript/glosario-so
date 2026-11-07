
# Zygote (Android OS) / Zygote
**Definición formal:** 
Proceso demonio fundamental en Android que se inicializa en el arranque del sistema y actúa como plantilla base precargando las bibliotecas del núcleo y la máquina virtual para acelerar el inicio de nuevas aplicaciones[cite: 3].

**Rol Operativo / Utilidad:** 
Actúa como el *árbitro* de inicialización que dispara el *rendimiento* móvil. Aplica el *control de hardware* mediante técnicas CoW (Copy-on-Write) para compartir la *abstracción* base en RAM entre todas las apps, manteniendo estrictas barreras de *seguridad* por sandboxing[cite: 4].

**Cita Bibliográfica formal:** Stallings, W. (2017). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson. Capítulo 5-6.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)