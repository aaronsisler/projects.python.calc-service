import unittest

from src import health_handler


class TestHealthHandler(unittest.TestCase):

    def test_main(self):
        expectedResult = {
            "statusCode": 200,
            "body": '"Service is alive and well"'
        }
        result = health_handler.main(None, None)
        self.assertEqual(expectedResult, result)


if __name__ == '__main__':
    unittest.main()
