# Cambio de Modo / Mode Switch
**Definición formal:** 
Transición controlada entre el modo de ejecución de usuario y el modo núcleo (y viceversa), desencadenada típicamente por llamadas al sistema (syscalls), excepciones o interrupciones de hardware[cite: 3].

**Rol Operativo / Utilidad:** 
Representa la frontera crítica de *seguridad y protección de hardware*. Garantiza que los procesos de usuario no puedan ejecutar instrucciones privilegiadas por sí mismos, obligándolos a ceder el control al núcleo para arbitrar cualquier modificación del estado del sistema.

---
**Navegación:** [[Índice Alfabético (A-Z)]] | [[Índice Módulo 1]]