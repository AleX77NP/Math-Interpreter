import unittest
from tokens import TokenType, Token
from lexer import Lexer


class TestLexer(unittest.TestCase):

    def test_empty(self):
        tokens = list(Lexer("").generate_tokens())
        self.assertEqual(tokens, [])

    def test_empty(self):
        tokens = list(Lexer("\t\n  \t\t\t\n").generate_tokens())
        self.assertEqual(tokens, [])

    def test_numbers(self):
        tokens = list(Lexer("124 56.56 .").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 124.000),
            Token(TokenType.NUMBER, 56.560),
            Token(TokenType.NUMBER, 000.000),
        ])

    def test_operators(self):
        tokens = list(Lexer("+-*/^%").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.PLUS),
            Token(TokenType.MINUS),
            Token(TokenType.MULTIPLY),
            Token(TokenType.DIVIDE),
            Token(TokenType.POWER),
            Token(TokenType.MOD),
        ])

    def test_parens(self):
        tokens = list(Lexer("( )").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.LPAREN),
            Token(TokenType.RPAREN),
        ])

    def test_all(self):
        tokens = list(Lexer("( 45 - 23 ) * 5 % 2").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 45.000),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 23.000),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 5.000),
            Token(TokenType.MOD),
            Token(TokenType.NUMBER, 2.000)
        ])
