import unittest
import requests
import json

data = [
  {
    "battery_power": 642,
    "blue": 1,
    "clock_speed": 0.5,
    "dual_sim": 0,
    "fc": 0,
    "four_g": 1,
    "int_memory": 38,
    "m_dep": 0.8,
    "mobile_wt": 86,
    "n_cores": 5,
    "pc": 10,
    "px_height": 887,
    "px_width": 1775,
    "ram": 435,
    "sc_h": 9,
    "sc_w": 2,
    "talk_time": 2,
    "three_g": 1,
    "touch_screen": 1,
    "wifi": 0
  }
]

class TestMain(unittest.TestCase):
    def test_healthcheck(self):
        response = requests.get('http://127.0.0.1:8000/healthcheck')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'true')

    def test_predict(self):
        """This test unit doesn't actually verify the request's result; it only checks that the API accepts input values and returns a response."""
        response = requests.post('http://127.0.0.1:8000/predict', json=data)
        self.assertEqual(response.status_code, 200)

        response_dict = json.loads(response.json())[0]
        self.assertEqual(len(response_dict.keys()), 21)
        self.assertEqual(response_dict['price_range_prediction'], 'Low')

if __name__ == '__main__':
    unittest.main()






