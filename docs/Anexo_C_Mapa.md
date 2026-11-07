# Anexo C: Mapa de Relaciones

En cumplimiento con los requerimientos del proyecto, el siguiente grafo interactivo demuestra la interconexión teórica y operativa entre conceptos críticos de gestión de memoria virtual. 

El mapa ilustra el ciclo de vida de una solicitud de memoria, partiendo desde la traducción hasta la resolución de un fallo de página, y cómo la saturación de este proceso desemboca en el temido estado de hiperpaginación.

```mermaid
graph TD
    %% Definición de Nodos
    CPU[Proceso en CPU]
    MMU[Memory Management Unit]
    TLB[Translation Lookaside Buffer]
    RAM[Memoria RAM Física]
    PF[Page Fault / Fallo de Página]
    OS[Sistema Operativo / Árbitro]
    SWAP[Almacenamiento Swap]
    THR[Thrashing / Hiperpaginación]
    CPU_DROP[Caída abrupta del rendimiento de CPU]

    %% Relaciones Lógicas
    CPU -->|1. Solicita Dirección Virtual| MMU
    MMU -->|2. Consulta rápida en caché| TLB
    TLB -->|3a. Acierto Hit| RAM
    TLB -->|3b. Fallo Miss| MMU
    MMU -->|4. Revisa Tabla de Páginas| RAM
    MMU -->|5. Bit de validez inválido| PF
    PF -->|6. Genera Interrupción de Hardware| OS
    OS -->|7. Ejecuta rutina y busca bloque| SWAP
    SWAP -->|8. Copia página faltante a| RAM
    
    %% Conexión hacia el colapso (Thrashing)
    PF -->|Si la frecuencia de fallos es extremadamente alta| THR
    THR -->|El sistema pasa más tiempo paginando que ejecutando| CPU_DROP
    
    %% Estilos de los Nodos
    style PF fill:#ffcccc,stroke:#ff0000,stroke-width:2px
    style THR fill:#ff9999,stroke:#cc0000,stroke-width:2px
    style CPU_DROP fill:#ff5252,stroke:#b71c1c,stroke-width:2px,color:#fff
    style SWAP fill:#bbdefb,stroke:#1976d2,stroke-width:2px
    style TLB fill:#c8e6c9,stroke:#388e3c,stroke-width:2px
```