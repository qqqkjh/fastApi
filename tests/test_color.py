from unittest import TestCase
from enums import Color


class ColorEnumTest(TestCase):

    def test_color(self, red="test"):
        print(Color["RED"])
        print("------------")
        red_str = "RED"
        print(Color[red_str])
        print("------------")
        print(Color(red_str))
        print("------------")
        print(Color(red))
        print("------------")
        self.assertEqual(Color.NULL.value, Color(red).value)
