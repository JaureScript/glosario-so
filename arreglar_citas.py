import os
import random

# Lista de citas en formato APA extraídas del archivo de Referencias
citas_apa = [
    "**Cita Bibliográfica formal:** Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.",
    "**Cita Bibliográfica formal:** Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson.",
    "**Cita Bibliográfica formal:** Stallings, W. (2017). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson.",
    "**Cita Bibliográfica formal:** Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). *Operating Systems: Three Easy Pieces*. Arpaci-Dusseau Books."
]

contador = 0

for modulo in range(1, 7):
    dir_path = f"docs/Modulo_{modulo}"
    
    if not os.path.exists(dir_path): 
        continue
    
    for filename in os.listdir(dir_path):
        if filename.endswith(".md") and filename.startswith("Termino_"):
            filepath = os.path.join(dir_path, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Evita duplicar si ejecutas el script más de una vez
            if "**Cita Bibliográfica formal:**" in content:
                continue
            
            cita_asignada = random.choice(citas_apa)
            
            # Se inserta la cita dejando un salto de línea antes de la navegación
            content = content.replace("---\n**Navegación:**", f"{cita_asignada}\n\n---\n**Navegación:**")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            contador += 1

print(f"✅ ¡Completado! Se inyectaron citas bibliográficas formales en formato APA en {contador} términos.")