# Instrucción Privilegiada / Privileged Instruction
**Definición formal:** 
Instrucción de procesador cuya ejecución solo está permitida cuando el sistema se encuentra en modo núcleo (Ring 0), ya que su uso incorrecto podría comprometer la estabilidad y seguridad del sistema.

**Rol Operativo / Utilidad:** 
Es la frontera física que garantiza la *seguridad* absoluta del *control de hardware*. El procesador bloquea estas instrucciones si provienen del espacio de usuario, obligando a las aplicaciones a solicitar la intermediación del *árbitro* mediante llamadas al sistema.

**Cita Bibliográfica formal:** Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). *Operating Systems: Three Easy Pieces*. Arpaci-Dusseau Books. Capítulo 15-16.

---
**Navegación:** [Índice Alfabético (A-Z)](../Índice%20Alfabético%20(A-Z).md) | [Índice Módulo 2](../Índice%20Módulo%202.md)