from unittest import TestCase
from enums import Color


class ColorEnumTest(TestCase):

    def test_color(self, red=None):
        """
            try , except 으로 대부분 예외 처리
            Color(None) 는 해당하는 열거형 value가 없으므로 ValueError 예외처리당한다
        """
        try:
            self.assertEqual(Color.RED.value, Color.RED)
            print(Color["RED"])
            print("------------")
            red_str = "RED"
            print(Color[red_str])
            print("------------")
            print(Color(red_str))
            print("------------")
            print(Color(None))
            print("------------")
            print(Color.RED)
            print("------------")

        except ValueError:
            print('잘못된 밸류.')


