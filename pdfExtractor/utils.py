import os
import pdfplumber

def route_validate(path):
    return os.path.exists(path)

def list_files(path):
    files =[f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    return files

def extract_text(path,files):
        texto_completo = ""

    
        for filename in files:
            source = os.path.join(path,filename)
            _, ext = os.path.splitext(source)
            if ext == '.pdf':     
                try:
                    with pdfplumber.open(source) as pdf:
                        print("Archivo leido: "+ filename)
                        for page in pdf.pages:
                            page_text = page.extract_text()
                            if page_text:
                                texto_completo += page_text + "\n"

                    txt_name = os.path.splitext(filename)[0] + ".txt"
                    with open(os.path.join(path, txt_name), "w", encoding="utf-8") as f:
                        f.write(texto_completo)
                        print(f"Texto guardado en: {txt_name}")

                except FileNotFoundError:
                    print(f"❌ Archivo no encontrado: {filename}")
                except Exception as e:
                    print(f"❌ Error al extraer texto de {filename}: {e}")
