import time
import unittest

import POM.fixtures.references as r
from POM.fixtures.utils import Utils, Position


class DatasetFunctionality(unittest.TestCase):
    def __init__(self, driver):
        """Here are the required initialisations"""
        self.driver = driver
        self.utils = Utils(self.driver)
        self.utils.create_view(Position.TOP, "TestDataset")

    def apply_dataset(self, name):
        """Function used to apply dataset demoD in given view name."""

        self.utils.open_view(name)
        self.utils.hover_over_side_panel()
        time.sleep(3)
        self.utils.select_dataset_demoD()
        time.sleep(3)
        self.utils.click_by_xpath(r.dataset_apply_button_xpath)  # Do this via id. id is provided
        time.sleep(3)

    def cancel_apply_datatset(self, name):
        """Function to select dataset and then click cancel"""

        self.utils.click_by_id(r.view_name_id + name)
        time.sleep(3)
        self.utils.hover_over_side_panel()
        self.utils.select_dataset_demoD()
        time.sleep(3)
        self.utils.click_by_xpath(r.dataset_cancel_button_xpath)
        time.sleep(3)
        self.assertFalse(self.utils.check_element_displayed_by_xpath(r.dataset_increment_side_panel_xpath))
        """assert to check that the dataset is not applied."""

    def dataset_increment_panel_opens_and_closes_on_clicking_plus(self):
        """Function which confirms if the dataset panel opens and closes when increment button is pressed."""

        self.utils.click_by_xpath(r.dataset_add_button_xpath)
        self.assertTrue(self.utils.check_element_displayed_by_xpath(r.dataset_increment_side_panel_xpath))
        """assert to check if the dataset panel is open"""
        self.utils.click_by_xpath(r.dataset_add_button_xpath)
        self.assertFalse(self.utils.check_element_displayed_by_xpath(r.dataset_increment_side_panel_xpath))
        """assert to check if the dataset panel is closed."""

    def dataset_upload_name_required_validation_displayed(self, name):
        """Function to upload a dataset with no name"""

        time.sleep(3)
        self.utils.click_by_id(r.view_name_id + name)
        time.sleep(3)
        self.utils.hover_over_side_panel()
        self.utils.click_by_xpath(r.dataset_add_button_xpath)
        time.sleep(3)
        self.utils.click_by_xpath(r.dataset_upload_button_xpath)
        time.sleep(3)
        error_message = "Please name your dataset."
        assert error_message in self.driver.page_source
        """assert to check if the no name validation is displayed."""

    def dataset_upload_same_name_validation_message_displayed(self, name, dataset_name):
        """Function to upload a dataset with a name which already exists."""

        time.sleep(3)
        self.utils.click_by_id(r.view_name_id + name)
        time.sleep(3)
        self.utils.hover_over_side_panel()
        self.utils.click_by_xpath(r.dataset_add_button_xpath)
        time.sleep(3)
        self.utils.type_text(r.dataset_upload_name_textbox_id, dataset_name)
        self.utils.click_by_xpath(r.dataset_upload_button_xpath)
        time.sleep(3)
        error_message = "The name already exists. Please enter a different name for your dataset."
        assert error_message in self.driver.page_source
        """assert to check if the same name validation is displayed."""

    # def dataset_allusers_and_groups_unchecked_but_name_error_displayed(self, name):
    #     time.sleep(3)
    #     self.utils.click_by_id(r.view_name_id + name)
    #     self.utils.hover_over_side_panel()
    #     self.utils.click_by_xpath(r.dataset_add_button_xpath)
    #     time.sleep(3)
    #     self.utils.click_by_id(r.dataset_all_users_and_groups_checkbox_id)#incomplete
