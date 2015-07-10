from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits enter accidentally when the input
        # box is empty.

        # Home page refreshes, tells her that list items can't be blank

        # Tries again, with some text, now it works

        # Amazingly, accidentally enters blank item again

        # Againl, she gets the error message again

        # again, able to correct it by entering some text
        self.fail("write me!")
