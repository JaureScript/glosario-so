# Pila del Kernel / Kernel Stack
**Definición formal:** 
Región de memoria aislada de tamaño fijo asignada a cada hilo del sistema para almacenar sus variables locales, parámetros y direcciones de retorno de forma segura cuando ejecuta código en modo privilegiado[cite: 3].

**Rol Operativo / Utilidad:** 
Constituye una barrera de *seguridad* crítica y una *abstracción* de aislamiento. Permite al *árbitro* gestionar interrupciones y llamadas al sistema con alto *rendimiento*, previniendo que el espacio de usuario malicioso manipule el flujo del *control de hardware* del núcleo[cite: 4].

**Cita Bibliográfica formal:** Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Capítulo 3-4.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 6](../Índice%20Módulo%206.md)
