"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from unittest import TestCase
from src.stack import Node, Stack


class NodeTest(TestCase):

    def test_initialization(self):
        self.assertIsInstance(Node(5, None), Node)
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n1, n2.next_node)


class StackTest(TestCase):

    def test_pushing(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(stack.top.next_node.next_node.next_node, None)

    def test_attribut_error(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        with self.assertRaises(AttributeError):
            stack.top.next_node.next_node.next_node.data

    def test_stack_pop(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.pop(), 'data1')
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.pop(), 'data2')
        self.assertEqual(stack.pop(), 'data1')
        self.assertEqual(stack.pop(), None)
