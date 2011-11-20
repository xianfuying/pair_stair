import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPairStair(unittest.TestCase):
    def test_should_create_pair_stairs(self):
        self.add_programmers()
        #Assert Pair Stair displayed
        self.assertEqual(self.driver.title, "Pair Stairs")
        self.driver.find_element(By.CSS_SELECTOR, "#stairs")
        names = self.driver.find_elements(By.CSS_SELECTOR, ".row")
        self.assertEqual(3, len(names))
        self.assertEqual("Minkey", self.driver.find_element(By.CSS_SELECTOR, ".column .nameMinkey").text)
        self.assertEqual("Minnie", self.driver.find_element(By.CSS_SELECTOR, ".row .nameMinnie").text)
        self.assertEqual(6, len(self.driver.find_elements(By.CSS_SELECTOR, ".row .pair")))

    def test_should_show_error_message_when_create_pair_stairs_with_less_than_two_programmers(self):
        #go to create page
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/create")
        #input one programmer name
        self.driver.find_element(By.CSS_SELECTOR, "#programmer_names").send_keys("Minkey")
        #submit
        self.driver.find_element(By.CSS_SELECTOR, "#add_programmers").click()
        #assert display error message
        self.assertEqual(self.driver.title, "Error")
        error_message = self.driver.find_element(By.CSS_SELECTOR, ".error_message")
        self.assertEqual(error_message.text, "You couldn't create pair stair with less than two programmers!")

    def test_should_add_by_one_when_clicked_on_the_count_of_pair(self):
        #go to stairs page
        self.add_programmers()
        self.driver.get("http://localhost:8000/stairs")
        #click on the pair count
        pair_count = self.driver.find_element(By.CSS_SELECTOR, ".pair a")
        self.assertEqual('0', pair_count.text)
        pair_count.click()
        #assert pair count add by one
        pair_count = self.driver.find_element(By.CSS_SELECTOR, ".pair a")
        self.assertEqual('1', pair_count.text)

    def add_programmers(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/create")
        self.assertEqual(self.driver.title, "Create Programmers")
        #input programmer names
        add_programmer_names_element = self.driver.find_element(By.CSS_SELECTOR, "#programmer_names")
        add_programmer_names_element.send_keys("Minkey, Minnie, Donald, Golf")
        #click on add button
        self.driver.find_element(By.CSS_SELECTOR, "#add_programmers").click()

    def tearDown(self):
        self.driver.close()
