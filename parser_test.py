import unittest
from tokens import TokenType, Token
from parser_ import Parser
from nodes import *


class TestParser(unittest.TestCase):

    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 12.3)]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(12.3))

    def test_individual_ops(self):
        tokens = [
            Token(TokenType.NUMBER, 12.3),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 4)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(12.3), NumberNode(4.0)))

        tokens = [
            Token(TokenType.NUMBER, 20 ),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 7.5)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(NumberNode(20), NumberNode(7.5)))

        tokens = [
            Token(TokenType.NUMBER, 45),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 2)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(45.0), NumberNode(2.0)))

        tokens = [
            Token(TokenType.NUMBER, 90),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 2)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(90), NumberNode(2)))

        tokens = [
            Token(TokenType.NUMBER, 2),
            Token(TokenType.POWER),
            Token(TokenType.NUMBER, 5)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, PowerNode(NumberNode(2), NumberNode(5)))

        tokens = [
            Token(TokenType.NUMBER, 5),
            Token(TokenType.MOD),
            Token(TokenType.NUMBER, 2)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, ModNode(NumberNode(5), NumberNode(2)))

    def test_full_expr(self):
        tokens = [
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 45.000),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 23.000),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 5.000),
            Token(TokenType.MOD),
            Token(TokenType.NUMBER, 2.000)
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, ModNode(MultiplyNode(SubtractNode(NumberNode(45.0), NumberNode(23.0)),NumberNode(5.0)), NumberNode(2.0)))
