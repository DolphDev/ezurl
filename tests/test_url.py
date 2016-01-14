import unittest
from ezurl import Url


class url_correct_test(unittest.TestCase):

    def test_url_is_string_method(self):
        test_url = Url("myurl.com")
        self.assertIsInstance(str(test_url), str)

    def test_url_query_list(self):
        test_url = Url("myurl.com").query(a=[0,1])
        self.assertEqual(str(test_url), "https://myurl.com?a=0+1")

    def test_url_query_single_query(self):
        test_url = Url("myurl.com").query(a=1)
        self.assertEqual(str(test_url), "https://myurl.com?a=1")

    def test_url_query_repeat_queary(self):
        test_url = Url("myurl.com").query(a=2).query(a=1)
        self.assertEqual(str(test_url), "https://myurl.com?a=1")

    def test_url_query_double_query(self):
        test_url = Url("myurl.com").query(a=1).query(b=10)
        self.assertEqual(str(test_url), "https://myurl.com?a=1&b=10")

    def test_url_page(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertEqual(str(test_url), "https://myurl.com/HELLO")
        test_url.page("WORLD")
        self.assertEqual(str(test_url), "https://myurl.com/HELLO/WORLD")

class url_generation_test_type(unittest.TestCase):

    def test_query_gen(self):
        test_url = Url("myurl.com").query(a=[0,1])
        self.assertIsInstance(test_url._query_gen(), str)

    def test_page_gen(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertIsInstance(test_url._page_gen(), str)

def url_generation_equalto(self):

    def test_query_gen(self):
        test_url = Url("myurl.com").query(a=[0,1])
        self.assertEqual(test_url._query_gen(), "?a=0+1")

    def test_page_gen(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertEqual(test_url._page_gen(), ["HELLO"])
        