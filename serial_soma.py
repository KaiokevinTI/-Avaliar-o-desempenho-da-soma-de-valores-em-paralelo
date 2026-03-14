"""
Solução Serial - Soma de Números em Arquivo

Descrição:
  Lê um arquivo com um número inteiro por linha e calcula a soma total
  de forma serial (uma única thread), medindo o tempo de processamento.

"""

import sys
import time


def soma_serial(filepath: str) -> tuple[int, float]:
    """
    Lê o arquivo e soma todos os números de forma serial.

    Args:
        filepath: caminho para o arquivo de entrada

    Returns:
        (soma_total, tempo_segundos)
    """
    inicio = time.perf_counter()

    soma = 0
    with open(filepath, "r") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                soma += int(linha)

    fim = time.perf_counter()
    tempo = fim - inicio

    return soma, tempo


if __name__ == "__main__":
    # ↓ Altere o caminho abaixo para onde o seu arquivo está salvo
    filepath = r"C:\Users\kkaio\OneDrive\Desktop\numeros\numero2.txt"

    print("=" * 50)
    print("  SOMA SERIAL DE NÚMEROS EM ARQUIVO")
    print("=" * 50)
    print(f"Arquivo: {filepath}")
    print("Processando...\n")

    soma, tempo = soma_serial(filepath)

    print(f"Soma total:             {soma}")
    print(f"Tempo de processamento: {tempo:.6f} segundos")
    print("=" * 50)