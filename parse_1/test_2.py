from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class SkillBox(object):
    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        self.driver.get('https://skillbox.ru/courses/?type=course')
        self.driver.find_elements_by_css_selector(".cookies__button")[0].click()
        print(self.driver.title)
        original_window = self.driver.current_window_handle
        links = self.driver.find_elements_by_css_selector(".card--course a")
        for link in links:
            self.driver.execute_script("return arguments[0].scrollIntoView(true);", link)
            print(link.text)
            print(link.get_attribute('href'))
            link.click()
            # new window
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    print('>>'+self.driver.title)
                    print("\n")
                    self.driver.close()
                    self.driver.switch_to.window(original_window)
                    WebDriverWait(self.driver, 10)


    def moreCourses(self):
        self.driver.get('https://skillbox.ru/courses/?type=course')

        xpath_0 = "/html/body/div[1]/div/div/main/div/div[2]/section/button"
        xpath_1 = '//section[contains(@class,"courses-block")]//button[contains(@class,"load-more")]'

        # wait = WebDriverWait(self.driver, 10, ignored_exceptions=[ElementClickInterceptedException])
        # btn_1 = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_1)))
        # button = self.driver.find_element_by_xpath(xpath_1)

        # print(btn_1.text)
        # print(btn_1.get_attribute("class"))

        actions = ActionChains(self.driver)
        btn_1 = self.driver.find_element_by_xpath(xpath_1)
        print(btn_1.rect)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)

        self.driver.execute_script("return arguments[0].scrollIntoView(true);", btn_1)

        # actions.move_to_element_with_offset(btn_1,0,0)
        # actions.key_down(Keys.DOWN)

        for i in range(2):
            actions.click(btn_1)

        # actions.key_down(Keys.UP)

        print("!")
        actions.perform()

        sleep(3)
        self.parse()



        #
        # btn_1.click()

        sleep(5)

def main():
    chromedriver_path_snap = '/snap/bin/chromium.chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path_snap)
    # driver.get('http://ya.ru')
    # print(driver.title)
    # button = driver.find_elements_by_css_selector(".button_theme_websearch")
    # print(button)
    # button[0].click()
    # sleep(3)
    sb = SkillBox(driver)
    sb.parse()


if __name__ == '__main__':
    main()
