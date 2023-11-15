#!/usr/bin/python
import sys

def main():
# Verifica se algum argumento foi passado (além do nome do arquivo)
    if len(sys.argv) > 1:
    # O primeiro argumento após o nome do arquivo é sys.argv[1]
        parametro = sys.argv[1]
        print("O parâmetro fornecido foi:", parametro)
    else:
        print("Nenhum parâmetro foi fornecido.")
    
if __name__ == "__main__":
    main()
