import os
import unittest

from selenium import webdriver

from POM.Pages.reportViewFunctionality import ReportViewFunctionality


class ReportViewTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        """setUp function is a class method which is by default called before each test is conducted."""

        cls.driver = webdriver.Chrome(os.path.abspath('Drivers/chromedriver'))
        """chrome driver is required to for testing to work on chrome. """

        cls.driver.get('https://p2dev.ownedoutcomes.com')
        """driver.get calls the site which is to be tested."""

        # cls.driver.get('//http://192.168.2.53:4210')
        cls.driver.maximize_window()
        """to maximize the browser window."""
        cls.report_view = ReportViewFunctionality(cls.driver)

    def test_01_creating_view(self):
        """Test to check if reportview can be created."""

        self.report_view.create_view_script('TestReportView')

    def test_02_cancel_create_view(self):
        """Test to check that reportview is not created when the cancel button is clicked."""

        self.report_view.cancel_create_view('DoNotCreateThisView')

    def test_03_edit_view_name(self):
        """Test to check if name of reportview can be edited."""

        self.report_view.edit_view_name('TestReportView', 'CreateAnotherView')

    def test_04_cancel_edit_view_name(self):
        """Test to check that name of reportview is not edited when cancel button is clicked."""

        self.report_view.cancel_edit_view_name('CreateAnotherView', 'DoNotCreateThisView')

    def test_05_cancel_delete_view(self):
        """Test to check that reportview is not deleted when the cancel button is clicked."""

        self.report_view.cancel_delete_view('CreateAnotherView')

    def test_06_create_view_with_same_name(self):
        """Test to check that the reportview is not created if a reportview with same already exists."""

        self.report_view.create_view_with_same_name('CreateAnotherView')

    def test_07_cancel_copy_view(self):
        """Test to check if the reportview is created when we try to copy a view and click on cancel."""

        self.report_view.cancel_copy_view('CreateAnotherView', 'CreateAnotherTestView')

    def test_08_copy_with_same_name(self):
        """Test to check if the validation appears when we try to copy a view with a name which already exists."""

        self.report_view.copy_with_same_name_validation('CreateAnotherView')

    def test_09_copy_with_no_name(self):
        """Test to check if the validation appears when we try to copy a view with no name"""

        self.report_view.copy_with_no_name_validation('CreateAnotherView')

    def test_10_copy_view(self):
        """Test to check if a copy of reportview can be created with different name."""

        self.report_view.copy_view('CreateAnotherView', 'CreateAnotherTestView')

    def test_11_go_to_map_view(self):
        """Test to check if we can navigate to map view by selecting a view."""

        self.report_view.go_to_graph_view('CreateAnotherView')

    def test_12_go_back_to_landing_page_through_back_button(self):
        """Test to check if we can go back to landing page by clicking on back button of browser."""

        self.report_view.go_back_to_landing_page_through_back_button('CreateAnotherView')

    def test_13_go_back_to_landing_page_through_logo(self):
        """Test to check if we can go back to landing page by clicking on the logo."""

        self.report_view.go_back_to_landing_page_through_logo('CreateAnotherView')

    def test_14_accept_button_greyed_while_editing(self):
        """Test to check if the accept button is greyed while editing and no change in name."""

        self.report_view.check_accept_button_greyed_while_editing_no_name_change('CreateAnotherView')

    def test_15_create_view_with_no_name(self):
        """Test to check if the validation appears when we try to create a view with no name"""

        self.report_view.create_view_with_no_name()

    def test_16_filters_inactive_when_no_dataset_selected(self):
        """Test to check if the filters are inactive when no dataset is selected."""

        self.report_view.filters_inactive_without_dataset('CreateAnotherView')

    def test_99_delete_view(self):
        """Test to check if the reportview can be deleted."""

        self.report_view.delete_view_script('CreateAnotherView')


if __name__ == '__main__':
    unittest.main()
