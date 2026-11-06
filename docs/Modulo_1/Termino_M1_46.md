# Dirty Bit / Dirty Bit
**Definición formal:** 
Bit indicador dentro de una entrada de tabla de páginas (PTE) que se activa automáticamente cuando el contenido de la página virtual ha sido modificado, indicando que debe ser reescrito en el disco de intercambio antes de ser desalojado[cite: 3].

**Rol Operativo / Utilidad:** 
Optimiza drásticamente el *rendimiento* de la gestión de memoria virtual y reduce el desgaste por *control de hardware* de E/S, asegurando que el núcleo solo incurra en costosas escrituras físicas a disco cuando los datos en memoria realmente han mutado.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 1](../Índice%20Módulo%201.md)