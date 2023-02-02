from unittest import TestCase
from pandas import Series, DataFrame


class Test(TestCase):
    def test_df(self):
        example_data = [
                {
                    "학번": 'test-1',
                    "학적1": 5,
                    "학적2": 4,
                    "학적3": 1,
                    "나이": 49,
                    "성별": 0,
                    "학과": 21,
                    "휴학1학기": 0,
                    "휴학2학기": 0,
                    "휴학1년": 1,
                    "장학1학기": 0,
                    "장학2학기": 1,
                    "장학1년": 2,
                    "입학구분": 3,
                    "접속횟수3월": 34,
                    "접속횟수4월": 39,
                    "접속횟수5월": 39,
                    "접속횟수6월": 34,
                    "접속횟수7월": 7,
                    "접속횟수8월": 12,
                    "접속횟수9월": 33,
                    "접속횟수10월": 37,
                    "접속횟수11월": 37,
                    "접속횟수12월": 24,
                    "접속횟수합계": 294,
                    "출석횟수1학기": 170,
                    "결석횟수1학기": 0,
                    "출석횟수2학기": 169,
                    "지각횟수2학기": 0,
                    "출석횟수1년": 339,
                    "지각횟수1년": 0,
                    "토론참여1학기": 1,
                    "토론참여2학기": 7,
                    "토론참여1년": 8,
                    "상담1학기": 1,
                    "상담2학기": 0,
                    "상담1년": 1,
                    "총점평균1학기": 87,
                    "성적등급1학기": 7,
                    "총점평균2학기": 88,
                    "성적등급2학기": 7,
                    "리포트점수1학기": 13.83,
                    "리포트기간내1학기": 6,
                    "리포트기간외1학기": 0,
                    "리포트점수2학기": 17,
                    "리포트기간내2학기": 6,
                    "리포트기간외2학기": 0
                },
                {
                    "학번": 'test-2',
                    "학적1": 5,
                    "학적2": 4,
                    "학적3": 1,
                    "나이": 54,
                    "성별": 1,
                    "학과": 21,
                    "휴학1학기": 0,
                    "휴학2학기": 0,
                    "휴학1년": 1,
                    "장학1학기": 1,
                    "장학2학기": 1,
                    "장학1년": 3,
                    "입학구분": 3,
                    "접속횟수3월": 34,
                    "접속횟수4월": 40,
                    "접속횟수5월": 28,
                    "접속횟수6월": 33,
                    "접속횟수7월": 7,
                    "접속횟수8월": 4,
                    "접속횟수9월": 17,
                    "접속횟수10월": 19,
                    "접속횟수11월": 41,
                    "접속횟수12월": 16,
                    "접속횟수합계": 234,
                    "출석횟수1학기": 182,
                    "결석횟수1학기": 0,
                    "출석횟수2학기": 171,
                    "지각횟수2학기": 0,
                    "출석횟수1년": 353,
                    "지각횟수1년": 0,
                    "토론참여1학기": 9,
                    "토론참여2학기": 0,
                    "토론참여1년": 9,
                    "상담1학기": 1,
                    "상담2학기": 0,
                    "상담1년": 1,
                    "총점평균1학기": 86,
                    "성적등급1학기": 7,
                    "총점평균2학기": 88,
                    "성적등급2학기": 7,
                    "리포트점수1학기": 13.83,
                    "리포트기간내1학기": 6,
                    "리포트기간외1학기": 0,
                    "리포트점수2학기": 14.33,
                    "리포트기간내2학기": 6,
                    "리포트기간외2학기": 0
                },
                {
                    "학번": 'test-3',
                    "학적1": 5,
                    "학적2": 4,
                    "학적3": 1,
                    "나이": 52,
                    "성별": 1,
                    "학과": 21,
                    "휴학1학기": 0,
                    "휴학2학기": 0,
                    "휴학1년": 1,
                    "장학1학기": 1,
                    "장학2학기": 1,
                    "장학1년": 3,
                    "입학구분": 3,
                    "접속횟수3월": 35,
                    "접속횟수4월": 19,
                    "접속횟수5월": 22,
                    "접속횟수6월": 14,
                    "접속횟수7월": 7,
                    "접속횟수8월": 2,
                    "접속횟수9월": 2,
                    "접속횟수10월": 14,
                    "접속횟수11월": 19,
                    "접속횟수12월": 22,
                    "접속횟수합계": 150,
                    "출석횟수1학기": 131,
                    "결석횟수1학기": 0,
                    "출석횟수2학기": 156,
                    "지각횟수2학기": 0,
                    "출석횟수1년": 287,
                    "지각횟수1년": 0,
                    "토론참여1학기": 11,
                    "토론참여2학기": 0,
                    "토론참여1년": 11,
                    "상담1학기": 1,
                    "상담2학기": 1,
                    "상담1년": 2,
                    "총점평균1학기": 84,
                    "성적등급1학기": 6,
                    "총점평균2학기": 91,
                    "성적등급2학기": 8,
                    "리포트점수1학기": 13.6,
                    "리포트기간내1학기": 4,
                    "리포트기간외1학기": 1,
                    "리포트점수2학기": 14.83,
                    "리포트기간내2학기": 6,
                    "리포트기간외2학기": 0
                },
                {
                    "학번": 'test-4',
                    "학적1": 5,
                    "학적2": 4,
                    "학적3": 1,
                    "나이": 53,
                    "성별": 1,
                    "학과": 21,
                    "휴학1학기": 0,
                    "휴학2학기": 0,
                    "휴학1년": 1,
                    "장학1학기": 1,
                    "장학2학기": 1,
                    "장학1년": 3,
                    "입학구분": 3,
                    "접속횟수3월": 68,
                    "접속횟수4월": 57,
                    "접속횟수5월": 36,
                    "접속횟수6월": 38,
                    "접속횟수7월": 7,
                    "접속횟수8월": 6,
                    "접속횟수9월": 38,
                    "접속횟수10월": 55,
                    "접속횟수11월": 36,
                    "접속횟수12월": 33,
                    "접속횟수합계": 368,
                    "출석횟수1학기": 143,
                    "결석횟수1학기": 0,
                    "출석횟수2학기": 155,
                    "지각횟수2학기": 0,
                    "출석횟수1년": 298,
                    "지각횟수1년": 0,
                    "토론참여1학기": 3,
                    "토론참여2학기": 1,
                    "토론참여1년": 4,
                    "상담1학기": 1,
                    "상담2학기": 1,
                    "상담1년": 2,
                    "총점평균1학기": 91,
                    "성적등급1학기": 8,
                    "총점평균2학기": 91,
                    "성적등급2학기": 7,
                    "리포트점수1학기": 13,
                    "리포트기간내1학기": 5,
                    "리포트기간외1학기": 0,
                    "리포트점수2학기": 17.17,
                    "리포트기간내2학기": 5,
                    "리포트기간외2학기": 1
                },
                {
                    "학번": 'test-5',
                    "학적1": 5,
                    "학적2": 4,
                    "학적3": 1,
                    "나이": 31,
                    "성별": 1,
                    "학과": 21,
                    "휴학1학기": 0,
                    "휴학2학기": 0,
                    "휴학1년": 1,
                    "장학1학기": 1,
                    "장학2학기": 1,
                    "장학1년": 3,
                    "입학구분": 3,
                    "접속횟수3월": 19,
                    "접속횟수4월": 17,
                    "접속횟수5월": 19,
                    "접속횟수6월": 16,
                    "접속횟수7월": 7,
                    "접속횟수8월": 6,
                    "접속횟수9월": 24,
                    "접속횟수10월": 24,
                    "접속횟수11월": 21,
                    "접속횟수12월": 22,
                    "접속횟수합계": 168,
                    "출석횟수1학기": 167,
                    "결석횟수1학기": 0,
                    "출석횟수2학기": 182,
                    "지각횟수2학기": 0,
                    "출석횟수1년": 349,
                    "지각횟수1년": 0,
                    "토론참여1학기": 1,
                    "토론참여2학기": 2,
                    "토론참여1년": 3,
                    "상담1학기": 1,
                    "상담2학기": 0,
                    "상담1년": 1,
                    "총점평균1학기": 88,
                    "성적등급1학기": 7,
                    "총점평균2학기": 94,
                    "성적등급2학기": 8,
                    "리포트점수1학기": 15,
                    "리포트기간내1학기": 4,
                    "리포트기간외1학기": 0,
                    "리포트점수2학기": 19.83,
                    "리포트기간내2학기": 6,
                    "리포트기간외2학기": 0
                },
                {
                    "학번": 'test-6',
                    "학적1": 5,
                    "학적2": 4,
                    "학적3": 1,
                    "나이": 56,
                    "성별": 0,
                    "학과": 21,
                    "휴학1학기": 0,
                    "휴학2학기": 0,
                    "휴학1년": 1,
                    "장학1학기": 1,
                    "장학2학기": 1,
                    "장학1년": 3,
                    "입학구분": 3,
                    "접속횟수3월": 30,
                    "접속횟수4월": 35,
                    "접속횟수5월": 23,
                    "접속횟수6월": 38,
                    "접속횟수7월": 7,
                    "접속횟수8월": 6,
                    "접속횟수9월": 36,
                    "접속횟수10월": 36,
                    "접속횟수11월": 30,
                    "접속횟수12월": 31,
                    "접속횟수합계": 268,
                    "출석횟수1학기": 117,
                    "결석횟수1학기": 0,
                    "출석횟수2학기": 145,
                    "지각횟수2학기": 0,
                    "출석횟수1년": 262,
                    "지각횟수1년": 0,
                    "토론참여1학기": 0,
                    "토론참여2학기": 8,
                    "토론참여1년": 8,
                    "상담1학기": 2,
                    "상담2학기": 0,
                    "상담1년": 2,
                    "총점평균1학기": 84,
                    "성적등급1학기": 6,
                    "총점평균2학기": 88,
                    "성적등급2학기": 7,
                    "리포트점수1학기": 13,
                    "리포트기간내1학기": 4,
                    "리포트기간외1학기": 0,
                    "리포트점수2학기": 17.4,
                    "리포트기간내2학기": 5,
                    "리포트기간외2학기": 0
                },
                {
                    "학번": 'test-7',
                    "학적1": 2,
                    "학적2": 2,
                    "학적3": 0,
                    "나이": 40,
                    "성별": 1,
                    "학과": 21,
                    "휴학1학기": 0,
                    "휴학2학기": 0,
                    "휴학1년": 1,
                    "장학1학기": 0,
                    "장학2학기": 0,
                    "장학1년": 1,
                    "입학구분": 3,
                    "접속횟수3월": 10,
                    "접속횟수4월": 24,
                    "접속횟수5월": 12,
                    "접속횟수6월": 28,
                    "접속횟수7월": 7,
                    "접속횟수8월": 1,
                    "접속횟수9월": 18,
                    "접속횟수10월": 30,
                    "접속횟수11월": 20,
                    "접속횟수12월": 23,
                    "접속횟수합계": 166,
                    "출석횟수1학기": 182,
                    "결석횟수1학기": 0,
                    "출석횟수2학기": 182,
                    "지각횟수2학기": 0,
                    "출석횟수1년": 364,
                    "지각횟수1년": 0,
                    "토론참여1학기": 7,
                    "토론참여2학기": 0,
                    "토론참여1년": 7,
                    "상담1학기": 3,
                    "상담2학기": 1,
                    "상담1년": 4,
                    "총점평균1학기": 90,
                    "성적등급1학기": 7,
                    "총점평균2학기": 90,
                    "성적등급2학기": 7,
                    "리포트점수1학기": 12.33,
                    "리포트기간내1학기": 5,
                    "리포트기간외1학기": 1,
                    "리포트점수2학기": 14.57,
                    "리포트기간내2학기": 5,
                    "리포트기간외2학기": 2
                }
        ]

        df = DataFrame(example_data);

        print(df)