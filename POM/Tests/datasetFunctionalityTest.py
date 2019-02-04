import os
import unittest

from selenium import webdriver

from POM.Pages.datatsetFunctionality import DatasetFunctionality


class DatasetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(os.path.abspath('Drivers/chromedriver'))
        """chrome driver is required to for testing to work on chrome. """
        cls.driver.get('https://p2dev.ownedoutcomes.com')
        """driver.get calls the site which is to be tested."""
        # cls.driver.get('http://192.168.2.53:4208')
        cls.driver.maximize_window()
        """to maximize the browser window."""

    @classmethod
    def setUp(cls):
        """setUp function is a class method which is by default called before each test is conducted."""

        cls.driver = webdriver.Chrome(os.path.abspath('Drivers/chromedriver'))
        """chrome driver is required to for testing to work on chrome. """

        cls.driver.get('https://p2dev.ownedoutcomes.com')
        """driver.get calls the site which is to be tested."""

        # cls.driver.get('http://192.168.2.53:4208')
        cls.driver.maximize_window()
        """to maximize the browser window."""
        cls.dataset = DatasetFunctionality(cls.driver)

    def test_01_dataset_increment_panel_opens_and_closes_on_clicking_plus(self):
        """Test to check if the dataset panel opens and closes when increment button is pressed"""

        self.dataset.dataset_increment_panel_opens_and_closes_on_clicking_plus()

    def test_02_cancel_apply_dataset(self):
        """Test to check if dataset is apllied if we clock on cancel after selecting dataset to apply."""

        self.dataset.cancel_apply_datatset('TestDataset')

    def test_03_dataset_upload_name_required_validation_displayed(self):
        """Test to chech if validation is displayed wyhen attempted to upload a dataset with no name."""

        self.dataset.dataset_upload_name_required_validation_displayed('TestDataset')

    def test_04_dataset_upload_same_name_validation_displayed(self):
        self.dataset.dataset_upload_same_name_validation_message_displayed('TestDataset', 'demoD')

    def test_05_dataset_allusers_and_groups_unchecked_but_name_error_displayed(self):
        pass
        # add code

    @classmethod
    def tearDown(cls):
        """tearDown function is a class method which is by default called after each test is conducted."""

        cls.driver.close()
        """closes the tab of browser"""

        cls.driver.quit()
        """quits the browser"""


if __name__ == '__main__':
    unittest.main()
