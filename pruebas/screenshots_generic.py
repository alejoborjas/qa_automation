from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


class Screenshots():

    def test(self):
        driverLocation = "C:\\Users\\Alejandro\\Documents\\Taller QA\\Practica\\drivers\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(driverLocation, options=options)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        
        driver.find_element_by_xpath("//*[@id='navbar']/div/div/button").click()
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        self.takeScreenshot(driver)

    def takeScreenshot(self, driver):
        """
        Takes screenshot of the current open web page
        :param driver
        :return:
        """
        fileName = "prueba de taller" + ".png"
        screenshotDirectory = "C:\\Users\\Alejandro\\Documents\\Taller QA\\Practica\\"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")


ff = Screenshots()
ff.test()
