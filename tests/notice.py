import pathlib
import unittest

from quant_friend import send_result

HERE = pathlib.Path(__file__).resolve().parent
print(HERE)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # from quant_friend import config_email_sender
        # config_email_sender(  YOUR DATA )
        send_result(['luffy.ja@gmail.com'], "测试", """仅仅一封测试邮件
""", ["{0}/1.jpeg".format(HERE), "{0}/2.jpg".format(HERE)])
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
