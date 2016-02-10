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

    def test_url_hostname(self):
        test_url = Url("myurl.com")
        self.assertEqual(str(test_url), "https://myurl.com")
        test_url.hostname("mynewurl.com")
        self.assertEqual(str(test_url), "https://mynewurl.com")

    def test_url_scheme(self):
        test_url = Url("myurl.com")
        self.assertEqual(str(test_url), "https://myurl.com")
        test_url.scheme("http")
        self.assertEqual(str(test_url), "http://myurl.com")

    def test_fragment_scheme(self):
        test_url = Url("myurl.com").fragment("file1")
        self.assertEqual(str(test_url), "https://myurl.com#file1")
        test_url.fragment("file2")
        self.assertEqual(str(test_url), "https://myurl.com#file2")

    def test_url___query___multi_query(self):
        test_url = Url("myurl.com").query(a="TEST", b="TEST")
        self.assertEqual(dict(test_url.__query__), {"a":"TEST", "b":"TEST"})


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

    def test___query___equalto(self):
        test_url = Url("myurl.com").query(a=[0,1])
        self.assertEqual(test_url.__query__, OrderedDict({"a":"0+1"}))

    def test_page_gen_equalto(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertEqual(test_url._page_gen(), "/HELLO")

    def test_page_equalto(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertEqual(test_url.__pages__, ["HELLO"])

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
        self.assertEqual(urlunparse((test_url.__scheme__,
                        test_url.__hostname__,
                        test_url._page_gen(),
                        "",
                        test_url._query_gen(),
                        test_url.__fragment__)), str(test_url))

    def test_pages_equalto(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertEqual(test_url.pages, test_url.__pages__)

    def test_path_equalto(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertEqual(test_url.path, test_url.url.path)

    def test_netloc_equalto(self):
        test_url = Url("myurl.com")
        self.assertEqual(test_url.netloc, test_url.__hostname__)

    def test_scheme_equalto(self):
        test_url = Url("myurl.com")
        self.assertEqual(test_url.schemes, test_url.__scheme__, "https")

    def test_page_equalto(self):
        test_url = Url("myurl.com").page("HELLO")
        self.assertEqual(test_url.__pages__, ["HELLO"])





class url_attribute_type_test(unittest.TestCase):

    def test___query___type(self):
        test_url = Url("")
        self.assertIsInstance(test_url.__query__, OrderedDict)

    def test_pagetrack_type(self):
        test_url = Url("")
        self.assertIsInstance(test_url.__pages__, list)

    def test_fragement_type(self):
        test_url = Url("")
        self.assertIsInstance(test_url.__fragment__, str)

    def test_hostname_type(self):
        test_url = Url("")
        self.assertIsInstance(test_url.__hostname__, str)

    def test_scheme_type(self):
        test_url = Url("")
        self.assertIsInstance(test_url.__scheme__, str)


