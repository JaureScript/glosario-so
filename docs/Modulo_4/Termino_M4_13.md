# Proceso Zombie / Zombie Process
**Definición formal:** 
Proceso que ha finalizado su ejecución pero cuyos datos de entrada en la tabla de procesos (PCB) aún no han sido leídos ni recolectados por su proceso padre mediante una llamada como wait()[cite: 3].

**Rol Operativo / Utilidad:** 
Representa un riesgo operativo para la *seguridad* y el *rendimiento* si se acumulan. Obliga al *árbitro* del núcleo a retener entradas en la tabla, impidiendo la reasignación plena del *hardware* (identificadores PID) hasta que se procese el estado de salida[cite: 4].

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 4](../Índice%20Módulo%204.md)