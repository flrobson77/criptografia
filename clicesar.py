#!/usr/bin/python

import socket
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

def cliente(host='127.0.0.1', port=30000, arquivo=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        with open(arquivo, 'r') as f:
            while True:
                linha = f.readline()
                if not linha:
                    break
                linha_cifrada = cifra_cesar(linha, 3)
                print ("Mensagem enviada :", linha_cifrada)
                s.sendall(linha_cifrada.encode())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nome_arquivo = sys.argv[1]
        cliente(arquivo=nome_arquivo)
    else:
        print("Por favor, forneça o nome do arquivo como argumento.")
