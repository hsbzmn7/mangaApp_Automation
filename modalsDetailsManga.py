from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import time

class TestMangaDetails(unittest.TestCase):

    def setUp(self):
        # Initialize Chrome WebDriver with the Service class
        service = Service(executable_path='C:\Program Files (x86)\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://myalice-automation-test.netlify.app')
        # Assuming you already have login logic here
        self.login()

    def login(self):
        driver = self.driver
        # Init Login
        self.assertIn("React App", driver.title)

        # Credentials Input
        driver.find_element(By.ID, 'username').send_keys('testuser')
        driver.find_element(By.ID, 'password').send_keys('password')
        time.sleep(1)
        # LoginHit
        driver.find_element(By.ID, 'login-btn').click()

        time.sleep(1)

    def test_manga_details_modal(self):
        driver = self.driver
        details_link = driver.find_element(By.XPATH, '//span[text()="Details"]')
        details_link.click()

        time.sleep(1)


        # Verify the modal appears and displays correct information
        modal = driver.find_element(By.CSS_SELECTOR, 'div.bg-white.p-6.rounded-lg.shadow-lg.w-96')
        self.assertTrue(modal.is_displayed())
        time.sleep(1)
        close_button = modal.find_element(By.CSS_SELECTOR, 'button.bg-blue-500.text-white')
        close_button.click()

        # Verify the modal is closed
        #self.assertFalse(modal.is_displayed())
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
