import argparse
import sys
import pdfplumber

def extract_programmatic_content(text):
    """
    Extrai o conteúdo programático da seção '24.2.3 CARGO 2: AGENTE DE POLÍCIA FEDERAL'.
    """
    start_keywords = ["24.2.3 CARGO 2: AGENTE DE POLÍCIA FEDERAL"]
    end_keywords = ["24.2.4", "CRITÉRIOS DE AVALIAÇÃO", "DISPOSIÇÕES FINAIS"]

    start_index = next((i for i, line in enumerate(text) if any(kw in line.upper() for kw in start_keywords)), None)
    end_index = next((i for i, line in enumerate(text[start_index:], start_index) if any(kw in line.upper() for kw in end_keywords)), None) if start_index is not None else None

    if start_index is not None and end_index is not None:
        return text[start_index:end_index]
    elif start_index is not None:
        return text[start_index:]  # Caso não encontre o final, retorna até o fim do texto
    return []

def extract_edital_content(edital_file):
    """
    Extrai o texto do edital PDF e retorna o conteúdo programático da seção relevante.
    """
    with pdfplumber.open(edital_file) as pdf:
        text = []
        for page in pdf.pages:
            text.extend(page.extract_text().splitlines())  # Dividir o texto em linhas

    # Log para depuração
    with open("debug_edital_text.txt", "w", encoding="utf-8") as debug_file:
        debug_file.write("\n".join(text))

    return extract_programmatic_content(text)

def save_to_file(content, output_file):
    """
    Salva o conteúdo extraído em um arquivo.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in content:
                f.write(line + '\n')
        return True
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Extrator de conteúdo programático de editais")
    parser.add_argument('edital', help="Caminho para o arquivo do edital")
    parser.add_argument('-o', '--output', help="Arquivo de saída (opcional)")
    args = parser.parse_args()

    content = extract_edital_content(args.edital)
    
    if not content:
        print("Nenhum conteúdo programático encontrado ou ocorreu um erro.")
        sys.exit(1)
    
    if args.output:
        if save_to_file(content, args.output):
            print(f"Conteúdo salvo com sucesso em {args.output}")
    else:
        for line in content:
            print(line)

if __name__ == "__main__":
    main()