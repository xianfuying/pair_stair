import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPairStair(unittest.TestCase):
    def test_should_create_pair_stairs(self):
        #go to page
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/create")
        self.assertEqual(driver.title, "Create Programmers")
        #input programmer names
        add_programmer_names_element = driver.find_element(By.CSS_SELECTOR, "#programmer_names")
        add_programmer_names_element.send_keys("Minkey, Minnie, Donald, Golf")
        #click on add button
        driver.find_element(By.CSS_SELECTOR, "#add_programmers").click()
        #Assert Pair Stair displayed
        self.assertEqual(driver.title, "Pair Stairs")

        driver.find_element(By.CSS_SELECTOR, "#stairs")
        names = driver.find_elements(By.CSS_SELECTOR, ".name")
        self.assertEqual(6, len(names))
        self.assertEqual("Minkey", driver.find_element(By.CSS_SELECTOR, ".column .name").text)
        self.assertEqual("Minnie", driver.find_element(By.CSS_SELECTOR, ".row .name").text)
        self.assertEqual(6, len(driver.find_elements(By.CSS_SELECTOR, ".row .pair")))

    def test_should_show_error_message_when_create_pair_stairs_with_less_than_two_programmers(self):
        #go to create page
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/create")
        #input one programmer name
        driver.find_element(By.CSS_SELECTOR, "#programmer_names").send_keys("Minkey")
        #submit
        driver.find_element(By.CSS_SELECTOR, "#add_programmers").click()
        #assert display error message
        self.assertEqual(driver.title, "Error")
        error_message = driver.find_element(By.CSS_SELECTOR, ".error_message")
        self.assertEqual(error_message.text, "You couldn't create pair stair with less than two programmers!")

