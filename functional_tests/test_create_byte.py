import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

create_byte_url = "http://localhost:8000/bytes"
MAX_WAIT = 5


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_wait_for_input_new_byte(self):
        start_time = time.time()
        self.browser.get(create_byte_url)
        while True:
            try:
                input_name = self.browser.find_element_by_id("name")
                self.assertIsNotNone(input_name)
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


if __name__ == "__main__":
    unittest.main(warnings="ignore")
