#!/usr/bin/python
import sys

def cifra_cesar(texto, chave):
      resultado = ""

      for i in range(len(texto)):
          char = texto[i]

          if char.isalpha():
             base = ord('A') if char.isupper() else ord('a')
             resultado += chr((ord(char) + chave - base) % 26 + base)
          else:
             resultado += char

      return resultado

def main():
      if len(sys.argv) > 1:
          texto = sys.argv[1]
          chave = 3
          texto_cifrado = cifra_cesar(texto, chave)
          print("Texto cifrado:", texto_cifrado)
      else:
          print("Por favor, forneça uma palavra como argumentos.")

if __name__ == "__main__":
      main()
