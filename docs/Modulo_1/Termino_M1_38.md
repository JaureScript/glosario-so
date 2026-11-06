# Copy-on-Write (CoW) / Copy-on-Write
**Definición formal:** 
Estrategia de optimización utilizada en la gestión de memoria y sistemas de archivos donde los recursos duplicados se comparten de lectura hasta que uno de los procesos intenta modificarlos, momento en el cual se realiza una copia física real[cite: 3].

**Rol Operativo / Utilidad:** 
Optimiza de forma drástica el *rendimiento* y la asignación eficiente del *hardware*. Posibilita operaciones operativas críticas, como la creación acelerada de procesos hijos (llamada al sistema fork), evitando duplicaciones costosas en memoria física.

---
**Navegación:** [[Índice Alfabético (A-Z)]] | [[Índice Módulo 1]]
