import time
import unittest

import POM.fixtures.references as r
from POM.fixtures.utils import Utils, Position


class ReportViewFunctionality(unittest.TestCase):

    def __init__(self, driver):
        """Here are the required initialisations"""

        self.driver = driver
        self.utils = Utils(self.driver)

    """Note: Each test creates a view by calling create_view function,
     tests the functionality and deletes the all created views by calling delete_view function."""

    def create_view_script(self,
                           name):
        """This function calls the create_view function twice.
        One to test create view for top and one create view for bottom.
        delete_view function is also called so that no residue views are left after test."""

        time.sleep(5)
        self.utils.create_view(Position.TOP, name)
        # self.utils.create_view(Position.BOTTOM, name)

    def cancel_create_view(self, name):
        """This function clicks on the createview button on the top , enters the name of the reportview but clicks on
        the cancel icon  and checks if the reportview is created or not.
        The test will only pass if no such reportview is created."""

        time.sleep(5)
        self.utils.click_by_xpath(r.create_add_icon_top_xpath)
        time.sleep(3)
        self.utils.click_by_id(r.cancel_icon_id, )
        time.sleep(3)
        assert name not in self.driver.page_source
        """assert command checks if the reportview is present on the page or not.
        In this case it should not be present to pass this test."""

    def edit_view_name(self, previous_name, current_name):
        """This function attempts to change the name of the view which is provided as previous_name parameter
         into the name provided in current_name parameter by clicking on the edit icon of the reportview."""
        time.sleep(3)
        self.utils.click_by_id(r.edit_view_icon_id + previous_name)
        self.utils.type_text(r.name_textbox_id, current_name)
        self.utils.click_by_id(r.accept_icon_id + previous_name)
        time.sleep(20)
        name_of_reportview = self.driver.find_element_by_id(r.view_name_id + current_name).text
        self.assertTrue(name_of_reportview == current_name)
        """assert command checks if the reportview with the current_name as the name is present on the page or not.
        It should be present to pass this test."""

    def cancel_edit_view_name(self, previous, intended):
        """This function attempts to change the name of the view which is provided as previous_name parameter
         into the name provided in current_name parameter by clicking on the edit icon of the reportview but
         instead of clicking accept button it clicks on cancel button so that the reportview name is not edited."""

        self.utils.click_by_id(r.edit_view_icon_id + previous)
        self.utils.type_text(r.name_textbox_id, intended)
        self.utils.click_by_id(r.cancel_icon_id + previous)
        time.sleep(10)
        name_of_reportview = self.driver.find_element_by_id(r.view_name_id + previous).text
        self.assertTrue(name_of_reportview == previous)
        """Here assert checks if the previous reportview is present or not.
        it should be present ot pass the test."""
        assert intended not in self.driver.page_source
        assert previous in self.driver.page_source
        """Here assert checks if the previous reportview is present or not.
                it should not be present ot pass the test."""

    def delete_view_script(self, name):
        """This function calls the delete_view function to delete the reportview with name as provided name parameter"""

        self.utils.delete_view(name)

    def cancel_delete_view(self, name):
        """This function attempts to delete the reportview with the name as provided in the name parameter
        and clicks cancel so that the reportview is not deleted."""

        self.utils.click_by_id(r.trash_view_icon_id + name)
        time.sleep(5)
        self.utils.click_by_id(r.trash_view_cancel_button_id + name)
        time.sleep(20)
        name_of_reportview = self.driver.find_element_by_id(r.view_name_id + name).text
        self.assertTrue(name_of_reportview == name)
        """assert command checks if the reportview is present on the page or not.
        It should be present to pass this test."""

    def copy_view(self, source_name, current_name):
        """This function creates a copied reportview with the name as provided in current_name parameter by clicking
        on the copy button of the reportview  with the name as provided in source_name."""

        self.utils.click_by_id(r.copy_view_icon_id + source_name)
        time.sleep(3)
        self.utils.type_text(r.name_textbox_id, current_name)
        self.utils.click_by_id(r.accept_icon_id)
        time.sleep(20)
        name_of_reportview = self.driver.find_element_by_id(r.view_name_id + current_name).text
        self.assertTrue(name_of_reportview == current_name)
        """assert command checks if the reportview is present on the page or not.
        It should be present to pass this test."""
        self.utils.delete_view(current_name)

    def cancel_copy_view(self, source_name, current_name):
        """This function attempts to copy a reportview by clicking on cancel button
        after typing the name for copying view."""

        self.utils.click_by_id(r.copy_view_icon_id + source_name)
        """clciks on the copy button of the provided source_name view"""
        time.sleep(3)
        self.utils.type_text(r.name_textbox_id, current_name)
        self.utils.click_by_id(r.cancel_icon_id)
        time.sleep(20)
        assert current_name not in self.driver.page_source

    def copy_with_no_name_validation(self, source_name):
        """This function attempts to copy a reportview and saving the copied view without name
        to see the validation message"""

        self.utils.click_by_id(r.copy_view_icon_id + source_name)
        time.sleep(3)
        self.utils.click_by_id(r.accept_icon_id)
        time.sleep(3)
        error_message = "Name field cannot be blank."
        assert error_message in self.driver.page_source
        """Assert to check if validation message is displayed or not."""

    def copy_with_same_name_validation(self, source_name):
        """This function attempts to copy a reportview and saving the copied view with a name which
        already exists."""

        self.utils.click_by_id(r.copy_view_icon_id + source_name)
        time.sleep(3)
        self.utils.type_text(r.name_textbox_id, source_name)
        self.utils.click_by_id(r.accept_icon_id)
        time.sleep(3)
        error_message = "This name already exists. Please select a different name for your view."
        assert error_message in self.driver.page_source
        """Assert to check if validation message is displayed or not."""

    def create_view_with_same_name(self, name):
        """The function attempts to create a reportview of which name already exists to see the validation message."""

        time.sleep(3)
        self.utils.click_by_xpath(r.create_add_icon_top_xpath)
        time.sleep(3)
        self.utils.type_text(r.name_textbox_id, name)
        self.utils.click_by_id(r.accept_icon_id)
        time.sleep(3)
        error_message = "This name already exists, please choose another for your view."
        assert error_message in self.driver.page_source
        """assert command checks if the error message is displayed on the page or not.
        It should be present to pass this test."""

    def create_view_with_no_name(self):
        """This function attempts to create a view with no name to see the validation message"""

        time.sleep(3)
        self.utils.click_by_xpath(r.create_add_icon_top_xpath)
        time.sleep(3)
        self.utils.type_text(r.view_name_id, "")
        error_message = "Name field cannot be blank."
        assert error_message in self.driver.page_source
        """assert command checks if the error message is displayed on the page or not.
        It should be present to pass this test."""

    def save_view_with_dataset_and_filters_selected(self, name):
        """This functions selects dataset and filters for given view and saves it."""

        self.utils.open_view(name)
        self.utils.hover_over_side_panel()
        self.utils.select_dataset_demoD()
        # add serviceline selecting code and other filters

    def go_to_graph_view(self, name):
        """This function opens a given view and checks if it has navigated to graph view."""

        self.utils.open_view(name)
        self.assertTrue(r.graph_view_url == self.driver.current_url)
        """assert to check if we have navigated to graph view """

    def go_back_to_landing_page_through_logo(self, name):
        """This function clicks the p2 logo to see if we navigated to the landing page."""

        self.utils.open_view(name)
        self.utils.click_by_xpath(r.p2_logo_xpath)
        self.assertTrue(r.landing_page_url == self.driver.current_url)
        """assert to check if we have indeed navigated to landing page."""

    def go_back_to_landing_page_through_back_button(self, name):
        """This function clicks the back button of browser to see if we navigated to the landing page."""

        self.utils.open_view(name)
        self.driver.back()
        self.assertTrue(r.landing_page_url == self.driver.current_url)
        """assert to check if we have indeed navigated to landing page."""

    def check_accept_button_greyed_while_editing_no_name_change(self, name):
        """This function checks if the accept button is greyed or not while editing with no change in name."""

        self.utils.click_by_id(r.edit_view_icon_id + name)
        time.sleep(3)
        assert r.inactive_accept_button_class in self.driver.page_source
        """assert to check if the button is greyed or not"""

    def filters_inactive_without_dataset(self, name):
        """This function opens a vie and checks with no dataset if the filters are inactive or not."""

        self.utils.open_view(name)
        self.utils.hover_over_side_panel()
        assert r.filter_location_increment_button_active_class in self.driver.page_source
        assert r.filter_serviceline_increment_button_active_class in self.driver.page_source
        assert r.filter_entity_increment_button_active_class in self.driver.page_source
        assert r.filter_time_increment_button_active_class in self.driver.page_source
        """assert to check if the filters are inactive. They should be"""
