#!/usr/bin/python

import sys

def cifra_cesar(texto, chave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) + chave - base) % 26 + base)
        else:
            resultado += char
    return resultado
    
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        sys.exit(1)

def escrever_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
    
def main():
    if len(sys.argv) > 1:
        nome_arquivo = sys.argv[1]
        texto = ler_arquivo(nome_arquivo)
        chave = 3
        texto_cifrado = cifra_cesar(texto, chave)
        print("Texto cifrado:\n",texto_cifrado)
    
        # Salvar o resultado em um novo arquivo
        nome_arquivo_saida = "cifrado_" + nome_arquivo
        escrever_arquivo(nome_arquivo_saida, texto_cifrado)
    else:
        print("Por favor, forneça o nome do arquivo como argumento.")
    
if __name__ == "__main__":
    main()
