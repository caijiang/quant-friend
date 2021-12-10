import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        from quant_friend.hosts import list_host
        rs = list_host("ucloud", Tag="123")
        print(rs)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
