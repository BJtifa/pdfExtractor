from pdfExtractor.core import pdf_text_extractor

def main():
    print("🛠️ pdf extractor \n")
    path = input("Introduce una ruta: ")
    pdf_text_extractor(path)


if __name__ == "__main__":
    main()