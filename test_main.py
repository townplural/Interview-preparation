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

    def test_task_2_True(self):
        string6 = '(((([{}]))))'
        st = Stack(string6)
        expected = True
        result = st.task_2()
        self.assertEqual(expected, result)

    def test_task_2_False(self):
        string7 = '}{}'
        st = Stack(string7)
        expected = False
        result = st.task_2()
        self.assertEqual(expected, result)
