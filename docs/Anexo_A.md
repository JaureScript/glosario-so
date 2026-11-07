# Anexo A: Diagramas y Flujogramas Ilustrativos

En esta sección se exponen los esquemas visuales que describen la arquitectura y las transiciones internas del Sistema Operativo, vinculados directamente a los conceptos teóricos desarrollados en el glosario.

## 1. Transiciones de Estados del Proceso
*(Conceptos vinculados: Proceso, Planificación de CPU, PCB, Cambio de Contexto, Interrupción).*

```mermaid
stateDiagram-v2
    direction LR
    [*] --> Nuevo : fork()
    Nuevo --> Listo : Admitido
    Listo --> Ejecución : Planificador (Despacho)
    Ejecución --> Listo : Interrupción / Fin de Quántum
    Ejecución --> Bloqueado : Llamada a E/S (Syscall)
    Bloqueado --> Listo : E/S Completada
    Ejecución --> Terminado : exit()
    Terminado --> [*]
```

## 2. Traducción de Memoria (MMU y TLB)
*(Conceptos vinculados: Memoria Virtual, Paginación, MMU, TLB, Fallo de Página, Swapping).*

```mermaid
flowchart TD
    CPU[CPU / Proceso] -->|Dirección Virtual| TLB{"¿Acierto en TLB?"}
    TLB -->|Hit Sí| FISICA[Dirección Física en RAM]
    TLB -->|Miss No| MMU[MMU consulta Tabla de Páginas]
    MMU -->|Página Válida| RAM[(Memoria RAM)]
    MMU -->|Página Inválida| PF[Fallo de Página / Page Fault]
    PF --> SO[Intervención del Sistema Operativo]
    SO -->|Trae bloque| DISCO[(Disco Secundario / Swap)]
    DISCO --> RAM
    RAM --> FISICA
```


## 3. Anillos de Protección (Jerarquía de Privilegios)
*(Conceptos vinculados: Ring 0, Ring 3, Modo Kernel, Modo Usuario, Llamadas al Sistema).*

```mermaid
flowchart TD
    R3[Ring 3: Modo Usuario] -->|Llamadas al Sistema| R0
    R2[Ring 2: Drivers de Dispositivos] --> R0
    R1[Ring 1: Drivers Básicos] --> R0
    R0[Ring 0: Modo Kernel]
    
    subgraph Descripción
    d3(Aplicaciones regulares, aislamiento estricto de seguridad)
    d0(Acceso irrestricto, control de hardware absoluto)
    end
    
    R3 -.-> d3
    R0 -.-> d0

    style R3 fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style R0 fill:#ffcdd2,stroke:#d32f2f,stroke-width:2px
```

## 4. Arquitectura de Contenedores vs Máquinas Virtuales
*(Conceptos vinculados: Máquina Virtual, Hipervisor, Contenedores, Cgroups, Namespaces).*

```mermaid
flowchart LR
    subgraph Máquinas_Virtuales [Máquinas Virtuales]
        direction BT
        HW1[Hardware Físico] --> HYP[Hipervisor / VMM]
        HYP --> GOS1[Guest OS 1]
        HYP --> GOS2[Guest OS 2]
        GOS1 --> A1[App A + Libs]
        GOS2 --> A2[App B + Libs]
    end

    subgraph Contenedores [Arquitectura de Contenedores]
        direction BT
        HW2[Hardware Físico] --> HOST[SO Anfitrión]
        HOST --> ENG[Motor de Contenedores]
        ENG --> C1[App A + Bin/Libs]
        ENG --> C2[App B + Bin/Libs]
    end
    
    style HYP fill:#fff3e0,stroke:#f57c00
    style ENG fill:#e8f5e9,stroke:#388e3c
```