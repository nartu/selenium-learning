import os
import env
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Apa(object):
    """Parsing and save"""
    uri = env.base_uri

    def __init__(self):
        self.driver = self._initDriver()

    def _initDriver(self):
        os.system("killall chrome")
        # Options
        chromedriver_path_snap = '/snap/bin/chromium.chromedriver'
        chrome_user_data_dir = '/home/julia/snap/chromium/common/chromium/Default'
        # chrome_user_data_dir = os.path.join(os.getcwd(),'user-data')
        # Driver init
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--user-data-dir="+chrome_user_data_dir)
        driver = webdriver.Chrome(executable_path=chromedriver_path_snap, chrome_options=chrome_options)
        return driver

    def auth(self):
        pass

    def links(self):
        self.driver.get(self.uri)
        # links = self.driver.find_elements_by_css_selector("a")
        # //*[@id="group-with-lesson-grid-container"]/table/tbody/tr[1]/td[8]/a
        # $x('//*[@id="group-with-lesson-grid-container"]/table//tr[2]/td[@data-col-seq="nextLessonTitle"]/a')[0].innerText
        # xpath = '//*[@id="group-with-lesson-grid-container"]/table//td[@data-col-seq="nextLessonTitle"]'
        xpath = '//*[@id="group-with-lesson-grid-container"]/table//tr[*]/td[@data-col-seq="nextLessonTitle"]/a'
        links_count = len(self.driver.find_elements_by_xpath(xpath))
        original_window = self.driver.current_window_handle
        print(f'Original window: {original_window}')
        print(f'Links: {links_count}')
        for l in range(1,links_count+1):
            xpath = f'//*[@id="group-with-lesson-grid-container"]/table//tr[{l}]/td[@data-col-seq="nextLessonTitle"]/a'
            link = self.driver.find_element_by_xpath(xpath)
            print(link)
            # self.driver.execute_script("return arguments[0].scrollIntoView(true);", link)
            print(link.text)
            print(link.get_attribute('href'))
            link.click()
            # links_inner = self.driver.find_elements_by_css_selector("a")
            print('>>'+self.driver.title)
            print("\n")
            # for li in links_inner:
            #     print("\t" + li.text)
            #     print("\t" + li.get_attribute('href')+"\n")
            self.driver.back()
            # WebDriverWait(self.driver, 10)
            # print(f'All window: {self.driver.window_handles}')







a = Apa()

# print(os.path.join(os.getcwd(),'user-data'))
a.links()
