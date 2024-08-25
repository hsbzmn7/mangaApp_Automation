from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import time

class TestMangaSearch(unittest.TestCase):

    def setUp(self):
        # Path Set Up
        service = Service(executable_path='C:\Program Files (x86)\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://myalice-automation-test.netlify.app')

    def test_login(self):
        driver = self.driver
        # Init Login
        self.assertIn("React App", driver.title)

        # Credentials Input
        driver.find_element(By.ID, 'username').send_keys('testuser')
        driver.find_element(By.ID, 'password').send_keys('password')
        time.sleep(2)
        #LoginHit
        driver.find_element(By.ID, 'login-btn').click()

        time.sleep(2)

        driver = self.driver
        search_terms = ["Naruto", "One Piece"]
        for term in search_terms:
            driver.find_element(By.ID, 'manga-search').clear()
            driver.find_element(By.ID, 'manga-search').send_keys(term)
            time.sleep(1)
            search_button = driver.find_element(By.XPATH, "//button[text()='Search']")
            search_button.click()
            self.assertIn(term, driver.page_source)
            time.sleep(2)

        # Search for a term with no results
        driver.find_element(By.ID, 'manga-search').clear()
        driver.find_element(By.ID, 'manga-search').send_keys('Seven Deadly Sins')
        search_button = driver.find_element(By.XPATH, "//button[text()='Search']")
        search_button.click()
        self.assertIn('No manga found', driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
