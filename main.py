# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
from lexer import Lexer

if __name__ == '__main__':
    while True:
        text = input("calculate > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        print(list(tokens))

