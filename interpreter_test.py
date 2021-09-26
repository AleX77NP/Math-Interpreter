import unittest
from nodes import *
from interpreter import Interpreter
from values import Number


class TestInterpreter(unittest.TestCase):

    def test_numbers(self):
        value = Interpreter().visit(NumberNode(110.5))
        self.assertEqual(value, Number(110.5))

    def test_individual_ops(self):
        value = Interpreter().visit(AddNode(NumberNode(2), NumberNode(4)))
        self.assertEqual(value, Number(6))

        value = Interpreter().visit(SubtractNode(NumberNode(2), NumberNode(4)))
        self.assertEqual(value, Number(-2))

        value = Interpreter().visit(MultiplyNode(NumberNode(2), NumberNode(4)))
        self.assertEqual(value, Number(8))

        value = Interpreter().visit(DivideNode(NumberNode(2), NumberNode(4)))
        self.assertEqual(value, Number(0.5))

        with self.assertRaises(Exception):
            Interpreter().visit(DivideNode(NumberNode(2), NumberNode(0)))

        value = Interpreter().visit(PowerNode(NumberNode(2), NumberNode(4)))
        self.assertEqual(value, Number(16))

        value = Interpreter().visit(ModNode(NumberNode(5), NumberNode(4)))
        self.assertEqual(value, Number(1))

    def test_full_expr(self):
        tree = AddNode(
            NumberNode(26),
            DivideNode(PowerNode(NumberNode(2), NumberNode(4)), NumberNode(16))
        )

        result = Interpreter().visit(tree)
        self.assertEqual(result.value, 27.0)
