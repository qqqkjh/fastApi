import unittest
from pandas import Series


class TestDataFrame(unittest.TestCase):
    def test_dataFrame(self):
        raw_data = [50, 100, 200, 300, 400]

        data = Series(raw_data)
        print(data)
        print('')
        print('value = ', data[0])

        data2 = Series([50, 100, 200, 300, 400], index=['2016-02-19',
                                                                   '2016-02-18',
                                                                   '2016-02-17',
                                                                   '2016-02-16',
                                                                   '2016-02-15'])
        print(data2)
        print('')
        print('value = ', data2['2016-02-19'])
        print('')

        for date in data2.index:
            print(date)

        print('-')

        for price in data2.values:
            print(price)

        # 인덱싱 거꾸로
        data3 = Series([50, 100, 200, 300, 400], index=['2016-02-15',
                                                                   '2016-02-16',
                                                                   '2016-02-17',
                                                                   '2016-02-18',
                                                                   '2016-02-19'])
        # 같은 인덱스끼리 오토 매칭 연산
        add = data2 + data3
        print(add)
