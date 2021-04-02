import unittest
import customer.profile


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        result = customer.profile.handler(None, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')


if __name__ == '__main__':
    unittest.main()
