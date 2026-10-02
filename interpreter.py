from collections import Counter
import re


class Interpreter:

    def __init__(self):
        self.text = ""
        self.ignore_words = set()
        self.results = []

    def execute(self, commands):
        for command in commands:
            self.execute_command(command)

    def execute_command(self, command):
        name = command[0]

        if name == 'LOAD':
            self.load(command[1])

        elif name == 'LINES':
            self.lines()

        elif name == 'WORDS':
            self.words()

        elif name == 'CHARACTERS':
            self.characters()

        elif name == 'COUNT':
            self.count(command[1])

        elif name == 'SEARCH':
            self.search(command[1])

        elif name == 'FREQUENCY':
            self.frequency()

        elif name == 'TOP':
            self.top(command[1])

        elif name == 'IGNORE':
            self.ignore(command[1])

        elif name == 'REPLACE':
            self.replace(command[1], command[2])

        elif name == 'EXPORT':
            self.export(command[1])

    def load(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.text = file.read()

            self.results.clear()

            print(f"Arquivo '{filename}' carregado com sucesso.")

        except FileNotFoundError:
            print(f"Erro: arquivo '{filename}' não encontrado.")

    def lines(self):
        if not self.check_loaded():
            return

        result = len(self.text.splitlines())

        print(f"Linhas: {result}")
        self.results.append(f"Linhas: {result}")

    def words(self):
        if not self.check_loaded():
            return

        words = self.get_words()
        result = len(words)

        print(f"Palavras: {result}")
        self.results.append(f"Palavras: {result}")

    def characters(self):
        if not self.check_loaded():
            return

        result = len(self.text)

        print(f"Caracteres: {result}")
        self.results.append(f"Caracteres: {result}")

    def count(self, term):
        if not self.check_loaded():
            return

        result = self.text.lower().count(term.lower())

        print(f"'{term}': {result} ocorrência(s)")
        self.results.append(
            f"'{term}': {result} ocorrência(s)"
        )

    def search(self, term):
        if not self.check_loaded():
            return

        found = False

        for line_number, line in enumerate(
            self.text.splitlines(),
            start=1
        ):
            if term.lower() in line.lower():
                print(f"Linha {line_number}: {line}")

                self.results.append(
                    f"Linha {line_number}: {line}"
                )

                found = True

        if not found:
            print(f"'{term}' não encontrado.")

            self.results.append(
                f"'{term}' não encontrado."
            )

    def frequency(self):
        if not self.check_loaded():
            return

        words = self.get_words()
        counter = Counter(words)

        print("Frequência das palavras:")
        self.results.append("Frequência das palavras:")

        for word, quantity in counter.most_common():
            result = f"{word}: {quantity}"

            print(result)
            self.results.append(result)

    def top(self, quantity):
        if not self.check_loaded():
            return

        words = self.get_words()
        counter = Counter(words)

        print(f"Top {quantity} palavras:")
        self.results.append(
            f"Top {quantity} palavras:"
        )

        for word, count in counter.most_common(quantity):
            result = f"{word}: {count}"

            print(result)
            self.results.append(result)

    def ignore(self, words):
        self.ignore_words.update(
            word.lower() for word in words
        )

        print(f"Ignorando: {', '.join(words)}")

    def replace(self, old, new):
        if not self.check_loaded():
            return

        quantity = self.text.count(old)

        self.text = self.text.replace(old, new)

        print(
            f"'{old}' substituído por '{new}' "
            f"({quantity} ocorrência(s))."
        )

        self.results.append(
            f"'{old}' substituído por '{new}' "
            f"({quantity} ocorrência(s))."
        )

    def export(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write('\n'.join(self.results))

            print(f"Resultados exportados para '{filename}'.")

        except OSError as error:
            print(f"Erro ao exportar resultados: {error}")

    def get_words(self):
        words = re.findall(
            r'\b[\wÀ-ÿ]+\b',
            self.text.lower()
        )

        return [
            word
            for word in words
            if word not in self.ignore_words
        ]

    def check_loaded(self):
        if not self.text:
            print("Erro: nenhum arquivo foi carregado.")

            return False

        return True
