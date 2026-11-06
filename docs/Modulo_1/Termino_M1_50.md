# E/S por Interrupciones / Interrupt-Driven I/O
**Definición formal:** 
Método de gestión de entrada/salida donde el dispositivo periférico genera una señal de interrupción al finalizar una operación, liberando a la CPU de realizar sondeos continuos (polling)[cite: 3].

**Rol Operativo / Utilidad:** 
Incrementa sustancialmente el *rendimiento* arquitectónico, delegando la reactividad del *control de hardware* al controlador de interrupciones asíncrono. Esto evita bloqueos síncronos innecesarios por parte de la CPU mientras los dispositivos periféricos resuelven operaciones lentas.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 1](../Índice%20Módulo%201.md)