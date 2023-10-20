import unittest
from main import archiver, unpacker


class TestArchiver(unittest.TestCase):
    def test_archiver(self):
        compressed_text = archiver('aaaaabbbbbccccdddeee')
        self.assertEqual(compressed_text, 'a5b5c4d3e3')
        # хочу добавить проверку на пустую строку
        compressed_text = archiver('')
        self.assertEqual(compressed_text, '')
        # проверка на строку без повторяющихся символов
        compressed_text = archiver('azdin')
        self.assertEqual(compressed_text, 'a1z1d1i1n1')

    def test_unpacker(self):
        # проверка на распаковку сжатой строки
        empty_text = unpacker("a5b5c4d3e3")
        self.assertEqual(empty_text, 'aaaaabbbbbccccdddeee')
        # проверка на пустую строку
        empty_text = unpacker('')
        self.assertEqual(empty_text, '')
        # проверка на строку без сжатия
        empty_text = unpacker('a1z1d1i1n1')
        self.assertEqual(empty_text, 'azdin')


if __name__ == '__main__':
    unittest.main()
