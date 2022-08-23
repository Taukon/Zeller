from asyncio.windows_events import NULL
import sys
import unittest
from unittest import result
sys.path.append("c:/Git_directry/python/Naist/")

from src.Zeller import Zeller

class TestZeller(unittest.TestCase):

    def test_入力の正規表現正常(self):
        zeller = Zeller("2022/8/23")
        result = zeller.getDate()
        ans = [2022, 8, 23]
        self.assertEqual(ans, result)

    def test_入力の正規表現エラー(self):
        zeller = Zeller("aaaa/a/a")
        result = zeller.getDate()
        ans = NULL
        self.assertEqual(ans, result)
    
    def test_入力の正規表現数値オーバー(self):
        zeller = Zeller("2022/13/50")
        result = zeller.getDate()
        ans = NULL
        self.assertEqual(ans, result)
    
    def test_入力の正規表現数値オーバー境界値(self):
        zeller = Zeller("2022/2/30")
        result = zeller.getDate()
        ans = NULL
        self.assertEqual(ans, result)

    def test_ツェラーの計算正常(self):
        zeller = Zeller("2022/8/23")
        result = zeller.calcZeller()
        self.assertEqual(2, result)

    def test_ツェラーの計算エラー(self):
        zeller = Zeller("あああ")
        result = zeller.calcZeller()
        self.assertEqual(8, result)

    def test_計算結果の曜日変換正常(self):
        zeller = Zeller("2022/8/23")
        result = zeller.judgeZeller()
        self.assertEqual('火曜日',result)
    
    def test_計算結果の曜日変換エラー(self):
        zeller = Zeller("aaaa")
        result = zeller.judgeZeller()
        self.assertEqual(NULL,result)


if __name__ == '__main__':
    # unittestを実行
    unittest.main()