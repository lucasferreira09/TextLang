
import sys

from parser import parser
from interpreter import Interpreter


def main():

    print("=" * 50)
    print("                  TextLang")
    print("    Linguagem de Análise de arquivos de texto")
    print("=" * 50)

    if len(sys.argv) != 2:
        print("\nUso:")
        print("  python main.py <arquivo.tl>")
        return

    filename = sys.argv[1]

    print(f"\nPrograma: {filename}")
    print("-" * 50)

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            program = file.read()

    except FileNotFoundError:
        print(f"Erro: programa '{filename}' não encontrado.")
        return

    # Garante que o programa termine com uma quebra de linha.
    if not program.endswith('\n'):
        program += '\n'

    print("Analisando programa...")

    commands = parser.parse(program)

    if commands is None:
        print("Não foi possível analisar o programa.")
        return

    print("Programa analisado com sucesso.")
    print(f"Comandos encontrados: {len(commands)}")

    print("\nExecutando programa...")
    print("-" * 50)

    interpreter = Interpreter()
    interpreter.execute(commands)

    print("-" * 50)
    print("Execução concluída.")
    print("=" * 50)


if __name__ == '__main__':
    main()