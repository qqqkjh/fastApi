import unittest
from pandas import Series, DataFrame


class TestDataFrame(unittest.TestCase):
    def test_dataFrame(self):
        # 딕셔너리를 통한 생성
        raw_data = {'col0': [1, 2, 3, 4],
                    'col1': [10, 20, 30, 40],
                    'col2': [100, 200, 300, 400]}

        data = DataFrame(raw_data)
        print(data)
        print('Series Type ? :', isinstance(data['col0'], Series))

        raw_data['col3'] = [9, 9, 9, 9]
        data2 = DataFrame(raw_data, columns=['col2', 'col1', 'col0', 'col3'])
        print(data2)

        # 배열을 통한 접근 -> 새로운 인스턴스 (읽기전용)
        print(data2[['col3', 'col3', 'col1', 'col0']])

        # 중복컬럼 설정 새로운 인스턴스
        data3 = data2[['col3', 'col3', 'col1', 'col0']]

        # 중복 컬럼은 동시에 가져온다
        print(data3['col3'])
        print('')

        index = ['2016-02-19',
                 '2016-02-18',
                 '2016-02-17',
                 '2016-02-16']

        data4 = DataFrame(raw_data, columns=['col2', 'col1', 'col0', 'col3'], index=index)
        print('시리즈를 통한 접근 : ', )
        print(data4['col2']['2016-02-19'])
        print('인덱스를 통한 접근 loc : ', )
        print(data4['col2'].loc['2016-02-19'])

        # 1 시리즈 = 테이블 1 row
        print(data4.loc['2016-02-18'])

        # → 가로축
        print(data4.columns)

        # ↓ 세로축
        print(data4.index)
