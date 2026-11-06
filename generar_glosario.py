import os

def crear_glosario():
    base_dir = "Glosario_Sistemas_Operativos"
    os.makedirs(base_dir, exist_ok=True)

    # Plantilla estricta según la rúbrica
    template = """# {termino_es} / {termino_en}

**Definición formal:**
[Escribe aquí tu explicación técnica rigurosa. Máximo 4 a 6 líneas.]

**Rol Operativo / Utilidad:**
[Explica cómo interviene en el funcionamiento del SO: árbitro, abstracción, control de hardware, seguridad o rendimiento.]

**Cita Bibliográfica formal:**
[Autor. (Año). Título del libro. Editorial. Capítulo X.]

---
**Navegación:** [[Índice Alfabético (A-Z)]] | [[Índice Módulo {modulo}]]
"""

    print("Generando estructura del glosario...")

    # Generar los 300 términos (6 módulos x 50 términos)
    for modulo in range(1, 7):
        folder_name = os.path.join(base_dir, f"Modulo_{modulo}")
        os.makedirs(folder_name, exist_ok=True)
        
        # Crear el índice del módulo
        with open(os.path.join(base_dir, f"Índice Módulo {modulo}.md"), "w", encoding="utf-8") as f:
            f.write(f"# Índice Módulo {modulo}\n\nAquí irán los enlaces a los 50 conceptos de este bloque.\n")

        # Crear los 50 archivos del módulo
        for i in range(1, 51):
            file_name = f"Termino_M{modulo}_{i:02d}.md"
            filepath = os.path.join(folder_name, file_name)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(template.format(
                    termino_es=f"Concepto_{i}",
                    termino_en=f"Concept_{i}",
                    modulo=modulo
                ))

    # Crear el Índice Alfabético global
    with open(os.path.join(base_dir, "Índice Alfabético (A-Z).md"), "w", encoding="utf-8") as f:
        f.write("# Índice Alfabético (A-Z)\n\nA - B - C - D - E - F - G - H - I - J - K - L - M - N - O - P - Q - R - S - T - U - V - W - X - Y - Z\n\n")

    print(f"¡Éxito! 300 archivos generados en la carpeta '{base_dir}'.")

if __name__ == "__main__":
    crear_glosario()