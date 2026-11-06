# Anexo C: Mapa de Relaciones (Gestión de Memoria Virtual)

A continuación se ilustra la interconexión técnica entre los componentes de hardware y software durante el acceso a la memoria y la resolución de un fallo de página.

```mermaid
graph TD
    A[CPU] -->|Genera Dirección Virtual| B(MMU)
    B -->|Consulta rápida| C{TLB}
    C -->|TLB Hit| D[Memoria Física / RAM]
    C -->|TLB Miss| E[Tabla de Páginas]
    E -->|Bit de Presencia = 1| D
    E -->|Bit de Presencia = 0| F((Page Fault))
    F -->|Rutina del SO| G[Disco de Intercambio / Swap]
    G -->|Carga página| D
    F -.->|Si hay exceso de fallos| H((Thrashing / Hiperpaginado))
    H -.->|Degrada| I[Rendimiento del SO]