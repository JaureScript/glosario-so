# IOMMU (Input/Output Memory Management Unit) / IOMMU
**Definición formal:** 
Componente de hardware especializado que traduce las direcciones de memoria virtual a físicas específicamente para los dispositivos de E/S capaces de realizar acceso directo a memoria (DMA)[cite: 3].

**Rol Operativo / Utilidad:** 
Es la barrera de *seguridad* física definitiva para los periféricos. El *árbitro* la programa para restringir el *control de hardware* de las tarjetas PCI/PCIe, aislando la *abstracción* de memoria y bloqueando ataques de DMA maliciosos sin penalizar el *rendimiento* de transferencia[cite: 4].

**Cita Bibliográfica formal:** Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson. Capítulo 2-3.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 5](../Índice%20Módulo%205.md)
