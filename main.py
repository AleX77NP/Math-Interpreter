# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

if __name__ == '__main__':
    while True:
        try:
            text = input("calculate > ")
            lexer = Lexer(text)
            tokens = lexer.generate_tokens()
            parser = Parser(tokens)
            tree = parser.parse()
            if not tree: continue
            interpreter = Interpreter()
            value = interpreter.visit(tree)
            print(value)
        except Exception as e:
            print(e)



