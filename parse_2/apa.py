import os
import pprint
import env
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint

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

    def quit():
        self.driver.quit()

    def _write_txt(self, text, filename, subdir=".", ext='txt'):
        file = os.path.join(os.getcwd(),'download_test',subdir,filename+'.'+ext)
        f = open(file, "w")
        f.write(text)
        f.close()

    def auth(self):
        pass

    def page(self, url, subdir):
        text = ""
        self.driver.get(url)
        xpath = '//*[@id="lesson-editor"]/div[2]/div[1]/div/div/p[2]/a'
        links = self.driver.find_elements_by_xpath(xpath)
        text += "Main links:"+"\n"
        text += "\n"
        for link in links:
            text += link.text+"\n"
            text += link.get_attribute('href')+"\n"
        ts = self.driver.find_elements_by_link_text("Трек 1")
        text += "\n"
        text += "Tasks:"+"\n"
        for t in ts:
            text += t.get_attribute('href')+"\n"
        self._write_txt(text,self.driver.title,subdir)

    def _list_item(self, url, subdir):
        """ Open in new window, parse, close window """
        # open new window
        original_window = self.driver.current_window_handle
        # self.driver.switch_to.new_window('window')    # not work
        self.driver.execute_script("window.open('');")
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # parse
        self.page(url, subdir)
        print(self.driver.title)
        sec = 3+randint(1,7)
        print(f"Wait for {sec} seconds...")
        sleep(sec)
        # close of new window and return
        self.driver.close()
        self.driver.switch_to.window(original_window)
        print("\n")


    def list(self, url, subdir):
        text = ""
        self.driver.get(url)
        xpath = '//*[@data-item-type="lesson"][*]//a'
        links = self.driver.find_elements_by_xpath(xpath)
        text += "URL: "+self.driver.current_url+"\n"
        text += "\n"
        for link in links:
            text += link.text+"\n"
            url = link.get_attribute('href')
            text += url +"\n"
            self._list_item(url, subdir)
        self._write_txt(text,'list',subdir)

    def document(self, url):
        self.driver.get(url)


    def links_test(self):
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

    def test(self):
        pass

a = Apa()

a.list(*for_list_1)
# a.test()
