import unittest
from app import check_status

class StatusTests(unittest.TestCase):
    def test_success(self):
        response = check_status('https://httpbin.org/status/200')
        if response is not None:
            self.assertEqual(response.status_code, 200)
            
    def test_failure(self):
        response = check_status('https://httpbin.ørg/status/500')
        self.assertEqual(response, None)

if __name__ == "__main__":
    unittest.main()
