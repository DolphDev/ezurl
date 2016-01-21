import unittest
from collections import OrderedDict
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

    def test_url_querytrack_multi_query(self):
        test_url = Url("myurl.com").query(a="TEST", b="TEST")
        self.assertEqual(dict(test_url.querytrack), {"a":"TEST", "b":"TEST"})


class url_generation_test_type(unittest.TestCase):

    def test_query_gen_type(self):
        test_url = Url("myurl.com").query(a=[0,1])
        self.assertIsInstance(test_url._query_gen(), str)

    def test_page_gen_type(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertIsInstance(test_url._page_gen(), str)

class url_generation_equalto(unittest.TestCase):

    def test_query_gen_equalto(self):
        test_url = Url("myurl.com").query(a=[0,1])
        self.assertEqual(test_url._query_gen(), "a=0+1")

    def test_querytrack_equalto(self):
        test_url = Url("myurl.com").query(a=[0,1])
        self.assertEqual(test_url.querytrack, OrderedDict({"a":"0+1"}))

    def test_page_gen_equalto(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertEqual(test_url._page_gen(), "/HELLO")

    def test_page_equalto(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertEqual(test_url.pagestrack, ["HELLO"])

class url_properties_test(unittest.TestCase):

    def test_url_urlparse_equalto(self):
        try: from urlparse import urlparse #PY2
        except ImportError: from urllib.parse import urlparse #PY3
        test_url = Url("myurl.com")
        self.assertEqual(urlparse(str(test_url)), test_url.url)

    def test_url_unurlparse_equalto(self):
        try: from urlparse import urlunparse #PY2
        except ImportError: from urllib.parse import urlunparse #PY3
        test_url = Url("myurl.com")
        self.assertEqual(urlunparse((test_url.schemetrack,
                        test_url.hostnametrack,
                        test_url._page_gen(),
                        "",
                        test_url._query_gen(),
                        test_url.fragmenttrack)), str(test_url))

    def test_pages_equalto(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertEqual(test_url.pages, test_url.pagestrack)

    def test_path_equalto(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertEqual(test_url.path, test_url.url.path)

    def test_netloc_equalto(self):
        test_url = Url("myurl.com")
        self.assertEqual(test_url.netloc, test_url.hostnametrack)

    def test_scheme_equalto(self):
        test_url = Url("myurl.com")
        self.assertEqual(test_url.scheme, test_url.schemetrack, "https")

    def test_page_equalto(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertEqual(test_url.pagestrack, ["HELLO"])



class url_attribute_type_test(unittest.TestCase):

    def test_querytrack_type(self):
        test_url = Url("")
        self.assertIsInstance(test_url.querytrack, OrderedDict)

    def test_pagetrack_type(self):
        test_url = Url("")
        self.assertIsInstance(test_url.pagestrack, list)

    def test_fragement_type(self):
        test_url = Url("")
        self.assertIsInstance(test_url.fragmenttrack, str)

