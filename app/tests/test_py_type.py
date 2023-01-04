import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        skip: int = 0
        limit: int = 10
        fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

        # 배열 0 ~ 10 까지( 총 길이 보다 인덱싱 범위가 넓어도 에러 안남 )
        print(fake_items_db[skip: skip + limit])

        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    """
    모듈을 직접 실행 하면 __main__ 이름을 가지고
    외부 에서 실행 하면 외부에 설정된 __name__ 값을 따라 간다
    """
    unittest.main()
