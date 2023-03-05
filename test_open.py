import unittest
from open import autocomplete

prefixes = ['abc123', 'abc234', "def100", "ghi100", "ghi234"]


class TestAutcomplete(unittest.TestCase):
    """Test class for folder-opener's autocomplete function"""

    def test_autocomplete_exact_match(self):
        self.assertEqual(autocomplete("abc123", prefixes), "abc123")

    def test_autocomplete_start1(self):
        self.assertEqual(autocomplete("abc12", prefixes), "abc123")

    def test_autocomplete_start2(self):
        self.assertEqual(autocomplete("def", prefixes), "def100")

    def test_autocomplete_end(self):
        self.assertEqual(autocomplete("123", prefixes), "abc123")

    def test_autocomplete_no_match(self):
        with self.assertRaises(ValueError):
            autocomplete("123abc", prefixes)
            autocomplete("aef", prefixes)

    def test_autocomplete_multi_match(self):
        with self.assertRaises(ValueError):
            autocomplete("234", prefixes)


if __name__ == '__main__':
    unittest.main()
