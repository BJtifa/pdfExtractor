from pdfExtractor.utils import route_validate, list_files, extract_text

def pdf_text_extractor(path):
        if not route_validate(path):
            print(f"La ruta: {path} no es válida.")
            return         
        
        files = list_files(path)
        print(f"La ruta: {path} es válida.")
        resultado = extract_text(path, files)
        print(resultado)