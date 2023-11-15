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

def servidor(host='0.0.0.0', port=30000, saida=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        print("Servidor escutando...")
        conn, addr = s.accept()
        with conn:
            print(f"Conectado por {addr}")

            with open(saida, 'w', encoding='utf-8') as file:
                while True:
                    dados = conn.recv(1024)
                    if not dados:
                        break
                    # Decodificar os dados recebidos para exibir como string
                    dados_recebidos = dados.decode('utf-8')
                    print("Conteúdo recebido:", dados_recebidos)
                    
                    # Descriptografar os dados antes de salvar
                    dados_decifrados = cifra_cesar(dados.decode(), -3)
                    file.write(dados_decifrados)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nome_arquivo = sys.argv[1]
        servidor(saida=nome_arquivo)
    else:
        print("Por favor, forneça o arquivo de saída")
