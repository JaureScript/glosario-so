# Init (Proceso 1 / Systemd) / Init Process
**Definición formal:** 
El primer proceso en espacio de usuario ejecutado por el núcleo durante el arranque, actuando como ancestro directo o indirecto de todos los procesos del sistema y responsable de gestionar el ciclo de vida del entorno.

**Rol Operativo / Utilidad:** 
Es el *árbitro* supremo y definitivo del espacio de usuario. Culmina la *abstracción* de la máquina extendida encendiendo los servicios con máxima *seguridad*, optimizando el *rendimiento* del arranque en paralelo y asumiendo el *control de hardware* residual (procesos huérfanos) hasta el apagado final.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)