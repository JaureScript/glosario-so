# Anexo B: Trazas de Terminal y Código de Ejemplo

En esta sección se evidencian comandos reales ejecutados en entornos GNU/Linux y fragmentos de código en C, demostrando la aplicación práctica de los conceptos teóricos de llamadas al sistema, gestión de memoria y concurrencia[cite: 2].

## 1. Trazas de Comandos GNU/Linux

**Auditoría de llamadas al sistema con `strace`:**
*(Demuestra cómo un proceso en Modo Usuario solicita servicios al Modo Kernel mediante syscalls)*.
```bash
$ strace -c ls
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 24.30    0.000185          10        18           mmap
 18.26    0.000139          13        10           openat
 11.83    0.000090           9        10           mprotect
  9.46    0.000072           9         8           read
  8.02    0.000061           8         7         1 access
------ ----------- ----------- --------- --------- ----------------
```

**Mapa de Memoria de un Proceso con `pmap`:**
*(Evidencia la segmentación de memoria virtual del proceso: texto, datos y bibliotecas compartidas)*.
```bash
$ pmap -x 1234
1234:   /usr/sbin/nginx -g daemon off;
Address           Kbytes     RSS   Dirty Mode  Mapping
000055c1b6910000    1024     768       0 r-x-- nginx
000055c1b6b10000      64      64      64 rw--- nginx
00007fc8d4a00000    2048     512       0 r-x-- libc.so.6
```

## 2. Código de Ejemplo en C: Procesos, Hilos y Mutex

*(Demuestra la creación de procesos pesados con `fork`, la generación de hilos ligeros con `pthreads` y la protección de una Sección Crítica de memoria compartida mediante exclusión mutua `mutex`)[cite: 2].*
```c
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/types.h>

pthread_mutex_t lock;
int contador_critico = 0;

// Función que ejecutarán los hilos
void* incrementar_contador(void* arg) {
    pthread_mutex_lock(&lock); // Entrada a Sección Crítica (Bloqueo del árbitro)
    contador_critico++;
    printf("Hilo en ejecución. Contador crítico: %d\n", contador_critico);
    pthread_mutex_unlock(&lock); // Salida de Sección Crítica (Liberación)
    return NULL;
}

int main() {
    // 1. Creación de un proceso hijo
    pid_t pid = fork(); 

    if (pid == 0) {
        // Espacio del proceso hijo
        printf("Proceso Hijo (PID: %d) creado exitosamente.\n", getpid());
    } else if (pid > 0) {
        // Espacio del proceso padre
        printf("Proceso Padre (PID: %d). Generando hilos concurrentes...\n", getpid());
        
        pthread_t hilo1, hilo2;
        pthread_mutex_init(&lock, NULL);
        
        // 2. Creación de hilos concurrentes
        pthread_create(&hilo1, NULL, incrementar_contador, NULL);
        pthread_create(&hilo2, NULL, incrementar_contador, NULL);
        
        // 3. Espera de finalización
        pthread_join(hilo1, NULL);
        pthread_join(hilo2, NULL);
        pthread_mutex_destroy(&lock);
    }
    
    return 0;
}
```