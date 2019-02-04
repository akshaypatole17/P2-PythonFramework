import time
import unittest
from enum import Enum

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import POM.fixtures.references as r


class Position(Enum):
    """Enum is used to indicate position of createview button"""
    TOP = 'top'
    BOTTOM = 'bottom'
    OUTSIDE = 'outside'
    INSIDE = 'inside'


class Utils(unittest.TestCase):
    def __init__(self, driver):
        """Here are the required initialisations"""
        self.driver = driver

    def create_view(self, position, name):
        """This function which creates view with given name parameter.
        It requires us to mention the position of createview button which needs to be used."""

        if position == Position.TOP:
            time.sleep(5)
            """Sleep functions are used to let the user see. They are also used to let the page load before
            the WebDriverWait tries to find the element for which it needs to wait. Note:Removing them may cause error
            depending upon your network"""
            self.click_by_xpath(r.create_add_icon_top_xpath)
            time.sleep(3)
        elif position == Position.BOTTOM:
            time.sleep(3)
            # self.driver.find_element(By.CSS_SELECTOR, 'icon-plus.down').click()
            # self.driver.find_element_by_class_name("icon-plus").click()
            # try:
            #     WebDriverWait(self.driver, float(5)).until(
            #         EC.((By.CLASS_NAME, 'icon-plus down'))).click()
            #     """Here the bottom createview button is clicked."""
            # except StaleElementReferenceException:
            #     self.driver.implicitly_wait(2)
            #     WebDriverWait(self.driver, float(10)).until(
            #         EC.element_to_be_clickable((By.XPATH, self.create_add_icon_bottom_xpath))).click()
            #     """Here the bottom createview button is clicked."""
        self.type_text(r.name_textbox_id, name)
        self.click_by_id(r.accept_icon_id)
        time.sleep(5)
        self.driver.refresh()
        try:
            WebDriverWait(self.driver, float(5)).until(
                EC.element_to_be_clickable((By.ID, r.view_name_id + name)))
            name_of_reportview = self.driver.find_element_by_id(r.view_name_id + name).text
            self.assertTrue(name_of_reportview == name)
        except StaleElementReferenceException:
            self.driver.implicitly_wait(5)
            """driver.implicitly_wait keeps the driver in stand by state for the given time(seconds)"""
            WebDriverWait(self.driver, float(10)).until(
                EC.element_to_be_clickable((By.ID, r.view_name_id + name)))
            name_of_reportview = self.driver.find_element_by_id(r.view_name_id + name).text
            self.assertTrue(name_of_reportview == name)

        """assert command checks if the reportview is present on the page or not.
        It should be present to pass this test."""

    def delete_view(self, name):
        """This function deletes the view with the name  as provided name parameter."""

        time.sleep(10)
        self.click_by_id(r.trash_view_icon_id + name)
        time.sleep(3)
        self.click_by_id(r.trash_view_confirm_button_id + name)
        time.sleep(20)
        self.driver.refresh()
        assert name not in self.driver.page_source
        """assert command checks if the reportview is present on the page or not.
                It should not be present to pass this test."""

    def open_view(self, name):
        time.sleep(3)
        self.click_by_id(r.view_name_id + name)

    def click_by_id(self, id):
        try:
            """WebDriverWait pauses the function until the button for which id or xpath is provided to be clickable
            and the clicks it. If the element take more time to load an exception is thrown.
            Exception is handles by making the function wait for more time."""

            WebDriverWait(self.driver, float(5)).until(
                EC.element_to_be_clickable((By.ID, id))).click()
        except StaleElementReferenceException:
            self.driver.implicitly_wait(2)
            WebDriverWait(self.driver, float(10)).until(
                EC.element_to_be_clickable((By.ID, id))).click()

    def click_by_xpath(self, xpath):
        try:
            """WebDriverWait pauses the function until the button for which id or xpath is provided to be clickable
            and the clicks it. If the element take more time to load an exception is thrown.
            Exception is handles by making the function wait for more time."""

            WebDriverWait(self.driver, float(5)).until(
                EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except StaleElementReferenceException:
            self.driver.implicitly_wait(2)
            WebDriverWait(self.driver, float(10)).until(
                EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def hover_over_side_panel(self):
        """This function hovers over the side panel so that the panel opens"""

        actions = ActionChains(self.driver)
        side_panel = self.driver.find_element_by_xpath(r.side_panel_xpath)
        actions.move_to_element(side_panel).perform()
        time.sleep(3)

    def type_text(self, textbox_id, text):
        """This functions types the given text in the textbox of which id is provided."""

        time.sleep(3)
        self.driver.find_element_by_id(textbox_id).clear()
        self.driver.find_element_by_id(r.name_textbox_id).send_keys(text)

    def select_dataset_demoD(self):
        """Checks the checkbox of demoD dataset in drop down list of datasets, but does not apply it."""

        self.click_by_xpath(r.dataset_add_button_xpath)
        self.click_by_xpath(r.dataset_demoD_xpath)

    def check_element_displayed_by_xpath(self, reference):
        """generic function to click on element of given xpath."""

        try:
            element = self.driver.find_element(By.XPATH, reference)
            return True
        except NoSuchElementException:
            return False

    def check_element_displayed_by_id(self, reference):
        """generic function to click on element of given xpath."""

        try:
            element = self.driver.find_element(By.ID, reference)
            return True
        except NoSuchElementException:
            return False
