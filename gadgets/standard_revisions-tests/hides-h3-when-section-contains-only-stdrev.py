# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class HidesH3WhenSectionContainsOnlyStdrev(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://en.cppreference.com/"
        self.verificationErrors = []
    
    def test_hides_h3_when_section_contains_only_stdrev(self):
        driver = self.driver
        driver.get(self.base_url + "/w/test-gadget-stdrev/hides-h3-when-section-contains-only-stdrev")
        try: self.assertTrue(driver.find_element_by_id("Should_be_removed_in_cxx98").is_displayed())
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_css_selector("select")).select_by_visible_text("C++98/03")
        try: self.assertFalse(driver.find_element_by_id("Should_be_removed_in_cxx98").is_displayed())
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_css_selector("select")).select_by_visible_text("C++11")
        try: self.assertTrue(driver.find_element_by_id("Should_be_removed_in_cxx98").is_displayed())
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()