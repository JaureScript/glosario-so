# wait() (Llamada al Sistema) / wait() System Call
**Definición formal:** Llamada al sistema mediante la cual un proceso padre bloquea y suspende su propia ejecución hasta que uno de sus procesos hijos termina y devuelve su código de salida[cite: 3].

**Rol Operativo / Utilidad:** Funciona como un mecanismo de *seguridad* y sincronización esencial. Permite al *árbitro* de procesos recolectar el estado de terminación de los hijos, liberando su *control de hardware* (estructuras PCB) y previniendo caídas de *rendimiento* por la acumulación de procesos zombies[cite: 4].

**Cita Bibliográfica formal:** Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Capítulo 3-4.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 5](../Índice%20Módulo%205.md)