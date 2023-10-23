import unittest
from unittest import TestCase
from main import Stack


class CheckStack(TestCase):

    def test_is_empty_false(self):
        string1 = 'asd'
        st = Stack(string1)
        expected1 = False
        result = st.is_empty()
        self.assertEqual(expected1, result)

    def test_pop(self):
        string3 = 'asd'
        st = Stack(string3)
        expected = 'd'
        result = st.pop()
        self.assertEqual(result, expected)

    def test_peek(self):
        string4 = 'asd'
        st = Stack(string4)
        expected = 'd'
        result = st.peek()
        self.assertEqual(result, expected)

    def test_size(self):
        string5 = 'asd'
        st = Stack(string5)
        expected = 3
        result = st.size()
        self.assertEqual(result, expected)

    def test_string1(self):
        string1 = '(((([{}]))))'
        stack = Stack(string1)
        result = stack.task_2()
        expected = True
        self.assertEqual(expected, result)

    def test_string2(self):
        string2 = '[([])((([[[]]])))]{()}'
        stack = Stack(string2)
        result = stack.task_2()
        expected = True
        self.assertEqual(expected, result)

    def test_string3(self):
        string3 = '{{[()]}}'
        stack = Stack(string3)
        result = stack.task_2()
        expected = True
        self.assertEqual(expected, result)

    def test_string4(self):
        string4 = '}{}'
        stack = Stack(string4)
        result = stack.task_2()
        expected = False
        self.assertEqual(expected, result)

    def test_string5(self):
        string5 = '{{[(])]}}'
        stack = Stack(string5)
        result = stack.task_2()
        expected = False
        self.assertEqual(expected, result)

    def test_string6(self):
        string6 = '[[{())}]'
        stack = Stack(string6)
        result = stack.task_2()
        expected = False
        self.assertEqual(expected, result)
