import unittest

import calc_handler


class TestCalcHandler(unittest.TestCase):

    def test_main_happy_path(self):
        expectedResult = {
            "statusCode": 200,
            "body": '3'
        }

        event = {'body': '{"value_1":1,"value_2":2}'}

        result = calc_handler.main(event, None)
        self.assertEqual(expectedResult, result)

    def test_main_400_path(self):
        expectedResult = {
            "statusCode": 400,
            "body": '"Please provide 2 values to add"'
        }

        event = {'body': '{}'}

        result = calc_handler.main(event, None)
        self.assertEqual(expectedResult, result)

    def test_main_server_failure_path(self):
        expectedResult = {
            "statusCode": 567,
            "body": '"Something went wrong"'
        }

        event = {'body': ''}

        result = calc_handler.main(event, None)
        self.assertEqual(expectedResult, result)


if __name__ == '__main__':
    unittest.main()
