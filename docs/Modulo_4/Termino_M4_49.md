# Spinlock (Espera Activa) / Spinlock
**Definición formal:** 
Mecanismo de bloqueo de baja sobrecarga donde un hilo en espera evalúa repetidamente en un bucle activo (polling) si el recurso compartido ha sido liberado, en lugar de suspenderse[cite: 3].

**Rol Operativo / Utilidad:** 
Es una primitiva de *seguridad* para la exclusión mutua. El *árbitro* la utiliza en sistemas multiprocesador para maximizar el *rendimiento* ante bloqueos muy breves, evitando el costoso cambio de contexto a nivel de *control de hardware*, a costa de consumir ciclos de reloj durante la espera activa[cite: 4].

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 4](../Índice%20Módulo%204.md)