import os
import glob
import unicodedata

docs_dir = "docs"

def quitar_acentos(texto):
    # Transforma caracteres acentuados en su versión base (ej. Á -> A)
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def actualizar_indices():
    todos_los_terminos = []

    for modulo in range(1, 7):
        modulo_dir = os.path.join(docs_dir, f"Modulo_{modulo}")
        if not os.path.exists(modulo_dir):
            continue
            
        archivos = glob.glob(os.path.join(modulo_dir, "*.md"))
        terminos_modulo = []
        
        for archivo in archivos:
            with open(archivo, "r", encoding="utf-8") as f:
                primera_linea = f.readline().strip()
                if primera_linea.startswith("#"):
                    titulo = primera_linea.replace("#", "").strip()
                    nombre_archivo = os.path.basename(archivo)
                    
                    ruta_relativa = f"Modulo_{modulo}/{nombre_archivo}"
                    terminos_modulo.append((titulo, f"- [{titulo}]({ruta_relativa})"))
                    todos_los_terminos.append((titulo, ruta_relativa))
        
        # SOLUCIÓN 1: Ordenar el módulo alfabéticamente ignorando acentos
        terminos_modulo.sort(key=lambda x: quitar_acentos(x[0].lower()))
        
        if terminos_modulo:
            with open(os.path.join(docs_dir, f"Índice Módulo {modulo}.md"), "w", encoding="utf-8") as f:
                f.write(f"# Índice Módulo {modulo}\n\n")
                for _, enlace in terminos_modulo:
                    f.write(enlace + "\n")
                f.write("\n")
                
    # SOLUCIÓN 2: Ordenar el índice general ignorando acentos
    todos_los_terminos.sort(key=lambda x: quitar_acentos(x[0].lower())) 
    
    with open(os.path.join(docs_dir, "Índice Alfabético (A-Z).md"), "w", encoding="utf-8") as f:
        f.write("# Índice Alfabético (A-Z)\n\n")
        letra_actual = ""
        for titulo, ruta in todos_los_terminos:
            # Agrupar siempre bajo la letra sin acento
            primera_letra = quitar_acentos(titulo[0]).upper()
            if primera_letra != letra_actual:
                letra_actual = primera_letra
                f.write(f"\n## {letra_actual}\n")
            f.write(f"- [{titulo}]({ruta})\n")

if __name__ == "__main__":
    actualizar_indices()
    print("¡Índices actualizados con orden alfabético y corrección de acentos!")