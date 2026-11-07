# Descriptor Leak / Descriptor Leak
**Definición formal:** 
Error de programación caracterizado por la omisión en el cierre de descriptores de archivo abiertos, provocando el agotamiento progresivo de los recursos del sistema[cite: 3].

**Rol Operativo / Utilidad:** 
Impacta de forma crítica en el *rendimiento* y la estabilidad; exige que el núcleo actúe proactivamente como *árbitro* imponiendo límites estrictos (como *ulimit*) por proceso, evitando que una aplicación defectuosa acapare las tablas de hardware y cause una denegación de servicio.

**Cita Bibliográfica formal:** Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. Capítulo 3-4.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 1](../Índice%20Módulo%201.md)